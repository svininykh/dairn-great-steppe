"""Validate the character extension of a book manifest without filling values.

This is not a ZIP, story, or game-rules validator.
"""

import argparse
import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


SCHEMA_PATH = Path(__file__).parent / "schemas/character-initial-state.schema.json"


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject duplicate YAML keys instead of silently losing authored data."""


def _mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str) or key in result:
            raise yaml.constructor.ConstructorError(
                None, None, "Expected a unique string mapping key", key_node.start_mark
            )
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)


def read_book(source):
    """Read a YAML string or stream, preserving omission and explicit emptiness."""
    return yaml.load(source, Loader=UniqueKeyLoader)


def validate_book(book):
    """Return errors, without mutating or normalizing the supplied manifest."""
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    errors = [
        f"{'/'.join(map(str, error.absolute_path)) or '$'}: {error.message}"
        for error in validator.iter_errors(book)
    ]
    if errors:
        return errors

    characters = book.get("heroes", []) + book.get("npcs", [])
    ids = set()
    for character in characters:
        character_id = character["id"]
        if character_id in ids:
            errors.append(f"Duplicate character id: {character_id}")
        ids.add(character_id)

    for character in characters:
        state = character.get("initial-state", {})
        hp = state.get("hp", {})
        if "current" in hp and "maximum" in hp and hp["current"] > hp["maximum"]:
            errors.append(f"{character['id']}: hp.current exceeds hp.maximum")
        for companion in state.get("companions", {}).get("items", []):
            target = companion.get("character-id")
            if target is not None and target not in ids:
                errors.append(f"{character['id']}: unknown companion character-id: {target}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("book", type=Path, help="Path to an unpacked book.yaml")
    args = parser.parse_args()
    try:
        with args.book.open(encoding="utf-8") as source:
            errors = validate_book(read_book(source))
    except (OSError, yaml.YAMLError) as error:
        parser.exit(1, f"{error}\n")
    if errors:
        parser.exit(1, "\n".join(errors) + "\n")
    print(f"Character definitions and initial states valid: {args.book}")


if __name__ == "__main__":
    main()
