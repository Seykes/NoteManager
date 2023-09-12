"""
01010011 01100101 01111001 01101011 01100101\n
:'######::'########:'##:::'##:'##:::'##:'########:
'##... ##: ##.....::. ##:'##:: ##::'##:: ##.....::
##:::..:: ##::::::::. ####::: ##:'##::: ##:::::::
. ######:: ######:::::. ##:::: #####:::: ######:::
:..... ##: ##...::::::: ##:::: ##. ##::: ##...::::
'##::: ##: ##:::::::::: ##:::: ##:. ##:: ##:::::::
. ######:: ########:::: ##:::: ##::. ##: ########:
:......:::........:::::..:::::..::::..::........::


12.09.2023
Telegram: @SeykeHG
"""
from asyncio import run

from src.utils.loader import start
from src import handlers


if __name__ == "__main__":
    start()

    manager = handlers.NotesManager()
    while True:
        try:
            run(manager())
        except KeyboardInterrupt:
            print("\033c", end='')
            break
        except KeyError:
            continue

    print("Thanks for using my work")
    