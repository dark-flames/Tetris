from .strategy import Strategy
from block_map import BlockMap
from internal import Self, Position
from entities.entity import Entity
from entities.tetrimino_types import TetriminoType
import random


class RandomTetrisStrategy(Strategy):
    def generate_tetrimino(self, position: Position) -> Entity:
        tetrimino_type = random.choice(list(TetriminoType))
        return TetriminoType.create_tetrimino(tetrimino_type, position)

    def update_block_map(self: Self, block_map: BlockMap) -> Self:
        pass
