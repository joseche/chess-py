import pygame

from boards import random_board_theme
from pieces import Pawn


def main(screen):
    board_theme = random_board_theme()
    b = board_theme(screen)
    b.drawBoard()
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.VIDEORESIZE:
                b = board_theme(screen, window_width=event.w, window_height=event.h)
                b.drawBoard()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_p:
                    p = Pawn()
                    p.c_file = 2
                    p.c_rank = 2
                    p.draw(screen, b)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Chess in Python")
    screen = pygame.display.set_mode((640, 640), pygame.RESIZABLE)
    main(screen)
