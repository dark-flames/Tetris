from .strategy.strategy import Strategy
from .internal import Self, Position, Counter
from .config.config import Config
from .block_map import BlockMap
from .tetriminos.tetrimino import Tetrimino
from .status import KeyStatus
from typing import Optional


class TetriminoManager:
    __config: Config
    __tick_counter: Counter
    __strategy: Strategy
    __current_tetrimino: Optional[Tetrimino]
    block_map: BlockMap

    def __init__(self, config: Config) -> None:
        self.__config = config
        self.set_strategy(self.__config.strategy)
        self.__tick_counter = Counter()

    def set_strategy(self: Self, strategy: Strategy) -> Self:
        self.__strategy = strategy
        return self

    def __new_tetrimino(self) -> None:
        self.__current_tetrimino = self.__strategy.generate_tetrimino(
            Position(self.__config.size[0] // 2 + 1, self.__config.size[1])
        )

    def __update_after_move(self) -> int:
        drop_lines = 0
        if not self.block_map.can_drop(self.__current_tetrimino.blocks):
            drop_lines = self.block_map.achieve(self.__current_tetrimino)
            self.__strategy.update_block_map(self.block_map)
            self.__new_tetrimino()
            self.__tick_counter.init()

        return drop_lines

    def __drop(self) -> int:
        if self.block_map.check(self.__current_tetrimino.peek_drop().blocks):
            self.__current_tetrimino.drop()
            return self.__update_after_move()
        else:
            return 0

    def __move_right(self) -> int:
        if self.block_map.check(self.__current_tetrimino.peek_right().blocks):
            self.__current_tetrimino.move_right()
            return self.__update_after_move()
        else:
            return 0

    def __move_left(self) -> int:
        if self.block_map.check(self.__current_tetrimino.peek_left().blocks):
            self.__current_tetrimino.move_left()
            return self.__update_after_move()
        else:
            return 0

    def __rotate(self) -> int:
        if self.block_map.check(self.__current_tetrimino.peek_rotate().blocks):
            self.__current_tetrimino.rotate()
            return self.__update_after_move()
        else:
            return 0

    def process_tick(self, status: KeyStatus) -> int:
        drop_lines = 0

        tick = self.__tick_counter.count
        self.__tick_counter.incr()

        if status.left:
            drop_lines = self.__move_left()
        elif status.right:
            drop_lines = self.__move_right()

        if drop_lines:
            return drop_lines

        if status.rotate:
            drop_lines = self.__rotate()

        if drop_lines:
            return drop_lines

        if not tick % 2 or status.accelerate:
            drop_lines = self.__drop()

        return drop_lines
