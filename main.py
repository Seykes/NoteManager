from src.utils.loader import start, close
from src import handlers

from asyncio import run


if __name__ == "__main__":
    start()

    manager = handlers.NotesManager()
    while True:
        try:
            run(manager())
        except (KeyboardInterrupt):
            print("\033c", end='')
            break
        except (KeyError):
            continue

    print("Thanks for using my work")
    