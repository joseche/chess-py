import logging
import os

from pygame.image import load
from pygame.transform import scale

logger = logging.getLogger(__name__)


class MediaManager:
    def __new__(cls):
        logger.debug("inside __new__ for %s", cls)
        if not hasattr(cls, "instance"):
            logger.debug("%s has not instance", cls)
            cls.instance = object.__new__(cls)
        else:
            logger.debug("%s already has an instance: %d", cls, id(cls.instance))
        return cls.instance

    def __init__(self, cell_lenght=12) -> None:
        if hasattr(self, "initialized"):
            logger.debug("%s is already initialized", self)
            return
        logger.debug("initializing %s", self)
        self.dir = os.path.dirname(os.path.abspath(__file__))
        self.load_pieces_images()
        self.resize_images(cell_lenght)
        self.initialized = True

    def load_pieces_images(self):
        logger.debug("loading piece images")
        self.black_pawn = load(f"{self.dir}/sprites/black-pawn.png")
        self.white_pawn = load(f"{self.dir}/sprites/white-pawn.png")
        self.black_rook = load(f"{self.dir}/sprites/black-rook.png")
        self.white_rook = load(f"{self.dir}/sprites/white-rook.png")
        self.black_knight = load(f"{self.dir}/sprites/black-knight.png")
        self.white_knight = load(f"{self.dir}/sprites/white-knight.png")
        self.black_bishop = load(f"{self.dir}/sprites/black-bishop.png")
        self.white_bishop = load(f"{self.dir}/sprites/white-bishop.png")
        self.black_queen = load(f"{self.dir}/sprites/black-queen.png")
        self.white_queen = load(f"{self.dir}/sprites/white-queen.png")
        self.black_king = load(f"{self.dir}/sprites/black-king.png")
        self.white_king = load(f"{self.dir}/sprites/white-king.png")

    def resize_images(self, cell_length: float):
        logger.debug("resizing images to cell_length: %d", cell_length)
        length = int((cell_length / 10) * 8)
        self.b_pawn = scale(self.black_pawn, (length, length))
        self.w_pawn = scale(self.white_pawn, (length, length))
        self.b_rook = scale(self.black_rook, (length, length))
        self.w_rook = scale(self.white_rook, (length, length))
        self.b_knight = scale(self.black_knight, (length, length))
        self.w_knight = scale(self.white_knight, (length, length))
        self.b_bishop = scale(self.black_bishop, (length, length))
        self.w_bishop = scale(self.white_bishop, (length, length))
        self.b_queen = scale(self.black_queen, (length, length))
        self.w_queen = scale(self.white_queen, (length, length))
        self.b_king = scale(self.black_king, (length, length))
        self.w_king = scale(self.white_king, (length, length))
