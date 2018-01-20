import pygame
from pygame import *


screen_with = 1680
screen_height = 1000
fps = 1000

def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT:
            return True
    return False


def main():
    quit = False
    red = pygame.Color(255,0,0)

    pygame.init()
    fpsClock= pygame.time.Clock()

    screen = pygame.display.set_mode((screen_with,screen_height))
    pygame.display.set_caption("Mindwave Viewer")

    i = 0
    hop = 1
    while quit is False:
        quit = event_handler()

        pygame.draw.line(screen, red, [i, 500], [i+hop,500], 1)
        i += hop
        pygame.display.update()
        fpsClock.tick(fps)

        if i == screen_with:
            screen.fill((0,0,0))
            i=0


if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()