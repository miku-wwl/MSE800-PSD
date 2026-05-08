"""Week 4 - Activity 2

OOP class for a rectangular piece of land.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RectangleLand:
    length: float
    width: float

    def __post_init__(self) -> None:
        if self.length <= 0 or self.width <= 0:
            raise ValueError("Length and width must be positive numbers.")

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)
