from dataclasses import dataclass, field
from typing import Self


@dataclass
class Rect:
    label: str = ""
    pos: list[int] = field(default_factory=lambda: [0, 0])

    def translate_x(self, by: int) -> Self:
        self.pos[0] += by
        return self

    def translate_y(self, by: int) -> Self:
        self.pos[1] += by
        return self
