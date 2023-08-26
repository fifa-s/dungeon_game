import pygame as pg
from sys import exit
import ctypes
from constants import SYSTEM

if SYSTEM == "Windows":
	import ctypes
elif SYSTEM == "Linux":
	import subprocess

class Screen:

	def __init__(self, screen_size, display_size):
		pg.init()

		flags = pg.RESIZABLE | pg.HWSURFACE | pg.DOUBLEBUF
		self.display = pg.display.set_mode(display_size, flags=flags)
		self.maximize()

		self.screen = pg.Surface(screen_size)

		self.clock = pg.time.Clock()

		global delta
		delta = 0

		self.bg_color = (20, 30, 40)
		self.display_color = None
		self.max_fps = 60
		self.running = True

	def maximize(self):
		if SYSTEM == "Windows":
		    ctypes.windll.user32.ShowWindow(pg.display.get_wm_info()['window'], 3)  # 3 = SW_MAXIMIZE

		elif SYSTEM == "Linux":
		    try:
		        subprocess.call(["wmctrl", "-r", "pygame window", "-b", "add,maximized_vert,maximized_horz"])
		    except FileNotFoundError:
		        print("failed to maximize window")  # wmctrl not available

	def events(self):
		# overwrite in inheritance
		self.running = not any(i.type == pg.QUIT for i in self.event_list)

	def update(self):
		"""This function should be called from the end of the main loop"""
		self.flip()
		global delta
		delta = self.clock.tick(self.max_fps)
		self.screen.fill(self.bg_color)
		self.event_list = pg.event.get()
		self.events()

	def flip(self):
		if self.display_color != None:
			self.display.fill(self.display_color)
		sw, sh = self.screen.get_size()
		dw, dh = self.display.get_size()
		screen_ar = sw / sh
		display_ar = dw / dh
		if screen_ar > display_ar:
			w = dw
			h = dw * (1 / screen_ar)
			x = 0
			y = (dh - h) / 2

		else:
			h = dh
			w = dh * screen_ar
			x = (dw - w) / 2
			y = 0

		transformed_screen = pg.transform.smoothscale(self.screen, (w, h))
		self.display.blit(transformed_screen, (x, y))
		pg.display.flip()

	def quit(self):
		pg.quit()
		exit(0)
