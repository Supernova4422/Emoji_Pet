import sys
from Scene_Main import Scene_Main
import cProfile


def run():
    main = Scene_Main()
    main.loop()


if __name__ == '__main__':
    run()
