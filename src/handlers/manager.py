"""
Main file for managing note actions and corresponding data validation
At the moment, class 1 is presented here with the prospect of further updating


Classes:
    NotesManager
"""


from typing import Any, Union
from colorama import Fore

from tortoise.models import Q
from tortoise import queryset
from src.db.db_models import Note
from src.utils.wrappers import with_str


class NotesManager:
    """
    Class for managing all available note actions and corresponding data validation

    Functions:
        find
        create
        get
        get_all
        delete

    Misc Functions:
        _emblem
        _stringify_commands
        _filter
        _get
        _get_all
        _create
        _delete
    """

    def __init__(self) -> None:
        self.commands: dict = {
            0: self.close,
            1: self.find,
            2: self.get,
            3: self.get_all,
            4: self.delete,
            5: self.create,
        }


    def _stringify_commands(self):
        """
        Stringify commands list

        Returns:
            None
        """
        message = ""
        for key,value in self.commands.items():
            message += f"{Fore.GREEN}{key}{Fore.RESET}. \
                {Fore.LIGHTBLUE_EX}{str(value)}{Fore.RESET}\n"

        print(message)
    
    def _emblem(self) -> None:
        """
        Clear terminal and put emblem

        Returns:
            None
        """

        print("\033c", end='')
        print(f"""
{Fore.GREEN}01010011 01100101 01111001 01101011 01100101\n
:'######::'########:'##:::'##:'##:::'##:'########:
'##... ##: ##.....::. ##:'##:: ##::'##:: ##.....::
##:::..:: ##::::::::. ####::: ##:'##::: ##:::::::
. ######:: ######:::::. ##:::: #####:::: ######:::
:..... ##: ##...::::::: ##:::: ##. ##::: ##...::::
'##::: ##: ##:::::::::: ##:::: ##:. ##:: ##:::::::
. ######:: ########:::: ##:::: ##::. ##: ########:
:......:::........:::::..:::::..::::..::........::
    {Fore.RESET}\n\n
{Fore.BLUE}Notes Manager{Fore.RESET}\n
""")


    async def __call__(self, *args: Any, **kwrgs: Any) -> None:
        """
        Replace native __call__ function for input wait

        Returns:
            None
        """
        self._emblem()
        self._stringify_commands()

        value = input(f"\n{Fore.CYAN}[#] {Fore.LIGHTRED_EX}")
        if value.isdigit():
            await self.commands[int(value)](self)

    async def _filter(self, *args, **kwargs) -> Union[None,queryset.QuerySet[Note]]:
        """
        Search in base Note class for coincidences with filters
        
        Parameters:
            *args
            **kwargs

        Returns:
            None
            QuerySet[Note] - iterable, list analog expression for all suitable notes
        """
        return await Note.filter(*args,**kwargs).all()


    async def _find(self, *args, **kwargs) -> Union[None,list[Note]]:
        """
        Subsidiary function for search by word function

        Parameters:
            *args
            **kwargs

        Returns:
            None
            list[Note] - list of all suitable notes
        """
        return await self._filter(*args, **kwargs)


    async def _get(self, *args, **kwargs) -> Note:
        """
        Subsidiary function for get by id function

        Parameters:
            *args
            **kwargs

        Returns:
            None
            Note - db model of note
        """
        all_notes = await self._filter(*args, **kwargs)
        return all_notes[0]

    async def _get_all(self) -> list[Note]:
        """
        Get all notes in database

        Parameters:

        Returns:
            None
            list[Note] - list of all suitable notes
        """
        return await Note.all()

    async def _delete(self, *args, **kwargs) -> None:
        """
        Delete needed note from database

        Parameters:
            *args
            **kwargs

        Returns:
            None
        """
        
        all_notes = await self._filter(*args, **kwargs)
        return await all_notes[0].delete()
    
    async def _create(self, **kwargs) -> Note:
        return await Note.create(**kwargs)
    
    @with_str("CLose application")
    async def close(self) -> None:
        raise KeyboardInterrupt

    @with_str("Create new note")
    async def create(self) -> None:
        self._emblem()

        title = input(f"{Fore.BLUE}Note title:{Fore.RESET} {Fore.LIGHTRED_EX}")
        text = input(f"{Fore.BLUE}Note text:{Fore.RESET} {Fore.LIGHTRED_EX}")

        await self._create(title=title, text=text)

    @with_str("Get all notes")
    async def get_all(self) -> None:
        self._emblem()

        notes = await self._get_all()

        for note in notes:
            print(f"{Fore.GREEN}{note.id}.{Fore.RESET} {Fore.LIGHTBLUE_EX}{note.title}{Fore.RESET}")
        print(f"\n{Fore.GREEN}0.{Fore.RESET} {Fore.LIGHTBLUE_EX}Back to menu{Fore.RESET}")

        key = input(f"\n{Fore.CYAN}[#] {Fore.LIGHTRED_EX}")
        if not key.isdigit() or key == "0":
            return self()


        self._emblem()

        note = await self._get(id=int(key))
        print(f"{Fore.GREEN}{note.title}.{Fore.RESET}\n{Fore.LIGHTBLUE_EX}{note.text}{Fore.RESET}\n")
        print(f"\n{Fore.GREEN}0.{Fore.RESET} {Fore.LIGHTBLUE_EX}Back to menu{Fore.RESET}")

        key = input(f"\n{Fore.CYAN}[#] {Fore.LIGHTRED_EX}")


    @with_str("Find note by keyword")
    async def find(self) -> None:
        self._emblem()

        keyword = input(f"{Fore.BLUE}Note title, keyword or id: {Fore.LIGHTRED_EX}")
        
        notes = await self._find(Q(title__contains=keyword) | Q(text__contains=keyword))
        
        for note in notes:
            print(f"{Fore.GREEN}{note.id}.{Fore.RESET} {Fore.LIGHTBLUE_EX}{note.title}{Fore.RESET}\n")
        print(f"\n{Fore.GREEN}0.{Fore.RESET} {Fore.LIGHTBLUE_EX}Back to menu{Fore.RESET}")

        key = input(f"\n{Fore.CYAN}[#] {Fore.LIGHTRED_EX}")
        if not key.isdigit() or key == "0":
            return self()


        self._emblem()

        note = await self._get(id=int(key))
        print(f"{Fore.GREEN}{note.title}.{Fore.RESET}\n{Fore.LIGHTBLUE_EX}{note.text}{Fore.RESET}\n")
        print(f"\n{Fore.GREEN}0.{Fore.RESET} {Fore.LIGHTBLUE_EX}Back to menu{Fore.RESET}")

        key = input(f"\n{Fore.CYAN}[#] {Fore.LIGHTRED_EX}")


    @with_str("Get note by ID")
    async def get(self) -> None:
        self._emblem()

        keyword = input(f"{Fore.BLUE}Note id: {Fore.LIGHTRED_EX}")
        if not keyword.isdigit():
            return

        self._emblem()
        note = await self._get(id=int(keyword))
        print(f"{Fore.GREEN}{note.title}.{Fore.RESET}\n{Fore.LIGHTBLUE_EX}{note.text}{Fore.RESET}\n")
        print(f"\n{Fore.GREEN}0.{Fore.RESET} {Fore.LIGHTBLUE_EX}Back to menu{Fore.RESET}")

        key = input(f"\n{Fore.CYAN}[#] {Fore.LIGHTRED_EX}")


    @with_str("Delete Note")
    async def delete(self) -> None:
        self._emblem()

        keyword = input(f"{Fore.BLUE}Note id: {Fore.LIGHTRED_EX}")
        if not keyword.isdigit():
            return
        
        await self._delete(id=int(keyword))
        