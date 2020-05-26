from functools import reduce

from internal import Size, Blocks, Position
from tetriminos.tetrimino import Tetrimino
from typing import List, Optional
from config.color import Color


class BlockMap:
    __size: Size
    __block_map: List[List[Optional[Color]]]
    __iter_current_position: Position

    def __init__(self, size: Size) -> None:
        self.__size = size
        self.__iter_current_position = Position(0, 0)

    def __iter__(self):
        self.__iter_current_position = Position(0, 0)
        return self

    def __next__(self):
        current = (self.__iter_current_position, self.get_content(self.__iter_current_position))
        if self.check_border(self.__iter_current_position.right()):
            self.__iter_current_position = self.__iter_current_position.right()
        else:
            self.__iter_current_position = Position(
                0,
                self.__iter_current_position.y + 1
            )
            if not self.check_border(self.__iter_current_position):
                raise StopIteration

        return current

    def init(self):
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

    def check_border(self, position: Position, allow_y_overflow=False) -> bool:
        if self.__size[0] <= position.x or position.x < 0:
            return False
        elif position.y < 0:
            return False
        elif position.y >= self.__size[1] and not allow_y_overflow:
            return False

        return True

    def check(self, blocks: Blocks) -> bool:
        for block in blocks:
            if not self.check_border(block, True):
                return False

            if not self.check_border(block):
                return True

            if self.get_content(block) is not None:

                return False

        return True

    def is_lose(self) -> bool:
        return reduce(
            lambda c, x: c or x is not None,
            self.__block_map[self.__size[1] - 1],
            False
        )

    def achieve(self, tetrimino: Tetrimino) -> int:
        for block in tetrimino.blocks:
            if self.check_border(block):
                self.set_content(block, tetrimino.color)

        self.__block_map = [
            line
            for line in self.__block_map
            if reduce(lambda c, item: c or item is None, line, False)
        ]

        drop_lines = self.__size[1] - len(self.__block_map)

        if drop_lines:
            self.__append_lines(drop_lines)

        return drop_lines
