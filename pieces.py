from enum import Enum
import logging as log
from boards import DefaultBoard
from pygame import Surface
import pygame


class PieceTypes(Enum):
    PAWN = "Pawn"
    ROOK = "Rook"
    KNIGHT = "Knight"
    BISHOP = "Bishop"
    QUEEN = "Queen"
    KING = "King"


class PieceColor(Enum):
    WHITE = "White"
    BLACK = "Black"


class Piece:
    def __init__(self) -> None:
        self.c_rank: int = 1
        self.c_file: int = 1
        self.c_type: PieceTypes = PieceTypes.PAWN
        self.c_color: PieceColor = PieceColor.WHITE

    def move(self, row: int, col: int):
        raise NotImplementedError("abstract method to be implemented")

    def draw(self):
        raise NotImplementedError("abstract method to be implemented")


class Pawn(Piece):
    img_black: Surface = None
    img_white: Surface = None

    def __init__(self) -> None:
        super().__init__()
        self.c_type = PieceTypes.PAWN

    @classmethod
    def load_images(cls, b: DefaultBoard):
        log.info("loading images...")
        cls.img_white = b.load_piece_image("sprites/black-pawn.png")
        cls.img_black = b.load_piece_image("sprites/white-pawn.png")

    def draw(self, screen: Surface, b: DefaultBoard):
        log.info("inside draw")
        if self.img_black == None:
            log.info("class prop is None, so,,, loading images")
            Pawn.load_images(b)
        screen.blit(Pawn.img_black, (b.cellPosX(self.c_file), b.cellPosY(self.c_rank)))


class Rook(Piece):
    def __init__(self) -> None:
        super().__init__()
        self.c_type = PieceTypes.ROOK


class Knight(Piece):
    def __init__(self) -> None:
        super().__init__()
        self.c_type = PieceTypes.KNIGHT
