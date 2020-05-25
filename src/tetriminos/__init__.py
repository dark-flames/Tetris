from enum import Enum, auto
from ..internal import Position
from .tetrimino import Tetrimino
from .i_tetrimino import ITetrimino
from .j_tetrimino import JTetrimino
from .l_tetrimino import LTetrimino
from .o_tetrimino import OTetrimino
from .s_tetrimino import STetrimino
from .t_tetrimino import TTetrimino
from .z_tetrimino import ZTetrimino


class TetriminoType(Enum):
    I = auto()
    J = auto()
    L = auto()
    O = auto()
    S = auto()
    T = auto()
    Z = auto()

    @classmethod
    def create_tetrimino(cls, type, position: Position) -> Tetrimino:
        if type == cls.I:
            return ITetrimino(position)
        elif type == cls.J:
            return JTetrimino(position)
        elif type == cls.L:
            return LTetrimino(position)
        elif type == cls.O:
            return OTetrimino(position)
        elif type == cls.S:
            return STetrimino(position)
        elif type == cls.T:
            return TTetrimino(position)
        elif type == cls.Z:
            return ZTetrimino(position)
