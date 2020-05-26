from strategy.strategy import Strategy
from internal import Self, Position, Counter, DeathException
from config.config import Config
from block_map import BlockMap
from tetriminos.tetrimino import Tetrimino
from status import KeyStatus
from typing import Optional


class TetriminoManager:
    __config: Config
    __tick_counter: Counter
    __strategy: Strategy
    current_tetrimino: Optional[Tetrimino]
    block_map: BlockMap

    def __init__(self, config: Config) -> None:
        self.__config = config
        self.set_strategy(self.__config.strategy)
        self.__tick_counter = Counter()
        self.block_map = BlockMap(self.__config.size)
        self.init()

    def init(self: Self) -> Self:
        self.__tick_counter.init()
        self.block_map.init()
        self.current_tetrimino = self.__new_tetrimino()
        return self

    def set_strategy(self: Self, strategy: Strategy) -> Self:
        self.__strategy = strategy
        return self

    def __new_tetrimino(self) -> Tetrimino:
        return self.__strategy.generate_tetrimino(
            Position(self.__config.size[0] // 2 + 1, self.__config.size[1])
        )

    def __update_after_move(self) -> int:
        drop_lines = 0
        if not self.block_map.check(self.current_tetrimino.peek_drop().blocks):
            drop_lines = self.block_map.achieve(self.current_tetrimino)
            if self.block_map.is_lose():
                raise DeathException
            self.__strategy.update_block_map(self.block_map)
            self.current_tetrimino = self.__new_tetrimino()
            self.__tick_counter.init()

        return drop_lines

    def __drop(self) -> None:
        if self.block_map.check(self.current_tetrimino.peek_drop().blocks):
            self.current_tetrimino.drop()

    def __move_right(self) -> None:
        if self.block_map.check(self.current_tetrimino.peek_right().blocks):
            self.current_tetrimino.move_right()

    def __move_left(self) -> None:
        if self.block_map.check(self.current_tetrimino.peek_left().blocks):
            self.current_tetrimino.move_left()

    def __rotate(self) -> None:
        if self.block_map.check(self.current_tetrimino.peek_rotate().blocks):
            self.current_tetrimino.rotate()

    def process_tick(self, status: KeyStatus) -> int:
        tick = self.__tick_counter.count
        self.__tick_counter.incr()

        if status.rotate and tick % self.__config.rotate_sampling_interval == 0:
            self.__rotate()

        accelerate_drop = status.accelerate and tick % self.__config.accelerated_drop_speed == 0
        normal_drop = tick % self.__config.drop_speed == 0

        if accelerate_drop or normal_drop:
            self.__drop()

        if tick % self.__config.left_and_right_sampling_interval == 0:
            if status.left:
                self.__move_left()
            elif status.right:
                self.__move_right()

        return self.__update_after_move()
