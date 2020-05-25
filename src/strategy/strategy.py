from abc import ABC, abstractmethod

from ..tetriminos.tetrimino import Tetrimino
from ..block_map import BlockMap
from ..internal import Self, Position


class Strategy(ABC):
    @abstractmethod
    def generate_tetrimino(self, position: Position) -> Tetrimino:
        ...

    @abstractmethod
    def update_block_map(self: Self, block_map: BlockMap) -> Self:
        ...
