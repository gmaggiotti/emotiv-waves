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

signals = ['F3', 'FC5', 'AF3', 'F7', 'T7', 'P7', 'O1', 'O2', 'P8', 'T8', 'F8', 'AF4', 'FC6', 'F4']
def render_text( screen ):
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    for x in range(0, len(signals)):
        textsurface = myfont.render(signals[x], False, (255, 255, 255))
        l = (x/14.0)*screen_height
        screen.blit(textsurface,(5,l+20))

def main():
    quit = False
    e = EPOC()

    pygame.init()
    fpsClock= pygame.time.Clock()

    screen = pygame.display.set_mode((screen_with,screen_height))
    pygame.display.set_caption("Emotiv Viewer")
    render_text(screen)

    i = 50
    hop = 1
    v = lv = 0
    while quit is False:
        quit = event_handler()

        data = e.get_sample()
        if data:
            for i1,channel in enumerate(e.channel_mask):
                print "%10s: %.5f %.5f %20s: %.2f" % (channel, data[i1], data[i1]*100/5000 , "Quality", e.quality[channel])
                v = data[i1]*75/5000.0 - 50
                l = (i1/14.0)*screen_height
                pygame.draw.line(screen, red, [i, l - lv], [i+hop,l - v], 1)
            print "----"

        lv = v
        i += hop
        pygame.display.update()
        fpsClock.tick(fps)

        if i == screen_with:
            screen.fill((0,0,0))
            i=50
            render_text(screen)


if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()