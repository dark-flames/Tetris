from dataclasses import dataclass
from enum import Enum, auto

from ..block_map import BlockMap


class Status(Enum):
    START = auto()
    GAMING = auto()
    DEATH = auto()


@dataclass
class Content:
    status: Status
    block_map: BlockMap
    current_score: int
    best_score: int
    stage: int
