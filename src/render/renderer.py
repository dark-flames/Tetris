from .content import Content, Status
from ..config.config import Config
from ..config.color import Color
from ..internal import Position
from typing import List
import pyxel


class Renderer:
    __config: Config

    def __init__(self, config: Config) -> None:
        self.__config = config

    def __clear(self) -> None:
        pyxel.cls(self.__config.background_color)

    def __center_texts(self, texts: List[str]) -> None:
        offset = self.__config.center_text_offset_y + self.__config.window_padding
        for (index, text) in enumerate(texts):
            text_width = len(text) * pyxel.FONT_WIDTH
            x = (self.__config.width - text_width) // 2
            y = (pyxel.FONT_HEIGHT + self.__config.center_text_margin_y) * index + offset
            pyxel.text(x, y, text, self.__config.text_color)

    def __render_start(self) -> None:
        self.__clear()
        self.__center_texts([
            self.__config.translate.title,
            self.__config.translate.start_description,
            self.__config.translate.esc_description
        ])

    def __render_death(self, content: Content) -> None:
        self.__clear()
        self.__center_texts([
            self.__config.translate.death,
            "{0}: {1}".format(self.__config.translate.score, content.current_score),
            "{0}: {1}".format(self.__config.translate.best_score, content.best_score),
            "{0}: {1}".format(self.__config.translate.stage, content.stage),
            self.__config.translate.restart_description,
            self.__config.translate.esc_description
        ])

    def __render_info(self, texts: List[str]):
        length = 0
        for (index, text) in enumerate(texts):
            x = self.__config.window_padding + length
            y = self.__config.window_padding
            pyxel.text(x, y, text, self.__config.text_color)
            length += len(text) * pyxel.FONT_WIDTH + self.__config.info_text_margin_x

    def coordinate_transform(self, position: Position):
        return Position(
            position.x * self.__config.pixel_per_block + self.__config.window_padding,
            self.__config.game_offset_y + (self.__config.size[1] - position.y - 1) * self.__config.pixel_per_block
        )

    def __render_block(self, position: Position, color: Color):
        pyxel.rect(
            x=position.x + self.__config.block_padding,
            y=position.y + self.__config.block_padding,
            w=self.__config.pixel_per_block - self.__config.block_padding * 2,
            h=self.__config.pixel_per_block - self.__config.block_padding * 2,
            col=color
        )

    def __render_gaming(self, content: Content) -> None:
        self.__clear()
        self.__render_info([
            "{0}: {1}".format(self.__config.translate.score, content.current_score),
            "{0}: {1}".format(self.__config.translate.best_score, content.best_score),
            "{0}: {1}".format(
                self.__config.translate.drop_speed_ratio,
                round(self.__config.get_speed_ratio(content.stage), 1)
            ),
        ])

        for (position, color) in content.block_map:
            transformed_position = self.coordinate_transform(position)
            self.__render_block(transformed_position, color)

    def render(self, content: Content) -> None:
        if content.status == Status.START:
            self.__render_start()
        elif content.status == Status.GAMING:
            self.__render_gaming(content)
        elif content.status == Status.DEATH:
            self.__render_death(content)
