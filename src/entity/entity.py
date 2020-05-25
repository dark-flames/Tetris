from abc import ABC, abstractmethod
from typing import Tuple, List, TypeVar
from ..config.color import Color
from copy import deepcopy

Position = Tuple[int, int]
Blocks = List[Position]
Self = TypeVar("Self")


class Entity(ABC):
    position: Position
    blocks: Blocks

    def __init__(self, x: int, y: int) -> None:
        self.position = (x, y)

    def peek_left(self: Self) -> Self:
        return deepcopy(self).move_left()

    def move_left(self: Self) -> Self:
        self.position[0] -= 1
        self.update_blocks()
        return self

    def peek_right(self: Self) -> Self:
        return deepcopy(self).move_right()

    def move_right(self) -> Self:
        self.position[0] += 1
        self.update_blocks()
        return self.position

    def peek_drop(self: Self) -> Self:
        return deepcopy(self).drop()

    def drop(self) -> Self:
        self.position[1] -= 1
        self.update_blocks()
        return self.position

    @abstractmethod
    def rotate(self: Self) -> Self:
        ...

    @abstractmethod
    def update_blocks(self: Self) -> Self:
        ...

    @property
    @abstractmethod
    def color(self) -> Color:
        ...
