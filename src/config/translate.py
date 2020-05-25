from dataclasses import dataclass


@dataclass
class Translate:
    title: str
    esc_description: str
    start_description: str
    restart_description: str
    score: str
    best_score: str
    stage: str
    drop_speed_ratio: str
    death: str
