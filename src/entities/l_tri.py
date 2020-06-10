from .entity import Entity, BlockVectors
from internal import Vec
from config.color import Color


class LTri(Entity):
    def get_block_vectors(self) -> BlockVectors:
        return BlockVectors([
            [Vec([0, 0]), Vec([0, 1]), Vec([1, 0])],
            [Vec([0, 0]), Vec([0, -1]), Vec([1, 0])],
            [Vec([0, 0]), Vec([0, -1]), Vec([-1, 0])],
            [Vec([0, 0]), Vec([0, 1]), Vec([-1, 0])]
        ])

    @property
    def color(self) -> Color:
        return Color.PINK
