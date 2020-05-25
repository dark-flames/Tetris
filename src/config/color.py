from enum import IntEnum
from typing import List, Dict


class Color(IntEnum):
    RED = 0
    PINK = 1
    PURPLE = 2
    DEEP_PURPLE = 3
    INDIGO = 4
    BLUE = 5
    CYAN = 6
    TEAL = 7
    GREEN = 8
    YELLOW = 9
    AMBER = 10
    ORANGE = 11
    BROWN = 12
    GRAY = 13
    DARK = 14
    LIGHT = 15

    @classmethod
    def color_map(cls) -> Dict[int, int]:
        return {
            cls.RED: 0xf44336,
            cls.PINK: 0xe91e63,
            cls.PURPLE: 0x9c27b0,
            cls.DEEP_PURPLE: 0x673ab7,
            cls.INDIGO: 0x3f51b5,
            cls.BLUE: 0x2196f3,
            cls.CYAN: 0x00bcd4,
            cls.TEAL: 0x009688,
            cls.GREEN: 0x4caf50,
            cls.YELLOW: 0xffeb3b,
            cls.AMBER: 0xffc107,
            cls.ORANGE: 0xff9800,
            cls.BROWN: 0x795548,
            cls.GRAY: 0x9e9e9e,
            cls.DARK: 0x002b36,
            cls.LIGHT: 0xfafafa
        }

    @classmethod
    def get_palette(cls) -> List[int]:
        return list(cls.color_map().values())
