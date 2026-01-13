from typing import Dict, Any
from marshmallow import Schema


def load_dict(schema: Schema, data: Any) -> Dict[str, Any]:
    result = schema.load(data)
    assert isinstance(result, dict)
    return result
