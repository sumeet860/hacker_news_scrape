# Stubs for pprint

# Based on http://docs.python.org/2/library/pprint.html
# Based on http://docs.python.org/3/library/pprint.html

from typing import IO, Any, Dict, Optional, Tuple

def pformat(
    object: object,
    indent: int = ...,
    width: int = ...,
    depth: Optional[int] = ...,
    *,
    compact: bool = ...,
    sort_dicts: bool = ...,
) -> str: ...


def pp(
    object: object,
    stream: Optional[IO[str]] = ...,
    indent: int = ...,
    width: int = ...,
    depth: Optional[int] = ...,
    *,
    compact: bool = ...,
    sort_dicts: bool = ...,
) -> None: ...

def pprint(
    object: object,
    stream: Optional[IO[str]] = ...,
    indent: int = ...,
    width: int = ...,
    depth: Optional[int] = ...,
    *,
    compact: bool = ...,
    sort_dicts: bool = ...,
) -> None: ...


def isreadable(object: object) -> bool: ...
def isrecursive(object: object) -> bool: ...
def saferepr(object: object) -> str: ...

class PrettyPrinter:
    def __init__(
        self,
        indent: int = ...,
        width: int = ...,
        depth: Optional[int] = ...,
        stream: Optional[IO[str]] = ...,
        *,
        compact: bool = ...,
        sort_dicts: bool = ...,
    ) -> None: ...

    def pformat(self, object: object) -> str: ...
    def pprint(self, object: object) -> None: ...
    def isreadable(self, object: object) -> bool: ...
    def isrecursive(self, object: object) -> bool: ...
    def format(self, object: object, context: Dict[int, Any], maxlevels: int, level: int) -> Tuple[str, bool, bool]: ...
