import pygame as pg


class Screen:

    def __init__(self, screen_size, display_size):
        pg.init()

        self.display = pg.display.set_mode(
            display_size,
            flags=pg.RESIZABLE | pg.FULLSCREEN
        )
        self.screen = pg.Surface(screen_size)

        self.clock = pg.time.Clock()
        
        global delta
        delta = 0

        self.bg_color = (20,30,40)
        self.display_color = None
        self.max_fps = 20

        self.load()
        self.mainLoop()

    def events(self):
        # overwrite in inheritance
        self.running = (True not in [True for i in self.event_list if i.type == pg.QUIT])

    def load(self):
        pass # overwrite in inheritance

    def tick(self):
        pass # overwrite in inheritance

    def mainLoop(self):
        self.running = True
        while self.running:
            self.screen.fill(
                self.bg_color
            )
            self.event_list = pg.event.get()
            self.events()
            self.tick()
            self.flip()
            global delta
            delta = self.clock.tick(
                self.max_fps
            )
        self.quit()

    def flip(self):
        if self.display_color != None:
            self.display.fill(
            self.display_color
            )
        sw,sh = self.screen.get_size()
        dw,dh = self.display.get_size()
        screen_ar = sw / sh
        display_ar = dw / dh
        if screen_ar > display_ar:
            w = dw
            h = dw*(1/screen_ar)
            x = 0
            y = (dh - h) / 2
            
        else:
            h = dh
            w = dh*screen_ar
            x = (dw - w) / 2
            y = 0
            
        transformed = pg.transform.smoothscale(
            self.screen,
            (w, h)
        )
        self.display.blit(
            transformed,
            (x,y)
        )
        pg.display.flip()

    def quit(self):
        pg.quit()





