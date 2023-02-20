from collections.abc import Callable
from typing import Union
from .object import *

def process(display=ItemEnum.EMERALD):
    """
    Defines a process, or a thread, in DiamondFire.

    Parameters:
        func - The body for the process
        display - The display item for the process when you use the `Start Process` block = ItemEnum.EMERALD

    Examples:
        ```py
        @process
        def longProcess():
            print("Before waiting")
            wait(1)
            print("After waiting")
        ```
        ```py
        @process(STONE)
        def proc():
            ...
        ```
    """
    def decor(func: Callable):
        print(f"Initiated Process {func.__name__}{f' with display {display}' if display else ''}")
        return func
    return decor

def function(display=ItemEnum.LAPIS_LAZULI):
    """
    Defines a function, although this is unnecessary.

    Parameters:
        func - The body for the function
        display - The display item for the function in the `Call Function` block = ItemEnum.LAPIS_LAZULI

    Examples:
        ```py
        @function
        def func1():
            i = 0
        ```
    """
    def decor(func: Callable):
        print(f"Initiated Function {func.__name__}{f' with display {display}' if display else ''} through decorator")
        return func
    return decor

def playerEvent(event=PlayerEvent.JOIN):
    """
    Creates a new Player Event that executes when a player does something.

    Parameters:
        func - The body of the event
        event - The trigger for the event

    Examples:
        ```py
        @playerEvent(P_EV_CMD)
        def _():
            ...
        ```
        ```py
        @playerEvent(P_EV_RESPAWN)
        def playerRespawns():
            print("some people found " + default + "'s reboot card")
        ```
    """
    def decor(func: Callable):
        print(f"Initiated PlayerEvent triggered by {event}{f' with name {func.__name__}' if not func.__name__ == '_' else ''}")
        return func
    return decor

def entityEvent(event=EntityEvent.DAMAGE_ENTITY):
    """
    Creates a new Entity Event that executes when an entity does something.

    Parameters:
        func - The body of the event
        event - The trigger for the event

    Examples:
        ```py
        @entityEvent(E_EV_DAMAGE_ENTITY)
        def _():
            ...
        ```
        ```py
        @entityEvent(E_EV_DEATH)
        def entityDies():
            print(killer + " killed his dog - " + victim)
        ```
    """
    def decor(func: Callable):
        print(f"Initiated EntityEvent triggered by {event}{f' with name {func.__name__}' if not func.__name__ == '_' else ''}")
        return func
    return decor

class Player:
    """
    Does not need to be initialized
    """
    def __init__(self):
        """
        Initialize will break the program lol
        """

    @staticmethod
    def give_items(items: Item | list[Item]):
        """
        Gives the player items

        Parameters:
            items - Either a singular or plural. The items will be given either way
        """

    @staticmethod
    def set_hotbar(items: list[Item]):
        """
        Sets the player's hotbar

        Parameters:
            items - A list of items to set
        """
