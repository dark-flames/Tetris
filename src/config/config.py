from dataclasses import dataclass

from ..internal import Size
from ..strategy.strategy import Strategy


@dataclass
class Config:
    size: Size
    strategy: Strategy
    drop_speed: int
    accelerated_drop_speed: int
