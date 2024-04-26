"""
Entrypoint for chess
"""

import os
import sys

import pygame
from boards import random_board_theme
from pieces import Pawn

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"


def main(screen):
    board_theme = random_board_theme()
    b = board_theme(screen)
    b.flipped = True
    b.draw_board()
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                b.adjust_size(event.w, event.h)
                b.draw_board()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
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
    scr = pygame.display.set_mode((640, 640), pygame.RESIZABLE)
    main(scr)
