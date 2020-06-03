from enum import IntEnum, auto


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
