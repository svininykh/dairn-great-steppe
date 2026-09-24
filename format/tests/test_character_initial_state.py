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
        expected = {"abilities", "hp", "armor", "inventory", "talisman", "fatigue",
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
        states = {hero["id"]: hero["initial-state"] for hero in book["heroes"]}
        horse = {"companions": {"items": [{"kind": "Верховой конь"}]}}
        self.assertEqual({"aibike": horse, "karashash": horse, "yersin": {}}, states)

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
