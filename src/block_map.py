from .internal import Size, Blocks
from .tetriminos.tetrimino import Tetrimino


class BlockMap:
    __size: Size

    def __init__(self, size: Size) -> None:
        self.__size = Size

    def check(self, blocks: Blocks) -> bool:
        return False

    def can_drop(self, blocks: Blocks) -> bool:
        return False

    def achieve(self, blocks: Tetrimino) -> None:
        ...
