import logging
from abc import abstractmethod
from enum import Enum, unique

from guiboards import DefaultBoard
from pygame import Surface

logger = logging.getLogger(__name__)


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

    # def draw(self, screen: Surface, b: DefaultBoard):
    #     screen.blit(Pawn.img_black,
    #                 (b.cell_pos_x(self.c_file), b.cell_pos_y(self.c_rank)))
