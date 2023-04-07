from dataclasses import dataclass


@dataclass(frozen=True)
class Todo:
    id: int
    name: str
    is_completed: bool
