import pygame
from tetris import Tetris
from scoreboard import ScoreBoard
from renderer import Renderer
from event_queue import EventQueue
from clock import Clock
from game_loop import GameLoop


TILE_SIZE = 55


def main():
    '''Initialize game variables & game related objects. Start game.'''
    
    width = 10
    height = 20
    game_screen_width = TILE_SIZE * width
    game_screen_heigth = TILE_SIZE * height
    game_screen = pygame.Surface((game_screen_width, game_screen_heigth))
    
    display_width = game_screen_width + 500
    display_height = game_screen_heigth + 80
    display = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("Tetris")

    grid = [pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
            for x in range(width) for y in range(height)]

    game = Tetris(height, width)
    scoreboard = ScoreBoard()
    renderer = Renderer(game_screen, display, grid, game, scoreboard, TILE_SIZE)
    event_queue = EventQueue()
    clock = Clock()
    game_loop = GameLoop(game, scoreboard, renderer, event_queue, clock, TILE_SIZE)

    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
