from dataclasses import dataclass


@dataclass
class Translate:
    title: str
    esc_description: str
    start_description: str
    restart_description: str
    score: str
    best_score: str
    level: str
    drop_speed_ratio: str
    death: str


def translate_factory(lang: str) -> Translate:
    if lang == "en":
        return Translate(
            title="Tetris",
            esc_description="Press [Esc] to quite",
            start_description="Press [s] to start game",
            restart_description="Press [r] to restart game",
            score="Score",
            best_score="Best Score",
            level="Level",
            drop_speed_ratio="Speed",
            death="Game over"
        )
