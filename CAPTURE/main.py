import pygame
pygame.init()

WIDTH, HEIGHT = 640, 480
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('First Game!')

def main():
    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.quit:
                run=False

        pygame.quit()

if __name__  == '__main__':

    main()