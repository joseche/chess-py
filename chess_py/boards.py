from random import randrange

import pygame
from pygame import Surface


class DefaultBoard:
    WINDOW_BACKGROUND = (0xBD, 0xC7, 0xDD)

    def __init__(
        self,
        screen: Surface,
        window_width: int = 640,
        window_height: int = 640,
        border_color: tuple = (141, 171, 181),
        board_color_white: tuple = (236, 244, 214),
        board_color_black: tuple = (45, 149, 150),
        flipped: bool = False,
        draw_cell_coords: bool = True,
    ):
        self.screen = screen
        self.border_color = border_color
        self.board_color_white = board_color_white
        self.board_color_black = board_color_black
        self.flipped = flipped
        self.draw_cell_coords = draw_cell_coords
        self.adjustSize(window_width=window_width, window_height=window_height)

    def adjustSize(self, window_width: int, window_height: int):
        self.window_width = window_width
        self.window_height = window_height
        self.cell_length = min(window_width, window_height) / 10
        self.letter_x_align = self.cell_length / 16
        self.letter_y_align = (self.cell_length / 4) * 3
        self.number_x_align = (self.cell_length / 8) * 7
        self.number_y_align = self.cell_length / 32
        self.board_font = pygame.font.SysFont(
            "Comic Sans MS", int(self.cell_length / 6), bold=True
        )

    def cellPosX(self, col: int = 1) -> int:
        return int(col * self.cell_length)

    def cellPosY(self, row: int = 1) -> int:
        return int(row * self.cell_length)

    def isCellWhite(self, c_rank: int, c_file: int) -> bool:
        if not self.flipped:
            return (c_rank + c_file) % 2 == 0
        else:
            return (c_rank + c_file) % 2 == 1

    def drawWhiteCell(self, topX: int, topY: int):
        self.screen.fill(
            self.board_color_white,
            (topX, topY, self.cell_length, self.cell_length),
        )

    def drawBlackCell(self, topX: int, topY: int):
        self.screen.fill(
            self.board_color_black,
            (topX, topY, self.cell_length, self.cell_length),
        )

    def drawCellCoords(self):
        if not self.flipped:
            c_rank = 8
            y_pos = self.cellPosY(c_rank)
            c_file = 1
            while c_file <= 8:
                x_pos = self.cellPosX(c_file)
                is_white = self.isCellWhite(c_rank=c_rank, c_file=c_file)
                c_file_letter = chr(ord("a") + (c_file - 1))
                letter = self.board_font.render(
                    c_file_letter,
                    True,
                    (
                        self.board_color_black
                        if is_white
                        else self.board_color_white
                    ),
                )
                self.screen.blit(
                    letter,
                    (x_pos + self.letter_x_align, y_pos + self.letter_y_align),
                )
                c_file += 1

            c_rank = 1
            c_file = 8
            x_pos = self.cellPosX(c_file)
            while c_rank <= 8:
                y_pos = self.cellPosY(c_rank)
                is_white = self.isCellWhite(c_rank=c_rank, c_file=c_file)
                c_num = 9 - c_rank
                c_rank_number = chr(ord("1") + (c_num - 1))
                number = self.board_font.render(
                    c_rank_number,
                    True,
                    (
                        self.board_color_black
                        if is_white
                        else self.board_color_white
                    ),
                )
                self.screen.blit(
                    number,
                    (x_pos + self.number_x_align, y_pos + self.number_y_align),
                )
                c_rank += 1

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
                x_pos = self.cellPosX(c_file)
                y_pos = self.cellPosY(c_rank)
                if self.isCellWhite(c_rank=c_rank, c_file=c_file):
                    self.drawWhiteCell(x_pos, y_pos)
                else:
                    self.drawBlackCell(x_pos, y_pos)
                c_rank += 1
            c_file += 1
        self.drawCellCoords()
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
        flipped: bool = False,
    ):
        super().__init__(
            screen,
            window_width,
            window_height,
            border_color=(141, 171, 181),
            board_color_white=(0xFF, 0xFE, 0xFA),
            board_color_black=(0x0C, 0x4D, 0x9C),
            flipped=flipped,
        )


class GreenBoard(DefaultBoard):

    def __init__(
        self,
        screen: Surface,
        window_width: int = 640,
        window_height: int = 640,
        flipped: bool = False,
    ):
        super().__init__(
            screen,
            window_width,
            window_height,
            border_color=(141, 171, 181),
            board_color_white=(0xFF, 0xFE, 0xFA),
            board_color_black=(0x3B, 0x73, 0x2B),
            flipped=flipped,
        )


class BrownBoard(DefaultBoard):

    def __init__(
        self,
        screen: Surface,
        window_width: int = 640,
        window_height: int = 640,
        flipped: bool = False,
    ):
        super().__init__(
            screen,
            window_width,
            window_height,
            border_color=(141, 171, 181),
            board_color_white=(0xCA, 0xB1, 0x76),
            board_color_black=(0x36, 0x1F, 0x03),
            flipped=flipped,
        )


def random_board_theme() -> DefaultBoard:
    theme_list = [DefaultBoard, BlueBoard, GreenBoard, BrownBoard]
    n = randrange(0, len(theme_list))
    return theme_list[n]
