import pygame as pg

from screen import Screen
from constants import SCREEN_SIZE, DISPLAY_SIZE


class Game(Screen):
    
    def __init__(self) -> None:
        super().__init__(
            SCREEN_SIZE,
            DISPLAY_SIZE
        )
        
    def run(self) -> None:
        ...