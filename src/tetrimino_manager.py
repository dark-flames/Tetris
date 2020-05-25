from .strategy.strategy import Strategy
from .internal import Self, Position, Counter
from .config.config import Config
from .block_map import BlockMap
from .tetriminos.tetrimino import Tetrimino
from typing import Optional


class TetriminoManager:
    __config: Config
    __tick_counter: Counter
    __strategy: Strategy
    block_map: BlockMap
    __current_tetrimino: Optional[Tetrimino]

    def __init__(self, config: Config) -> None:
        self.__config = config
        self.__tick_counter = Counter()

    def set_strategy(self: Self, strategy: Strategy) -> Self:
        self.__strategy = strategy
        return self

    def __new_tetrimino(self) -> None:
        self.__current_tetrimino = self.__strategy.generate_tetrimino(
            Position(self.__config.size[0] // 2 + 1, self.__config.size[1])
        )

    def __update_after_move(self):
        if not self.block_map.can_drop(self.__current_tetrimino.blocks):
            self.block_map.achieve(self.__current_tetrimino)
            self.__new_tetrimino()
            self.__tick_counter.init()

    def __drop(self) -> None:
        if self.block_map.check(self.__current_tetrimino.peek_drop().blocks):
            self.__current_tetrimino.drop()
            self.__update_after_move()

    def __move_right(self) -> None:
        if self.block_map.check(self.__current_tetrimino.peek_right().blocks):
            self.__current_tetrimino.move_right()
            self.__update_after_move()

    def __move_left(self) -> None:
        if self.block_map.check(self.__current_tetrimino.peek_left().blocks):
            self.__current_tetrimino.move_left()
            self.__update_after_move()

    def process_tick(self, accelerate: bool) -> None:
        if not self.__tick_counter.count % 2 or accelerate:
            self.__drop()
        self.__tick_counter.incr()

    def process_left_and_right(self, is_left: bool) -> None:
        if is_left:
            self.__move_left()
        else:
            self.__move_right()
