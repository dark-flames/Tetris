from typing import List, Tuple, TypeVar
from dataclasses import dataclass

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


Blocks = List[Position]
