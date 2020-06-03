from enum import IntEnum, auto
from internal import Position, Self
from .entity import Entity
from .i_tetrimino import ITetrimino
from .j_tetrimino import JTetrimino
from .l_tetrimino import LTetrimino
from .o_tetrimino import OTetrimino
from .s_tetrimino import STetrimino
from .t_tetrimino import TTetrimino
from .z_tetrimino import ZTetrimino
from .i_penta import IPenta


class TetriminoType(IntEnum):
    I = auto()
    J = auto()
    L = auto()
    O = auto()
    S = auto()
    T = auto()
    Z = auto()

    @classmethod
    def create_tetrimino(cls: Self, constant: Self, position: Position) -> Entity:
        if constant is cls.I:
            return ITetrimino(position)
        elif constant is cls.J:
            return JTetrimino(position)
        elif constant is cls.L:
            return LTetrimino(position)
        elif constant is cls.O:
            return OTetrimino(position)
        elif constant is cls.S:
            return STetrimino(position)
        elif constant is cls.T:
            return TTetrimino(position)
        elif constant is cls.Z:
            return ZTetrimino(position)
        else:
            raise RuntimeError("Can not create tetrimino by this type {0}".format(constant))


class PentaType(IntEnum):
    I = auto()
    LeftT = auto()
    Right = auto()

    @classmethod
    def create_penta(cls: Self, constant: Self, position: Position) -> Entity:
        if constant is cls.I:
            return IPenta(position)
