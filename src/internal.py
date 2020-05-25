from typing import List, Tuple, TypeVar
from dataclasses import dataclass
from time import time_ns

Size = Tuple[int, int]
Vec = Tuple[int, int]
Self = TypeVar("Self")


@dataclass
class Position:
    x: int
    y: int

    def __add__(self: Self, other: Vec) -> Self:
        return Position(
            x=self.x + other[0],
            y=self.y + other[1]
        )

    def peek(self: Self, vec: Vec) -> Self:
        return self + vec

    def below(self: Self) -> Self:
        return self.peek(Vec(0, -1))

    def above(self: Self) -> Self:
        return self.peek(Vec(0, 1))

    def left(self: Self) -> Self:
        return self.peek(Vec(-1, 0))

    def right(self: Self) -> Self:
        return self.peek(Vec(1, 0))


class Counter:
    count: int

    def __init__(self):
        self.init()

    def init(self):
        self.count = 0

    def incr(self):
        self.count += 1


class Timer:
    __time: int

    def __init__(self):
        self.__time = 0

    def start(self):
        self.__time = time_ns()

    @property
    def time_pass_ns(self) -> int:
        return self.__time

    @property
    def time_pass_ms(self) -> int:
        return self.__time // 1000000


class DeathException(Exception):
    pass


Blocks = List[Position]
