from abc import ABC, abstractmethod

from entities.entity import Entity
from block_map import BlockMap
from internal import Self, Position


class Strategy(ABC):
    @abstractmethod
    def generate_tetrimino(self, position: Position) -> Entity:
        ...

    def generate_penta(self, position: Position) -> Entity:
        ...

    @abstractmethod
    def update_block_map(self: Self, block_map: BlockMap) -> Self:
        ...
