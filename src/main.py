import pygame, sys
import settings
from level import Level


class Game:

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
		pygame.display.set_caption(settings.SCREEN_TITLE)
		self.clock = pygame.time.Clock()
		self.level = Level()
	
	def __check_events(self) -> None:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

	def run(self):
		while True:
			self.__check_events()
			dt = self.clock.tick() / 1000
			self.level.run(dt)
			pygame.display.update()


if __name__ == '__main__':
	game = Game()
	game.run()
