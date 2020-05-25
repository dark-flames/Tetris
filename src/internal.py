from typing import List, Tuple, TypeVar

Size = Tuple[int, int]

Position = Tuple[int, int]
Blocks = List[Position]
Self = TypeVar("Self")


class Counter:
    count: int

    def __init__(self):
        self.init()

    def init(self):
        self.count = 0

    def incr(self):
        self.count += 1
