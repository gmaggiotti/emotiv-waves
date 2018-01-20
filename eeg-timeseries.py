import pygame
from pygame import *


screen_with = 1680
screen_height = 1000

def event_handler():
    for event in pygame.event.get():
        if event.type == 12:
            return True
    return False


def main():
    quit = False
    pygame.init()
    fpsClock= pygame.time.Clock()

    screen = pygame.display.set_mode((screen_with,screen_height))
    pygame.display.set_caption("Mindwave Viewer")

    while quit is False:
        quit = event_handler()
        pygame.display.update()
        fpsClock.tick(7)


if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()