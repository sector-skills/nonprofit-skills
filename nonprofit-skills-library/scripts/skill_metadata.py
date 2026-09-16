"""Read portable metadata, with legacy top-level fields accepted during transition."""
import re

try:
    import yaml
except ImportError:
    raise SystemExit("Install script dependencies: python3 -m pip install -r scripts/requirements.txt")

CUSTOM_FIELDS = ("supervision", "supervision_note", "last_reviewed", "date_added", "date_added_source")
FRONTMATTER = re.compile(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|$)", re.S)


class UniqueKeyLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str) or key in result:
            raise ValueError("Frontmatter keys must be unique strings")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def read_metadata(text):
    match = FRONTMATTER.match(text)
    if not match:
        raise ValueError("Missing or malformed YAML frontmatter")
    try:
        fields = yaml.load(match.group(1), Loader=UniqueKeyLoader)
    except yaml.YAMLError as exc:
        raise ValueError(f"Invalid YAML: {exc}") from exc
    if not isinstance(fields, dict):
        raise ValueError("Frontmatter must be a mapping")
    nested = fields.get("metadata", {})
    if not isinstance(nested, dict):
        raise ValueError("metadata must be a mapping")
    result = dict(fields)
    for key in CUSTOM_FIELDS:
        if key in nested:
            if key in fields and str(fields[key]) != str(nested[key]):
                raise ValueError(f"Conflicting top-level and metadata.{key}")
            result[key] = nested[key]
    return result
