from dataclasses import dataclass
from enum import Enum, auto

from block_map import BlockMap
from entities.entity import Entity


class Status(Enum):
    START = auto()
    GAMING = auto()
    DEATH = auto()


@dataclass
class Content:
    status: Status
    block_map: BlockMap
    entity: Entity
    current_score: int
    best_score: int
    level: int
