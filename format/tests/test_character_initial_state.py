"""Contract tests for Issue #24; no external reader or runtime is required."""

import copy
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

import yaml
from jsonschema import Draft202012Validator

FORMAT = Path(__file__).resolve().parents[1]
ROOT = FORMAT.parent
sys.path.insert(0, str(FORMAT))
from validate_characters import SCHEMA_PATH, read_book, validate_book


class CharacterInitialStateTests(unittest.TestCase):
    def load(self, path):
        return read_book(path.read_text(encoding="utf-8"))

    def assert_valid(self, book):
        original = copy.deepcopy(book)
        self.assertEqual([], validate_book(book))
        self.assertEqual(original, book, "Validation must not fill or alter data")

    def test_schema_is_valid(self):
        Draft202012Validator.check_schema(json.loads(SCHEMA_PATH.read_text()))

    def test_legacy_book_without_state(self):
        book = self.load(FORMAT / "tests/fixtures/legacy-book.yaml")
        self.assert_valid(book)
        for hero in book["heroes"]:
            self.assertNotIn("initial-state", hero)
        self.assertNotIn("name", book["heroes"][1])
        self.assertNotIn("npcs", book)

    def test_book_without_character_lists(self):
        self.assert_valid({"book-id": "no-characters"})

    def test_missing_and_empty_state_remain_distinct(self):
        book = read_book("heroes:\n- id: absent\n- id: empty\n  initial-state: {}\n")
        self.assert_valid(book)
        self.assertNotIn("initial-state", book["heroes"][0])
        self.assertEqual({}, book["heroes"][1]["initial-state"])

    def test_partial_state_does_not_gain_values(self):
        state = {"hp": {"current": 2}, "inventory": {"items": [{"name": "Посох"}]}}
        book = {"heroes": [{"id": "partial", "initial-state": state}]}
        self.assert_valid(book)
        self.assertNotIn("maximum", state["hp"])
        self.assertNotIn("complete", state["inventory"])
        self.assertEqual({"name": "Посох"}, state["inventory"]["items"][0])
        self.assertNotIn("armor", state)

    def test_examples_cover_all_supported_state_fields(self):
        book = self.load(FORMAT / "examples/character-initial-states.yaml")
        self.assert_valid(book)
        full = next(h["initial-state"] for h in book["heroes"] if h["id"] == "fully-authored")
        expected = {"age", "appearance", "abilities", "hp", "armor", "inventory", "talisman", "fatigue",
                    "deprived", "critical-damage", "scars", "features", "words", "companions"}
        self.assertEqual(expected, set(full))

    def test_hero_and_npc_have_the_same_contract(self):
        for collection in ("heroes", "npcs"):
            for state in ({}, {"hp": {"current": 0}}, {"abilities": {"str": 20}}):
                with self.subTest(collection=collection, state=state):
                    self.assert_valid({collection: [{"id": "character", "initial-state": state}]})

    def test_states_are_independent(self):
        book = read_book("""heroes:
  - id: first
    initial-state: {hp: {current: 1}}
  - id: second
    initial-state: {hp: {current: 4}}
npcs:
  - id: third
    initial-state: {}
""")
        self.assert_valid(book)
        book["heroes"][0]["initial-state"]["hp"]["current"] = 0
        self.assertEqual(4, book["heroes"][1]["initial-state"]["hp"]["current"])
        self.assertEqual({}, book["npcs"][0]["initial-state"])

    def test_zero_false_and_empty_collections_are_preserved(self):
        state = {"abilities": {"str": 0}, "hp": {"current": 0},
                 "armor": {"value": 0}, "fatigue": 0, "deprived": False,
                 "scars": {"complete": True, "items": []}}
        self.assert_valid({"heroes": [{"id": "zero", "initial-state": state}]})

    def test_null_and_placeholder_values_are_rejected(self):
        for state in (None, "", {"hp": None}, {"hp": {"current": None}},
                      {"inventory": {"items": [{"name": ""}]}},
                      {"inventory": {"items": [{"name": "   "}]}},
                      {"companions": {"complete": None}}):
            with self.subTest(state=state):
                self.assertTrue(validate_book({"heroes": [{"id": "a", "initial-state": state}]}))

    def test_invalid_types_and_ranges_are_rejected(self):
        for state in ({"fatigue": -1}, {"deprived": 0}, {"abilities": {"str": True}},
                      {"hp": {"current": "2"}}, {"armor": {"value": 4}},
                      {"inventory": {"items": [{"slots": 3}]}},
                      {"talisman": {"slots": 1}}):
            with self.subTest(state=state):
                self.assertTrue(validate_book({"heroes": [{"id": "a", "initial-state": state}]}))

    def test_description_and_unknown_keys_are_not_state(self):
        for field in ("name", "description", "portrait", "role", "player", "hpo"):
            with self.subTest(field=field):
                self.assertTrue(validate_book({"heroes": [{"id": "a", "initial-state": {field: "x"}}]}))

    def test_state_at_book_level_is_rejected(self):
        self.assertTrue(validate_book({"initial-state": {}}))

    def test_duplicate_ids_within_and_across_lists_are_rejected(self):
        for book in ({"heroes": [{"id": "a"}, {"id": "a"}]},
                     {"npcs": [{"id": "a"}, {"id": "a"}]},
                     {"heroes": [{"id": "a"}], "npcs": [{"id": "a"}]}):
            with self.subTest(book=book):
                self.assertTrue(validate_book(book))

    def test_duplicate_yaml_keys_are_rejected(self):
        for source in ("heroes: []\nheroes: []", "heroes:\n- id: a\n  initial-state:\n    fatigue: 1\n    fatigue: 2"):
            with self.subTest(source=source):
                with self.assertRaises(yaml.YAMLError):
                    read_book(source)

    def test_collection_completeness_is_explicit(self):
        for value in ({}, {"items": []}, {"items": [], "complete": False},
                      {"items": [], "complete": True}):
            with self.subTest(value=value):
                self.assert_valid({"heroes": [{"id": "a", "initial-state": {"inventory": value}}]})
        self.assertTrue(validate_book({"heroes": [{"id": "a", "initial-state": {"inventory": {"complete": True}}}]}))

    def test_known_hp_bounds_are_checked_without_filling_missing_bounds(self):
        for hp in ({}, {"current": 2}, {"maximum": 1}, {"current": 0, "maximum": 1}):
            self.assert_valid({"heroes": [{"id": "a", "initial-state": {"hp": hp}}]})
        self.assertTrue(validate_book({"heroes": [{"id": "a", "initial-state": {"hp": {"current": 2, "maximum": 1}}}]}))

    def test_companion_references(self):
        book = {"heroes": [{"id": "a", "initial-state": {"companions": {"items": [{"character-id": "b"}]}}}],
                "npcs": [{"id": "b", "initial-state": {}}]}
        self.assert_valid(book)
        del book["npcs"]
        self.assertTrue(validate_book(book))

    def test_pilot_has_only_confirmed_initial_facts(self):
        book = self.load(ROOT / "books/battles-of-the-great-steppe-pilot/book.yaml")
        self.assert_valid(book)
        self.assertEqual({"aibike", "karashash"}, {hero["id"] for hero in book["heroes"]})
        self.assertEqual(["yersin"], [npc["id"] for npc in book["npcs"]])
        states = {c["id"]: c["initial-state"] for c in book["heroes"] + book["npcs"]}
        self.assertEqual({"aibike": 18, "karashash": 23, "yersin": 21},
                         {key: state["age"] for key, state in states.items()})
        for state in states.values():
            # No numerical character stats, later injuries, or invented resources.
            self.assertLessEqual(set(state), {"age", "appearance", "inventory", "companions"})
            for key in ("inventory", "companions"):
                if key in state:
                    self.assertNotIn("complete", state[key])
            for item in state["inventory"]["items"]:
                self.assertNotIn("uses", item)
                self.assertNotIn("монист", item["name"]["ru"].lower())
        for character_id in ("aibike", "karashash"):
            state = states[character_id]
            self.assertEqual(["Riding horse"],
                             [c["kind"] for c in state["companions"]["items"]])
            self.assertEqual(["Короткий лук + колчан со стрелами"],
                             [i["name"]["ru"] for i in state["inventory"]["items"]])
        self.assertNotIn("companions", states["yersin"])
        self.assertEqual({"Қамшы (плеть)", "Сокольничья перчатка", "Поясной подсумок"},
                         {i["name"]["ru"] for i in states["yersin"]["inventory"]["items"]})
        for item in states["yersin"]["inventory"]["items"]:
            if item["name"]["ru"] != "Қамшы (плеть)":
                self.assertNotIn("damage", item)
                self.assertNotIn("slots", item)
        # Editing one runtime copy must not affect either other character.
        before = copy.deepcopy(states)
        states["aibike"]["inventory"]["items"].clear()
        states["aibike"]["companions"]["items"].clear()
        self.assertEqual(before["karashash"], states["karashash"])
        self.assertEqual(before["yersin"], states["yersin"])

    def test_pilot_weapon_parameters_match_market(self):
        # Read the source table so changes to Market cannot silently leave
        # stale weapon numbers in the pilot's authored manifest.
        market = {}
        source = (ROOT / "dairn/tables/basic-equipment-master.md").read_text(encoding="utf-8")
        for line in source.splitlines():
            if line.startswith("| "):
                cells = [cell.strip() for cell in line.strip("|").split("|")]
                if len(cells) == 4 and cells[1].startswith("d") and cells[2].isdigit():
                    market[cells[0]] = (cells[1], int(cells[2]))
        book = self.load(ROOT / "books/battles-of-the-great-steppe-pilot/book.yaml")
        for character in book["heroes"] + book["npcs"]:
            weapons = [i for i in character["initial-state"]["inventory"]["items"] if "damage" in i]
            self.assertTrue(weapons, character["id"])
            for item in weapons:
                with self.subTest(character=character["id"], item=item["name"]):
                    self.assertIn(item["name"]["ru"], market)
                    self.assertEqual(market[item["name"]["ru"]], (item["damage"], item["slots"]))
                    for note in item["notes"].values():
                        self.assertIn("dairn/tables/basic-equipment-master.md", note)

    def test_localized_text_at_all_supported_positions(self):
        for value in ("Legacy text", {"kk": "Мәтін"}, {"ru": "Текст"},
                      {"kk": "Мәтін", "ru": "Текст", "en": "Text"}):
            for collection in ("heroes", "npcs"):
                character = {"id": "example", "name": value,
                             "description": value, "notes": value,
                             "initial-state": {
                                 "inventory": {"items": [{"name": value, "notes": value}]},
                                 "talisman": {"name": value, "notes": value},
                                 "companions": {"items": [{"name": value, "notes": value}]}}}
                book = {collection: [character]}
                with self.subTest(value=value, collection=collection):
                    self.assert_valid(book)
                    self.assertEqual(book, read_book(yaml.safe_dump(book, allow_unicode=True)))

    def test_age_is_optional_and_requires_nonnegative_whole_years(self):
        for collection in ("heroes", "npcs"):
            for state in ({}, {"age": 0}, {"age": 21}):
                self.assert_valid({collection: [{"id": "a", "initial-state": state}]})
            for age in (-1, 18.5, True, "18", None, {"en": "18"}):
                with self.subTest(collection=collection, age=age):
                    self.assertTrue(validate_book({collection: [{"id": "a", "initial-state": {"age": age}}]}))

    def test_appearance_uses_partial_numeric_table_results(self):
        categories = ("physique", "skin", "hair", "face", "clothing")
        for collection in ("heroes", "npcs"):
            for appearance in ({}, {"hair": 2}, {key: 10 for key in categories}):
                self.assert_valid({collection: [{"id": "a", "initial-state": {"appearance": appearance}}]})
            for key in categories:
                for value in (0, 11, -1, 2.5, True, None, "Braided", {"en": "Braided"}):
                    with self.subTest(collection=collection, key=key, value=value):
                        self.assertTrue(validate_book({collection: [{"id": "a", "initial-state": {
                            "appearance": {key: value}}}]}))
            for key in ("speech", "virtue", "flaw", "unknown"):
                self.assertTrue(validate_book({collection: [{"id": "a", "initial-state": {
                    "appearance": {key: 1}}}]}))

    def test_pilot_appearance_references_existing_localized_rows(self):
        book = self.load(ROOT / "books/battles-of-the-great-steppe-pilot/book.yaml")
        # Category order is the same in the master and all three localizations.
        categories = ("physique", "skin", "hair", "face", "speech", "clothing", "virtue", "flaw")
        for locale in ("master", "kk", "ru", "en"):
            text = (ROOT / f"dairn/tables/character-traits-8d10-{locale}.md").read_text(encoding="utf-8")
            sections = text.split("\n## ")[1:]
            self.assertEqual(len(categories), len(sections))
            rows = {}
            for category, section in zip(categories, sections):
                rows[category] = {}
                for line in section.splitlines():
                    cells = [part.strip() for part in line.strip("|").split("|")]
                    if line.startswith("|") and len(cells) == 2 and cells[0].isdigit():
                        rows[category][int(cells[0])] = cells[1]
            for character in book["heroes"] + book["npcs"]:
                appearance = character["initial-state"]["appearance"]
                self.assertEqual({"physique", "skin", "hair", "face", "clothing"}, set(appearance))
                for category, result in appearance.items():
                    self.assertIn(result, rows[category])
                    self.assertTrue(rows[category][result])
                for excluded in ("speech", "virtue", "flaw"):
                    self.assertNotIn(excluded, appearance)

    def test_invalid_localized_text_is_rejected_at_all_positions(self):
        for value in ({}, {"de": "Text"}, {"kk": ""}, {"ru": "   "},
                      {"en": None}, {"kk": 42}, {"en": {"en": "Text"}}, []):
            for field in ("name", "description", "notes"):
                self.assertTrue(validate_book({"heroes": [{"id": "a", field: value}]}))
            for field in ("name", "notes"):
                for state in ({"inventory": {"items": [{field: value}]}},
                              {"talisman": {field: value}},
                              {"companions": {"items": [{field: value}]}}):
                    with self.subTest(value=value, field=field, state=state):
                        self.assertTrue(validate_book({"npcs": [{"id": "a", "initial-state": state}]}))

    def test_technical_fields_do_not_accept_localization_maps(self):
        value = {"en": "technical"}
        self.assertTrue(validate_book({"heroes": [{"id": value}]}))
        for state in ({"inventory": {"items": [{"kind": value}]}},
                      {"inventory": {"items": [{"damage": value}]}},
                      {"inventory": {"items": [{"properties": {"items": [value]}}]}},
                      {"companions": {"items": [{"kind": value}]}},
                      {"companions": {"items": [{"character-id": value}]}}):
            self.assertTrue(validate_book({"heroes": [{"id": "a", "initial-state": state}]}))

    def test_pilot_display_fields_have_three_languages(self):
        book = self.load(ROOT / "books/battles-of-the-great-steppe-pilot/book.yaml")

        def check(node):
            if isinstance(node, dict):
                for key, value in node.items():
                    if key in ("name", "description", "notes"):
                        self.assertIsInstance(value, dict)
                        self.assertEqual({"kk", "ru", "en"}, set(value))
                    else:
                        check(value)
            elif isinstance(node, list):
                for value in node:
                    check(value)

        check(book)

    def test_yaml_roundtrip_preserves_authored_values_and_omissions(self):
        book = self.load(FORMAT / "examples/character-initial-states.yaml")
        reread = read_book(yaml.safe_dump(book, allow_unicode=True))
        self.assertEqual(book, reread)
        self.assert_valid(reread)

    def test_read_book_manifest_from_dairn_zip(self):
        # The unchanged container carries the manifest; this is not a full ZIP validator.
        for path in (FORMAT / "tests/fixtures/legacy-book.yaml",
                     ROOT / "books/battles-of-the-great-steppe-pilot/book.yaml"):
            with self.subTest(path=path):
                data = io.BytesIO()
                with zipfile.ZipFile(data, "w") as archive:
                    archive.writestr("book.yaml", path.read_bytes())
                    archive.writestr("dairn-package.yaml", 'package-format: dairn-book-package\npackage-version: "0.1"\nbook: book.yaml\n')
                data.seek(0)
                with zipfile.ZipFile(data) as archive:
                    book = read_book(archive.read("book.yaml"))
                self.assertEqual(self.load(path), book)
                self.assert_valid(book)

    def test_cli_success_and_failure(self):
        for path, expected in ((FORMAT / "examples/character-initial-states.yaml", 0),
                               (FORMAT / "tests/fixtures/nonexistent.yaml", 1)):
            result = subprocess.run([sys.executable, "-B", str(FORMAT / "validate_characters.py"), str(path)],
                                    capture_output=True, text=True)
            self.assertEqual(expected, result.returncode, result.stderr)
        with tempfile.TemporaryDirectory(prefix="dairn-format-test-") as directory:
            path = Path(directory) / "invalid.yaml"
            # Temporary test data, never an authored book.
            path.write_text("heroes:\n- id: invalid\n  initial-state: null\n", encoding="utf-8")
            result = subprocess.run([sys.executable, "-B", str(FORMAT / "validate_characters.py"), str(path)],
                                    capture_output=True, text=True)
            self.assertEqual(1, result.returncode)
            self.assertIn("initial-state", result.stderr)


if __name__ == "__main__":
    unittest.main()
