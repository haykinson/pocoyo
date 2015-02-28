import pygame
import sys
import time

from square import Square
from square_floor import SquareFloor
from color import Color
from color_sequencer import ColorSequencer
from corner_sequencer import CornerSequencer

pygame.init()

size = width, height = (pygame.display.Info().current_w, pygame.display.Info().current_h)
black = 0, 0, 0
speed = [2,2]

screen = pygame.display.set_mode(size)

#ball = pygame.image.load("ball.bmp")
#ballrect = ball.get_rect()


corner_sequencer = CornerSequencer([Color.red, Color.green, Color.blue, Color.purple, Color.orange])

#color_cycle = ColorCycle()
floor = SquareFloor()

sequencer = ColorSequencer([Color.orange,
                            Color.yellow, 
                            Color.blue, 
                            Color.green, 
                            Color.red], 5, 24)



while True:
    for event in pygame.event.get():
        if event.type in [pygame.QUIT, pygame.KEYDOWN]:
            sys.exit()
    
    screen.fill(black)

    #floor.update_color_sequence(floor.spiral_order(), sequencer)

    floor.update_color_sequence(floor.corner_order(), corner_sequencer)

    for square in floor.natural_order():
        loc = square.pos()
        size = square.size()
        rect = (loc,size)
        color = square.color()
        pygame.draw.rect(screen, color, rect)

    pygame.display.flip()

    pygame.time.delay(300)

