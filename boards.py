from pygame import Surface
from random import randrange

import pygame


class DefaultBoard:
    WINDOW_BACKGROUND = (0xBD, 0xC7, 0xDD)

    def __init__(
        self,
        screen: Surface,
        window_width: int = 640,
        window_height: int = 640,
        cell_length: int = 0,
        letter_x_align: int = 0,
        letter_y_align: int = 0,
        number_x_align: int = 0,
        number_y_align: int = 0,
        border_color: tuple = (141, 171, 181),
        board_color_white: tuple = (236, 244, 214),
        board_color_black: tuple = (45, 149, 150),
    ):
        self.screen = screen
        self.window_width = window_width
        self.window_height = window_height
        self.cell_length = (
            cell_length if cell_length != 0 else min(window_width, window_height) / 10
        )
        self.letter_x_align = (
            letter_x_align if letter_x_align != 0 else self.cell_length / 16
        )
        self.letter_y_align = (
            letter_y_align if letter_y_align != 0 else (self.cell_length / 4) * 3
        )
        self.number_x_align = (
            number_x_align if number_x_align != 0 else (self.cell_length / 8) * 7
        )
        self.number_y_align = (
            number_y_align if number_y_align != 0 else self.cell_length / 32
        )
        self.border_color = border_color
        self.board_color_white = board_color_white
        self.board_color_black = board_color_black
        self.board_font = pygame.font.SysFont(
            "Comic Sans MS", int(self.cell_length / 6), bold=True
        )

    def cellPosX(self, col: int = 1) -> int:
        return int(col * self.cell_length)

    def cellPosY(self, row: int = 1) -> int:
        return int(row * self.cell_length)

    def drawBoard(self):
        self.screen.fill(self.WINDOW_BACKGROUND)
        pygame.draw.rect(
            self.screen,
            self.border_color,
            (
                self.cell_length - 1,
                self.cell_length - 1,
                self.cell_length * 8 + 2,
                self.cell_length * 8 + 2,
            ),
            2,
            1,
        )

        c_file = 1
        c_rank = 1
        while c_file < 9:
            c_rank = 1
            while c_rank < 9:
                squareColor = (
                    self.board_color_white
                    if ((c_file + c_rank) % 2 == 0)
                    else self.board_color_black
                )
                contrastColor = (
                    self.board_color_white
                    if ((c_file + c_rank) % 2 == 1)
                    else self.board_color_black
                )
                x_pos = self.cellPosX(c_file)
                y_pos = self.cellPosY(c_rank)
                self.screen.fill(
                    squareColor,
                    (x_pos, y_pos, self.cell_length, self.cell_length),
                )

                if c_rank == 8:  # draw the letters for the files
                    c_file_letter = chr(ord("a") + (c_file - 1))
                    letter = self.board_font.render(c_file_letter, True, contrastColor)
                    self.screen.blit(
                        letter,
                        (x_pos + self.letter_x_align, y_pos + self.letter_y_align),
                    )
                if c_file == 8:  # draw the rank number
                    c_num = 9 - c_rank
                    c_rank_number = chr(ord("1") + (c_num - 1))
                    number = self.board_font.render(c_rank_number, True, contrastColor)
                    self.screen.blit(
                        number,
                        (x_pos + self.number_x_align, y_pos + self.number_y_align),
                    )

                c_rank += 1
            c_file += 1
        pygame.display.update()

    def load_piece_image(self, filename: str):
        img_length = int((self.cell_length / 10) * 8)
        img_raw = pygame.image.load(filename)
        return pygame.transform.scale(img_raw, (img_length, img_length))


class BlueBoard(DefaultBoard):
    def __init__(
        self,
        screen: Surface,
        window_width: int = 640,
        window_height: int = 640,
    ):
        super().__init__(
            screen,
            window_width,
            window_height,
            border_color=(141, 171, 181),
            board_color_white=(0xFF, 0xFE, 0xFA),
            board_color_black=(0x0C, 0x4D, 0x9C),
        )


class GreenBoard(DefaultBoard):
    def __init__(
        self,
        screen: Surface,
        window_width: int = 640,
        window_height: int = 640,
    ):
        super().__init__(
            screen,
            window_width,
            window_height,
            border_color=(141, 171, 181),
            board_color_white=(0xFF, 0xFE, 0xFA),
            board_color_black=(0x3B, 0x73, 0x2B),
        )


class BrownBoard(DefaultBoard):
    def __init__(
        self,
        screen: Surface,
        window_width: int = 640,
        window_height: int = 640,
    ):
        super().__init__(
            screen,
            window_width,
            window_height,
            border_color=(141, 171, 181),
            board_color_white=(0xCA, 0xB1, 0x76),
            board_color_black=(0x36, 0x1F, 0x03),
        )


def random_board_theme() -> DefaultBoard:
    theme_list = [DefaultBoard, BlueBoard, GreenBoard, BrownBoard]
    n = randrange(0, len(theme_list))
    return theme_list[n]
