from .tetrimino import Tetrimino, BlockVectors
from ..internal import Vec
from ..config.color import Color


class OTetrimino(Tetrimino):
    def get_block_vectors(self) -> BlockVectors:
        return BlockVectors(
            [Vec(-1, 1), Vec(0, 1), Vec(-1, 0), Vec(0, 0)],
            [Vec(-1, 1), Vec(0, 1), Vec(-1, 0), Vec(0, 0)],
            [Vec(-1, 1), Vec(0, 1), Vec(-1, 0), Vec(0, 0)],
            [Vec(-1, 1), Vec(0, 1), Vec(-1, 0), Vec(0, 0)],
        )

    @property
    def color(self) -> Color:
        return Color.YELLOW