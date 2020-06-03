from internal import Timer, DeathException
from config.config import Config
from entity_manager import EntityManager
from status import KeyStatus
from render.renderer import Renderer
from render.content import Content, Status
from config.color import Color
import pyxel


class Core:
    __timer: Timer
    __entity_manager: EntityManager
    __renderer: Renderer
    __config: Config
    __level: int
    __score: int
    __best_score: int
    __status: Status
    __key_status: KeyStatus

    def __init__(self, config: Config):
        self.__timer = Timer()
        self.__config = config
        self.__status = Status.START
        self.__level = 0
        self.__score = 0
        self.__best_score = 0
        self.__entity_manager = EntityManager(self.__config)
        self.__renderer = Renderer(self.__config)

    def __update_key_status(self):
        self.__key_status += KeyStatus.get_status()

    def __update(self) -> None:
        self.__update_key_status()
        if self.__status == Status.START and pyxel.btn(pyxel.KEY_S):
            self.__entity_manager.init()
            self.__status = Status.GAMING
        elif pyxel.btn(pyxel.KEY_R):
            self.__level = 0
            self.__score = 0
            self.__status = Status.START
        elif self.__timer.time_pass_ns > self.__config.get_tick_time(
                self.__level) and self.__status == Status.GAMING:
            try:
                lines = self.__entity_manager.process_tick(self.__key_status)
            except DeathException:
                self.__status = Status.DEATH
            else:
                self.__score += lines * self.__config.score_per_line
                self.__best_score = max(self.__score, self.__best_score)
                self.__level = self.__score // self.__config.score_per_level

            self.__key_status = KeyStatus.get_status()

            self.__timer.start()

    def __render(self) -> None:
        self.__renderer.render(Content(
            status=self.__status,
            block_map=self.__entity_manager.block_map,
            entity=self.__entity_manager.current_entity,
            current_score=self.__score,
            best_score=self.__best_score,
            level=self.__level
        ))

    def run(self) -> None:
        pyxel.init(
            width=self.__config.width,
            height=self.__config.height,
            caption=self.__config.translate.title,
            palette=Color.get_palette(),
            quit_key=pyxel.KEY_ESCAPE
        )
        self.__key_status = KeyStatus.get_status()
        self.__timer.start()
        pyxel.run(self.__update, self.__render)
