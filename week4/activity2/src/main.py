"""Week 4 - Activity 2

User input program: calculate area and perimeter of a rectangular land.
"""

from __future__ import annotations

from rectangle_land import RectangleLand


def read_positive_float(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if value <= 0:
            print("Please enter a positive number (> 0).")
            continue

        return value


def main() -> None:
    print("Rectangle Land - Area & Perimeter")
    length = read_positive_float("Enter the length: ")
    width = read_positive_float("Enter the width: ")

    land = RectangleLand(length=length, width=width)
    print(f"\nArea: {land.area():.2f}")
    print(f"Perimeter: {land.perimeter():.2f}")


if __name__ == "__main__":
    main()
