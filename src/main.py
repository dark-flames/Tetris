from .internal import Timer, DeathException
from .config.config import Config
from .tetrimino_manager import TetriminoManager
from .status import KeyStatus
from .render.renderer import Renderer
from .render.content import Content, Status
from .config.color import Color

import pyxel


class Core:
    __timer: Timer
    __tetrimino_manager: TetriminoManager
    __renderer: Renderer
    __config: Config
    __stage: int
    __score: int
    __best_score: int
    __status: Status

    def __init__(self, config: Config):
        self.__timer = Timer()
        self.__config = config
        self.__stage = 0
        self.__score = 0
        self.__best_score = 0
        self.__tetrimino_manager = TetriminoManager(self.__config)
        self.__renderer = Renderer(self.__config)

    def __update(self) -> None:
        if self.__status == Status.START and pyxel.btn(pyxel.KEY_S):
            self.__tetrimino_manager.init()
            self.__status = Status.GAMING
        elif pyxel.btn(pyxel.KEY_R):
            self.__status = Status.START
        elif self.__timer.time_pass_ns > self.__config.get_tick_time(
                self.__stage) and self.__status == Status.GAMING:
            try:
                lines = self.__tetrimino_manager.process_tick(KeyStatus.get_status())
            except DeathException:
                self.__status = Status.DEATH
            else:
                self.__score += lines * self.__config.score_per_line
                self.__best_score = max(self.__score, self.__best_score)
                self.__stage = self.__score // self.__config.score_per_stage

            self.__timer.start()

    def __render(self) -> None:
        self.__renderer.render(Content(
            status=self.__status,
            block_map=self.__tetrimino_manager.block_map,
            current_score=self.__score,
            best_score=self.__best_score,
            stage=self.__stage
        ))

    def run(self) -> None:
        pyxel.init(
            width=self.__config.width,
            height=self.__config.height,
            caption=self.__config.caption,
            palette=Color.get_palette(),
            quit_key=pyxel.KEY_ESCAPE
        )

        pyxel.run(self.__update, self.__render)
