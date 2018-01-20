import pygame
from pygame import *
from emotiv.epoc import EPOC


screen_with = 1680
screen_height = 1000
fps = 1000
red = pygame.Color(255,0,0)

def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT:
            return True
    return False


def render_text( screen ):
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('F3', False, (255, 255, 255))
    screen.blit(textsurface,(0,480))

def main():
    quit = False
    e = EPOC()

    pygame.init()
    fpsClock= pygame.time.Clock()

    screen = pygame.display.set_mode((screen_with,screen_height))
    pygame.display.set_caption("Emotiv Viewer")
    render_text(screen)

    i = 40
    hop = 2
    new_val = prev_val = 0
    while quit is False:
        quit = event_handler()

        data = e.get_sample()
        if data:
            for i1,channel in enumerate(e.channel_mask):
                if channel == "F3":
                    print "%10s: %.2f %20s: %.2f" % (channel, data[i1]*100/5000 , "Quality", e.quality[channel])
                    new_val = data[i1]*100/5000 - 50

        pygame.draw.line(screen, red, [i, 500 + prev_val], [i+hop,500 + new_val], 1)
        prev_val = new_val
        i += hop
        pygame.display.update()
        fpsClock.tick(fps)

        if i == screen_with:
            screen.fill((0,0,0))
            i=40
            render_text(screen)


if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()