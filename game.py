import pygame as pg

from screen import Screen
from constants import SCREEN_SIZE, DISPLAY_SIZE


class Game(Screen):
    
    def __init__(self):
        super().__init__(
            SCREEN_SIZE,
            DISPLAY_SIZE
        )

    def menuLoop(self, menu):
        while self.running:
            pg.draw.circle(self.screen, "red", (SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2), 100)
            pg.display.set_caption(f"FPS: {self.clock.get_fps():.1f}")
            self.update()
            
    def gameLoop(self):
        ...
        
    def run(self):
        self.menuLoop(None) # TODO: add a class Menu that would hold all information about the menu