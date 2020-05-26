from dataclasses import dataclass
from pyxel import KEY_UP, KEY_RIGHT, KEY_LEFT, KEY_DOWN, btn
from internal import Self


@dataclass
class KeyStatus:
    accelerate: bool
    left: bool
    right: bool
    rotate: bool

    @staticmethod
    def get_status():
        return KeyStatus(
            accelerate=btn(KEY_DOWN),
            left=btn(KEY_LEFT) and not btn(KEY_RIGHT),
            right=btn(KEY_RIGHT) and not btn(KEY_LEFT),
            rotate=btn(KEY_UP),
        )

    def __add__(self: Self, other: Self) -> Self:
        self.accelerate = self.accelerate or other.accelerate
        self.left = self.left or other.left
        self.right = self.right or other.right
        self.rotate = self.rotate or other.rotate
        return self
