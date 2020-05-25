from dataclasses import dataclass

from ..internal import Size
from ..strategy import StrategyType


@dataclass
class Config:
    size: Size
    strategy: StrategyType
    drop_speed: int
    accelerated_drop_speed: int
