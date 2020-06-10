from .strategy import Strategy
from block_map import BlockMap
from internal import Self, Position
from entities.entity import Entity
from entities.entity_types import TetriminoType, PentaType, TriType, ExType, InvType
import random


class RandomTetrisStrategy(Strategy):
    def generate_tetrimino(self, position: Position) -> Entity:
        tetrimino_type = random.choice(list(TetriminoType))
        return TetriminoType.create_tetrimino(tetrimino_type, position)

    def generate_penta(self, position: Position) -> Entity:
        penta_type = random.choice(list(PentaType))
        return PentaType.create_penta(penta_type, position)

    def generate_tri(self, position: Position) -> Entity:
        tri_type = random.choice(list(TriType))
        return TriType.create_tri(tri_type, position)

    def generate_ex(self, position: Position) -> Entity:
        ex_type = random.choice(list(ExType))
        return ExType.create_ex(ex_type, position)

    def generate_inv(self, position: Position) -> Entity:
        inv_type = random.choice(list(InvType))
        return InvType.create_inv(inv_type, position)

    def update_block_map(self: Self, block_map: BlockMap) -> Self:
        pass
