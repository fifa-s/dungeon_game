"""nefunguje, jen testuju"""
import pygame as pg
import sys

from networking.server import Server
from networking.client import Client


WIDTH, HEIGHT = SCREEN_SIZE = (800,800)

class Player(pg.sprite.Sprite):
    
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pg.Surface()
        self.image.fill("red")
        self.rect = self.image.get_rect()
        
    def send(self, client):
        client.my_data = self.to_dict()
        
    def update(self, client, events):
        if events[pg.K_W]:
            self.rect.center[0] += 6
        if events[pg.K_S]:
            self.rect.center[0] -= 6
        if events[pg.K_A]:
            self.rect.center[1] -= 6
        if events[pg.K_D]:
            self.rect.center[1] += 6
        self.send(client)
        
    def to_dict(self):
        return {
            "pos": self.rect.center,
        }
    
if __name__ == "__main__":
    PYDEVD_DISABLE_FILE_VALIDATION=1
    server = Server()
    client = Client(id=server.id)

    print(server.id)


    pg.init()

    screen = pg.display.set_mode(SCREEN_SIZE)
    clock = pg.time.Clock()

    my_player = Player()

    while True:
        events = pg.event.get()
        if events[pg.QUIT]:
            sys.exit(0)
        screen.fill('black')
        my_player.update(client, events)
        my_player.draw(screen)
        pg.display.flip()
        clock.tick(60)