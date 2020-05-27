from config.config import Config
import argparse
from core import Core


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Tetris'
    )

    config: Config = Config.from_args(parser)

    core = Core(config)

    core.run()
