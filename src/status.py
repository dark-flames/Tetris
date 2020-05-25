from enum import Enum
from pyxel import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT, btn
from .internal import Self


class KeyStatus(Enum):
    NORMAL = None
    ACCELERATED_DROP = KEY_DOWN
    ROTATE = KEY_UP
    MOVE_LEFT = KEY_LEFT
    MOVE_RIGHT = KEY_RIGHT

    @classmethod
    def get_status(cls: Self) -> Self:
        for status in cls:
            if btn(status.value):
                return status

        return KeyStatus.NORMAL
