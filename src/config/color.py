from enum import Enum
from typing import List


class Color(Enum):
    RED = "#f44336"
    PINK = "#e91e63"
    PURPLE = "#9c27b0"
    DEEP_PURPLE = "#673ab7"
    INDIGO = "#3f51b5"
    BLUE = "#2196f3"
    CYAN = "#00bcd4"
    TEAL = "#009688"
    GREEN = "#4caf50"
    YELLOW = "#ffeb3b"
    AMBER = "#ffc107"
    ORANGE = "#ff9800"
    BROWN = "#795548"
    GRAY = "#9e9e9e"
    DARK = "#002b36"
    LIGHT = "##fafafa"

    @classmethod
    def get_palette(cls, constant) -> List[str]:
        return list(cls.__members__.values())
