from .strategy import Strategy
from ..block_map import BlockMap
from ..internal import Self, Position
from ..tetriminos.tetrimino import Tetrimino
from ..tetriminos import TetriminoType
import random


class RandomStrategy(Strategy):
    def generate_tetrimino(self, position: Position) -> Tetrimino:
        tetrimino_type = random.choice(list(TetriminoType.__members__))
        return TetriminoType.create_tetrimino(tetrimino_type, position)

    def update_block_map(self: Self, block_map: BlockMap) -> Self:
        pass
