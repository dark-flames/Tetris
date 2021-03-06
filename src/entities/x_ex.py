from .entity import Entity, BlockVectors
from internal import Vec
from config.color import Color


class XEx(Entity):
    def get_block_vectors(self) -> BlockVectors:
        return BlockVectors([
            [Vec([-1, 1]), Vec([1, 1]), Vec([-1, -1]), Vec([1, -1]), Vec([0, 0])],
            [Vec([-1, 1]), Vec([1, 1]), Vec([-1, -1]), Vec([1, -1]), Vec([0, 0])],
            [Vec([-1, 1]), Vec([1, 1]), Vec([-1, -1]), Vec([1, -1]), Vec([0, 0])],
            [Vec([-1, 1]), Vec([1, 1]), Vec([-1, -1]), Vec([1, -1]), Vec([0, 0])],
        ])

    @property
    def color(self) -> Color:
        return Color.BLUE
