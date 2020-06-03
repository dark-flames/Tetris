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
from .left_short_t_penta import LeftShortTPenta
from .right_short_t_penta import RightShortTPenta
from .j_penta import JPenta
from .l_penta import LPenta
from .t_penta import TPenta
from .p_penta import PPenta
from .q_penta import QPenta
from .c_penta import CPenta
from .s_penta import SPenta
from .z_penta import ZPenta
from .x_penta import XPenta
from .big_l_penta import BigLPenta


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
    LEFT_SHORT_T = auto()
    RIGHT_SHORT_T = auto()
    L = auto()
    J = auto()
    T = auto()
    P = auto()
    Q = auto()
    C = auto()
    S = auto()
    Z = auto()
    X = auto()
    BIG_L = auto()

    @classmethod
    def create_penta(cls: Self, constant: Self, position: Position) -> Entity:
        if constant is cls.I:
            return IPenta(position)
        elif constant is cls.LEFT_SHORT_T:
            return LeftShortTPenta(position)
        elif constant is cls.RIGHT_SHORT_T:
            return RightShortTPenta(position)
        elif constant is cls.L:
            return LPenta(position)
        elif constant is cls.J:
            return JPenta(position)
        elif constant is cls.T:
            return TPenta(position)
        elif constant is cls.P:
            return PPenta(position)
        elif constant is cls.Q:
            return QPenta(position)
        elif constant is cls.C:
            return CPenta(position)
        elif constant is cls.S:
            return SPenta(position)
        elif constant is cls.Z:
            return ZPenta(position)
        elif constant is cls.X:
            return XPenta(position)
        elif constant is cls.BIG_L:
            return BigLPenta(position)
