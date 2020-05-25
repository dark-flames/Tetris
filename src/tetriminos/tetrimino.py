from abc import ABC, abstractmethod
from copy import deepcopy
from typing import Tuple

from ..internal import Position, Blocks, Self, Vec, List
from ..config.color import Color

BlockVectors = Tuple[List[Vec], List[Vec], List[Vec], List[Vec]]


class Tetrimino(ABC):
    position: Position
    blocks: Blocks
    __block_vectors: BlockVectors
    __status: int

    def __init__(self, position: Position) -> None:
        self.position = position
        self.__status = 0
        self.__block_vectors = self.get_block_vectors()
        self.update_blocks()

    def peek_left(self: Self) -> Self:
        return deepcopy(self).move_left()

    def move_left(self: Self) -> Self:
        self.position = self.position.left()
        self.update_blocks()
        return self

    def peek_right(self: Self) -> Self:
        return deepcopy(self).move_right()

    def move_right(self) -> Self:
        self.position = self.position.right()
        self.update_blocks()
        return self.position

    def peek_drop(self: Self) -> Self:
        return deepcopy(self).drop()

    def drop(self) -> Self:
        self.position = self.position.below()
        self.update_blocks()
        return self.position

    def peek_rotate(self: Self) -> Self:
        return deepcopy(self).rotate()

    def rotate(self: Self) -> Self:
        self.__status = (self.__status + 1) % 4
        self.update_blocks()
        return self

    def update_blocks(self: Self) -> Self:
        self.blocks = list(
            map(
                lambda vec: self.position + vec,
                self.__block_vectors[self.__status]
            )
        )
        return self

    @abstractmethod
    def get_block_vectors(self) -> BlockVectors:
        ...

    @property
    @abstractmethod
    def color(self) -> Color:
        ...
