import logging
from random import randint, randrange, uniform

import pygame
from pygame import Surface

from chess_py.media_manager import MediaManager

logger = logging.getLogger(__name__)
NOISE_PCT: float = uniform(0.05, 0.2)


class DefaultBoard:
    WINDOW_BACKGROUND = (0xBD, 0xC7, 0xDD)

    def __init__(
            self,
            screen: Surface,
            border_color: tuple = (141, 171, 181),
            board_color_white: tuple = (236, 244, 214),
            board_color_black: tuple = (45, 149, 150),
    ):
        logger.debug("initializing %s", self)
        self.screen = screen
        self.border_color = border_color
        self.board_color_white = board_color_white
        self.board_color_black = board_color_black
        self.flipped = False
        self.cell_coords = True
        self.media = MediaManager()
        self.adjust_size(window_width=screen.get_width(),
                         window_height=screen.get_height())

    def adjust_size(self, window_width: int, window_height: int):
        logger.debug("adjusting size of board: %s", self)
        self.window_width = window_width
        self.window_height = window_height
        self.cell_length = min(window_width, window_height) / 9
        self.letter_x_align = self.cell_length / 16
        self.letter_y_align = (self.cell_length / 4) * 3
        self.number_x_align = (self.cell_length / 8) * 7
        self.number_y_align = self.cell_length / 32
        self.board_font = pygame.font.SysFont("Comic Sans MS",
                                              int(self.cell_length / 6),
                                              bold=True)
        self.media.resize_images(self.cell_length)

    def cell_pos_x(self, col: int = 1) -> int:
        return int((col - 1) * self.cell_length + (0.5 * self.cell_length))

    def cell_pos_y(self, row: int = 1) -> int:
        return int((row - 1) * self.cell_length + (0.5 * self.cell_length))

    def _noise_color(self) -> tuple:
        return _intermediate_color(self.board_color_white,
                                   self.board_color_black)

    def is_cell_white(self, c_rank: int, c_file: int) -> bool:
        if self.flipped:
            return (c_rank + c_file) % 2 == 1
        return (c_rank + c_file) % 2 == 0

    def draw_white_cell(self, top_x: int, top_y: int):
        self.screen.fill(
            self.board_color_white,
            (top_x, top_y, self.cell_length, self.cell_length),
        )

        # draw noise pixels for realistic touch
        n = int(NOISE_PCT * self.cell_length)
        for _ in range(n):
            x = randint(top_x, top_x + int(self.cell_length))
            y = randint(top_y, top_y + int(self.cell_length))
            self.screen.set_at((x, y), self._noise_color())
        # end of noise

    def draw_black_cell(self, top_x: int, top_y: int):
        self.screen.fill(
            self.board_color_black,
            (top_x, top_y, self.cell_length, self.cell_length),
        )

        # draw noise pixels for realistic touch
        n = int(NOISE_PCT * self.cell_length)
        for _ in range(n):
            x = randint(top_x, top_x + int(self.cell_length))
            y = randint(top_y, top_y + int(self.cell_length))
            self.screen.set_at((x, y), self._noise_color())

    def draw_cell_coords(self):
        """
        Draw the a-h and 1-8 in the bottom and right cells
        """

        # first draw the letters in the last file
        c_rank = 8
        y_pos = self.cell_pos_y(c_rank)
        c_file = 1
        while c_file <= 8:
            x_pos = self.cell_pos_x(c_file)
            is_white = self.is_cell_white(c_rank=c_rank, c_file=c_file)
            c_file_letter = c_file_letter = (chr(ord("h") -
                                                 (c_file - 1)) if self.flipped
                                             else chr(ord("a") + (c_file - 1)))

            letter = self.board_font.render(
                c_file_letter,
                True,
                (self.board_color_black
                 if is_white else self.board_color_white),
            )
            self.screen.blit(
                letter,
                (x_pos + self.letter_x_align, y_pos + self.letter_y_align),
            )
            c_file += 1

        # draw the number is the last column
        c_rank = 1
        c_file = 8
        x_pos = self.cell_pos_x(c_file)
        while c_rank <= 8:
            y_pos = self.cell_pos_y(c_rank)
            is_white = self.is_cell_white(c_rank=c_rank, c_file=c_file)
            c_num = 9 - c_rank
            c_rank_number = c_rank_number = (chr(ord("8") -
                                                 (c_num - 1)) if self.flipped
                                             else chr(ord("1") + (c_num - 1)))
            number = self.board_font.render(
                c_rank_number,
                True,
                (self.board_color_black
                 if is_white else self.board_color_white),
            )
            self.screen.blit(
                number,
                (x_pos + self.number_x_align, y_pos + self.number_y_align),
            )
            c_rank += 1

    def draw_board(self):
        self.screen.fill(self.WINDOW_BACKGROUND)
        c_file = 1
        while c_file < 9:
            c_rank = 1
            while c_rank < 9:
                x_pos = self.cell_pos_x(c_file)
                y_pos = self.cell_pos_y(c_rank)
                if self.is_cell_white(c_rank=c_rank, c_file=c_file):
                    self.draw_white_cell(x_pos, y_pos)
                else:
                    self.draw_black_cell(x_pos, y_pos)
                c_rank += 1
            c_file += 1
        self.draw_cell_coords()
        pygame.display.update()


class BlueBoard(DefaultBoard):

    def __init__(
        self,
        screen: Surface,
    ):
        super().__init__(
            screen,
            border_color=(141, 171, 181),
            board_color_white=(0xFF, 0xFE, 0xFA),
            board_color_black=(0x0C, 0x4D, 0x9C),
        )


class GreenBoard(DefaultBoard):

    def __init__(
        self,
        screen: Surface,
    ):
        super().__init__(
            screen,
            border_color=(141, 171, 181),
            board_color_white=(0xFF, 0xFE, 0xFA),
            board_color_black=(0x3B, 0x73, 0x2B),
        )


class BrownBoard(DefaultBoard):

    def __init__(
        self,
        screen: Surface,
    ):
        super().__init__(
            screen,
            border_color=(141, 171, 181),
            board_color_white=(0xCA, 0xB1, 0x76),
            board_color_black=(0x36, 0x1F, 0x03),
        )


def _intermediate_color(c1: tuple, c2: tuple) -> tuple:
    c3 = ((c1[0] + c2[0]) / 2, (c1[1] + c2[1]) / 2, (c1[2] + c1[2]) / 2)
    return c3


def random_board_theme():
    theme_list = [DefaultBoard, BlueBoard, GreenBoard, BrownBoard]
    n = randrange(0, len(theme_list))
    return theme_list[n]
