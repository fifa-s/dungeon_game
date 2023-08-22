import pygame as pg

from screen import Screen
from constants import SCREEN_SIZE, DISPLAY_SIZE


class Game(Screen):
    
    def __init__(self):
        super().__init__(
            SCREEN_SIZE,
            DISPLAY_SIZE
        )
        
    def tick(self):
        pg.draw.circle(self.screen, "red", (SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2), 100)