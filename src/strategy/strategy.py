from abc import ABC, abstractmethod

from entities.entity import Entity
from block_map import BlockMap
from internal import Self, Position
from config.difficulty import Difficulty
from random import choice


class Strategy(ABC):
    @abstractmethod
    def generate_tetrimino(self, position: Position) -> Entity:
        ...

    def generate_penta(self, position: Position) -> Entity:
        ...

    def generate_tri(self, position: Position) -> Entity:
        ...

    def generate_ex(self, position: Position) -> Entity:
        ...

    def generate_inv(self, position: Position) -> Entity:
        ...

    def generate_entity(self, position: Position, difficulty: Difficulty) -> Entity:
        if difficulty == Difficulty.EASY:
            return self.generate_tetrimino(position)
        elif difficulty == Difficulty.NORMAL:
            return self.generate_penta(position)
        elif difficulty == Difficulty.VERY_EASY:
            return choice([
                self.generate_tri,
                self.generate_tetrimino
            ])(position)
        elif difficulty == Difficulty.HARD:
            return choice([
                self.generate_tetrimino,
                self.generate_penta
            ])(position)
        elif difficulty == Difficulty.EX:
            return choice([
                self.generate_tetrimino,
                self.generate_penta,
                self.generate_ex,
                self.generate_inv
            ])(position)
        elif difficulty == Difficulty.VERY_HARD:
            return choice([
                self.generate_tetrimino,
                self.generate_penta,
                self.generate_ex
            ])(position)
        elif difficulty == Difficulty.INV:
            return choice([
                self.generate_tetrimino,
                self.generate_inv
            ])(position)

    @abstractmethod
    def update_block_map(self: Self, block_map: BlockMap) -> Self:
        ...
