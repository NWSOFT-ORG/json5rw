from typing import Any, Callable, Dict

from src.decoder import Decoder

GLOBALS = {
    "__builtins__": {
        "true"    : True,
        "false"   : False,
        "null"    : None,
        "Infinity": float("inf"),
        "NaN"     : float("nan"),
    }
}


def parse(
    string,
    cls: Decoder,
    object_hook: Callable,
    parse_float: Callable,
    parse_int: Callable,
    parse_constant: Callable,
    object_pairs_hook: Callable,
) -> Dict[str, Any]:
    try:
        byte_code = compile(string, "<json>", mode="eval")
        json_object: Dict[str, Any] = eval(byte_code, GLOBALS)

        if cls:
            object_hook = cls.object_hook
            parse_float = cls.parse_float
            parse_int = cls.parse_int
            parse_constant = cls.parse_constant
            object_pairs_hook = cls.object_pairs_hook

        for key, value in json_object.items():  # Apply hooks
            if isinstance(value, dict):
                json_object[key] = object_hook(value)
                object_pairs_hook(value)
            elif value in [float("-inf"), float("inf"), float("nan")]:
                json_object[key] = parse_constant(value)
            elif isinstance(value, int):
                json_object[key] = parse_int(value)
            elif isinstance(value, float):
                json_object[key] = parse_float(value)
        return json_object
    except Exception:
        raise ValueError("Unable to parse JSON content")
