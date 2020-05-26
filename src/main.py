from internal import Size
from config.config import Config
from config.translate import translate_factory
from strategy.random_strategy import RandomStrategy
from core import Core


if __name__ == "__main__":
    core = Core(
        Config(
            dark_mod=True,
            size=Size([15, 20]),
            pixel_per_block=10,
            block_padding=1,
            strategy=RandomStrategy(),
            rotate_sampling_interval=2,
            left_and_right_sampling_interval=1,
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
            translate=translate_factory('en')
        )
    )

    core.run()
