from dataclasses import dataclass

from internal import Size
from strategy.random_strategy import RandomTetrisStrategy
from strategy.strategy import Strategy
from .color import Color
from .translate import Translate, translate_factory
from .difficulty import Difficulty
from pyxel import FONT_HEIGHT
from argparse import ArgumentParser
from copy import deepcopy


@dataclass
class Config:
    dark_mod: bool
    size: Size
    pixel_per_block: int
    block_padding: int
    strategy: Strategy
    rotate_sampling_interval: int  # tick
    left_and_right_sampling_interval: int  # tick
    drop_speed: int  # tick per step
    accelerated_drop_ratio: float  # tick per step
    default_tick_per_second: int  # tps at game start
    tps_level_accelerate_ratio: float
    score_per_line: int
    score_per_level: int
    window_padding_y: int
    window_padding_x: int
    center_text_offset_y: int  # px
    center_text_margin_y: int  # px
    info_text_margin_x: int
    info_text_margin_y: int
    translate: Translate
    difficulty: Difficulty

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
        return self.size[0] * self.pixel_per_block + self.window_padding_x * 2

    @property
    def height(self) -> int:
        return self.size[1] * self.pixel_per_block + self.game_offset_y + self.window_padding_y

    @property
    def game_offset_y(self) -> int:
        return self.info_text_margin_y * 2 + FONT_HEIGHT + self.window_padding_y

    @property
    def accelerated_drop_speed(self) -> int:
        return int(self.drop_speed // self.accelerated_drop_ratio)

    def get_tick_time(self, level: int) -> int:
        return int(1e9 / (self.default_tick_per_second * self.get_speed_ratio(level)))

    def get_speed_ratio(self, level: int) -> float:
        return self.tps_level_accelerate_ratio ** level

    @classmethod
    def default_config(cls):
        return Config(
            dark_mod=False,
            size=Size([15, 20]),
            pixel_per_block=10,
            block_padding=1,
            strategy=RandomTetrisStrategy(),
            rotate_sampling_interval=2,
            left_and_right_sampling_interval=2,
            drop_speed=4,
            accelerated_drop_ratio=4,
            default_tick_per_second=8,
            tps_level_accelerate_ratio=1.1,
            score_per_line=100,
            score_per_level=500,
            window_padding_y=5,
            window_padding_x=5,
            center_text_offset_y=40,
            center_text_margin_y=2,
            info_text_margin_x=3,
            info_text_margin_y=1,
            translate=translate_factory('en'),
            difficulty=Difficulty.NORMAL
        )

    @classmethod
    def from_args(cls, parser: ArgumentParser):
        default_config: Config = deepcopy(cls.default_config())
        parser.add_argument("--dark-mode", help="run game in dark mode", action="store_true")
        parser.add_argument("--size", help="[width][height] game size, default 15 * 20", action="extend", type=int, nargs="+")
        parser.add_argument("--lang", help="language, default 'en'", type=str, default="en")
        parser.add_argument("--difficulty", help="'easy', 'hard', 'very_easy', 'very_hard','invisible','ex', "
                                                 "or 'normal'", type=str, default='very_hard')

        args = parser.parse_args()
        default_config.dark_mod = args.dark_mode
        if args.size and len(args.size) == 2:
            default_config.size = Size(args.size)
        default_config.translate = translate_factory(args.lang)
        default_config.difficulty = Difficulty.get_difficulty(args.difficulty)

        return default_config
