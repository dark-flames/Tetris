from dataclasses import dataclass

from ..internal import Size
from ..strategy.strategy import Strategy
from .color import Color
from .translate import Translate
from pyxel import FONT_HEIGHT


@dataclass
class Config:
    dark_mod: bool
    size: Size
    pixel_per_block: int
    block_padding: int
    strategy: Strategy
    caption: str
    drop_speed: int  # tick per step
    accelerated_drop_ratio: float  # tick per step
    default_tick_per_second: int  # tps at game start
    tps_stage_accelerate_ratio: float
    score_per_line: int
    score_per_stage: int
    window_padding: int
    center_text_offset_y: int  # px
    center_text_margin_y: int  # px
    info_text_margin_x: int
    info_text_margin_y: int
    translate: Translate

    @property
    def background_color(self):
        if self.dark_mod:
            return Color.DARK
        else:
            return Color.LIGHT

    @property
    def text_color(self):
        if self.dark_mod:
            return Color.LIGHT
        else:
            return Color.DARK

    @property
    def width(self) -> int:
        return self.size[0] * self.pixel_per_block + self.window_padding * 2

    @property
    def height(self) -> int:
        return self.size[0] * self.pixel_per_block + self.game_offset_y + self.window_padding

    @property
    def game_offset_y(self) -> int:
        return self.info_text_margin_y * 2 + FONT_HEIGHT + self.window_padding

    @property
    def accelerated_drop_speed(self) -> int:
        return int(self.drop_speed * self.accelerated_drop_ratio)

    def get_tick_time(self, stage: int) -> int:
        return int(1e9 / self.default_tick_per_second * self.get_speed_ratio(stage))

    def get_speed_ratio(self, stage: int) -> float:
        return self.tps_stage_accelerate_ratio ** stage
