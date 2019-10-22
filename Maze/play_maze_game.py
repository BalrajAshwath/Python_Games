
import cfg
import pygame
from modules.misc import *
from modules.mazes import *
from modules.Sprites import *


def main(cfg):

	pygame.init()
	pygame.mixer.init()
	pygame.font.init()
	pygame.mixer.music.load(cfg.BGMPATH)
	pygame.mixer.music.play(-1, 0.0)
	screen = pygame.display.set_mode(cfg.SCREENSIZE)
	pygame.display.set_caption('Maze Game')
	font = pygame.font.SysFont('Consolas', 15)
	Interface(screen, cfg, 'game_start')
	num_levels = 0
	best_scores = 'None'

	while True:
		num_levels += 1
		clock = pygame.time.Clock()
		screen = pygame.display.set_mode(cfg.SCREENSIZE)

		maze_now = RandomMaze(cfg.MAZESIZE, cfg.BLOCKSIZE, cfg.BORDERSIZE)

		hero_now = Hero(cfg.HEROPICPATH, [0, 0], cfg.BLOCKSIZE, cfg.BORDERSIZE)

		num_steps = 0

		while True:
			dt = clock.tick(cfg.FPS)
			screen.fill((255, 255, 255))
			is_move = False

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit(-1)
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						is_move = hero_now.move('up', maze_now)
					elif event.key == pygame.K_DOWN:
						is_move = hero_now.move('down', maze_now)
					elif event.key == pygame.K_LEFT:
						is_move = hero_now.move('left', maze_now)
					elif event.key == pygame.K_RIGHT:
						is_move = hero_now.move('right', maze_now)
			num_steps += int(is_move)
			hero_now.draw(screen)
			maze_now.draw(screen)

			showText(screen, font, 'LEVELDONE: %d' % num_levels, (255, 0, 0), (10, 10))
			showText(screen, font, 'BESTSCORE: %s' % best_scores, (255, 0, 0), (210, 10))
			showText(screen, font, 'USEDSTEPS: %s' % num_steps, (255, 0, 0), (410, 10))
			showText(screen, font, 'S: your starting point    D: your destination', (255, 0, 0), (10, 600))

			if (hero_now.coordinate[0] == cfg.MAZESIZE[1] - 1) and (hero_now.coordinate[1] == cfg.MAZESIZE[0] - 1):
				break
			pygame.display.update()

		if best_scores == 'None':
			best_scores = num_steps
		else:
			if best_scores > num_steps:
				best_scores = num_steps

		Interface(screen, cfg, mode='game_switch')


if __name__ == '__main__':
	main(cfg)