from functools import reduce

from .internal import Size, Blocks, Position
from .tetriminos.tetrimino import Tetrimino
from typing import List, Optional
from .config.color import Color


class BlockMap:
    __size: Size
    __block_map: List[List[Optional[Color]]]

    def __init__(self, size: Size) -> None:
        self.__size = Size
        self.__block_map = []  # (y, x)

        self.__append_lines(self.__size[1])

    def __append_lines(self, count: int):
        for x in range(count):
            self.__block_map.append(
                list(map(lambda y: None, range(self.__size[0]))))

    def get_content(self, position: Position) -> Optional[Color]:
        return self.__block_map[position.y][position.x]

    def set_content(self, position: Position, color: Optional[Color]):
        self.__block_map[position.y][position.x] = color

    def check(self, blocks: Blocks) -> bool:
        for block in blocks:
            if self.get_content(block) is not None:
                return False

        return True

    def can_drop(self, blocks: Blocks) -> bool:
        for block in blocks:
            below = block.below()
            if below.y < 0 or self.get_content(below) is not None:
                return False

        return True

    def achieve(self, tetrimino: Tetrimino) -> int:
        for block in tetrimino.blocks:
            self.set_content(block, tetrimino.color)

        self.__block_map = [
            line
            for line in self.__block_map
            if reduce(lambda c, item: c and item is not None, line, True)
        ]

        drop_lines = self.__size[1] - len(self.__block_map)

        if drop_lines:
            self.__append_lines(drop_lines)

        return drop_lines
