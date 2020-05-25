from abc import ABC, abstractmethod

from ..tetriminos.tetrimino import Tetrimino
from ..block_map import BlockMap
from ..internal import Self


class Strategy(ABC):
    @abstractmethod
    def get_next_tetrimino(self) -> Tetrimino:
        ...

    @abstractmethod
    def update_block_map(self: Self, block_map: BlockMap) -> Self:
        ...
