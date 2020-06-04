from enum import IntEnum, auto
import pyxel


class Difficulty(IntEnum):
    EASY = auto()
    NORMAL = auto()
    HARD = auto()

    @classmethod
    def get_difficulty(cls, string: str):
        if string == 'easy':
            return cls.EASY
        elif string == 'normal':
            return cls.NORMAL
        elif string == 'hard':
            return cls.HARD

    def play_sound(self):
        if self == self.EASY:
            sound = 0
        elif self == self.NORMAL:
            sound = 1
        elif self == self.HARD:
            sound = 2

        pyxel.play(sound, sound, loop=True)

    @staticmethod
    def register_sound():
        pyxel.sound(0).set(
            "E3E3E3E3 D3D3D3D3 C3C3C3C3 D3D3D3D3",
            "S",
            "6",
            "FFFF FFFF FFFF FFFF",
            60
        )
        pyxel.sound(1).set(
            "E1E1E1E1 D1D1D1D1 C1C1C1C1 D1D1D1D1",
            "S",
            "6",
            "FFFF FFFF FFFF FFFF",
            60
        )
        pyxel.sound(2).set(
            "C2D2E2F2G2A2B2C3",
            "S",
            "6",
            "FFFF FFFF ",
            60
        )
