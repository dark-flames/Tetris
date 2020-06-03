from .entity import Entity, BlockVectors
from config.color import Color
from internal import Vec


class RightShortTPenta(Entity):
    def get_block_vectors(self) -> BlockVectors:
        return BlockVectors([
            [Vec([-2, 0]), Vec([-1, 0]), Vec([0, 0]), Vec([1, 0]), Vec([0, 1])],
            [Vec([0, 0]), Vec([0, 1]), Vec([0, 2]), Vec([0, 3]), Vec([1, 1])],
            [Vec([-2, 1]), Vec([-1, 1]), Vec([0, 1]), Vec([1, 1]), Vec([-1, 0])],
            [Vec([0, 0]), Vec([0, 1]), Vec([0, 2]), Vec([0, 3]), Vec([-1, 2])]
        ])

    @property
    def color(self) -> Color:
        return Color.BLUE
