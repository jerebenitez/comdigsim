from typing import Any, List


def alphabet_is_valid(alphabet: List[Any]) -> bool:
    return len(set(alphabet)) == len(alphabet)
