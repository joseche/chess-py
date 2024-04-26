import logging as log
from abc import abstractmethod
from enum import Enum, unique

from boards import DefaultBoard
from pygame import Surface


@unique
class PieceTypes(Enum):
    PAWN = "Pawn"
    ROOK = "Rook"
    KNIGHT = "Knight"
    BISHOP = "Bishop"
    QUEEN = "Queen"
    KING = "King"


@unique
class PieceColor(Enum):
    WHITE = "White"
    BLACK = "Black"


class Piece:

    def __init__(self) -> None:
        self.c_rank: int = 1
        self.c_file: int = 1
        self.c_type: PieceTypes = PieceTypes.PAWN
        self.c_color: PieceColor = PieceColor.WHITE

    @abstractmethod
    def move(self, row: int, col: int):
        pass

    @abstractmethod
    def draw(self, screen: Surface, b: DefaultBoard):
        pass


class Pawn(Piece):
    img_black: Surface
    img_white: Surface

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
        if Pawn.img_black is None:
            log.info("class prop is None, so,,, loading images")
            Pawn.load_images(b)
        screen.blit(Pawn.img_black,
                    (b.cell_pos_x(self.c_file), b.cell_pos_y(self.c_rank)))


class Rook(Piece):

    def __init__(self) -> None:
        super().__init__()
        self.c_type = PieceTypes.ROOK


class Knight(Piece):

    def __init__(self) -> None:
        super().__init__()
        self.c_type = PieceTypes.KNIGHT
