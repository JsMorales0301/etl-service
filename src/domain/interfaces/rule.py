from typing import Protocol, TypeVar, Any

T = TypeVar("T")

class Rule(Protocol[T]):
    name: str
    def apply(self, data: T, context: dict[str, Any] | None = None) -> T:
        ...
