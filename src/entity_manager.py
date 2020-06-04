from strategy.strategy import Strategy
from internal import Self, Position, Counter, DeathException
from config.config import Config
from block_map import BlockMap
from entities.entity import Entity
from status import KeyStatus
from typing import Optional


class EntityManager:
    __config: Config
    __tick_counter: Counter
    __strategy: Strategy
    current_entity: Optional[Entity]
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
        self.current_entity = self.__new_entity()
        return self

    def set_strategy(self: Self, strategy: Strategy) -> Self:
        self.__strategy = strategy
        return self

    def __new_entity(self) -> Entity:
        return self.__strategy.generate_entity(
            Position(self.__config.size[0] // 2 + 1, self.__config.size[1]),
            self.__config.difficulty
        )

    def __update_after_move(self) -> int:
        drop_lines = 0
        if not self.block_map.check(self.current_entity.peek_drop().blocks):
            drop_lines = self.block_map.achieve(self.current_entity)
            if self.block_map.is_lose():
                raise DeathException
            self.__strategy.update_block_map(self.block_map)
            self.current_entity = self.__new_entity()
            self.__tick_counter.init()

        return drop_lines

    def __drop(self) -> None:
        if self.block_map.check(self.current_entity.peek_drop().blocks):
            self.current_entity.drop()

    def __move_right(self) -> None:
        if self.block_map.check(self.current_entity.peek_right().blocks):
            self.current_entity.move_right()

    def __move_left(self) -> None:
        if self.block_map.check(self.current_entity.peek_left().blocks):
            self.current_entity.move_left()

    def __rotate(self) -> None:
        if self.block_map.check(self.current_entity.peek_rotate().blocks):
            self.current_entity.rotate()

    def __inverse_rotate(self) -> None:
        if self.block_map.check(self.current_entity.peek_inverse_rotate().blocks):
            self.current_entity.inverse_rotate()

    def process_tick(self, status: KeyStatus) -> int:
        tick = self.__tick_counter.count
        self.__tick_counter.incr()

        if status.rotate and tick % self.__config.rotate_sampling_interval == 0:
            self.__rotate()
        elif status.inverse_rotate and tick % self.__config.rotate_sampling_interval == 0:
            self.__inverse_rotate()

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
