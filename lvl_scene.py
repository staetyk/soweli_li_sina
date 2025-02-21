import pygame
import ComSurLib
import level_lib
from math import *


def frame(dim: tuple[int, int], Sc: float, preSc: float, key: int) -> tuple[float, pygame.Surface]:
    if key == -1 or Sc != preSc or key == 5:
        PostSc = Sc
        index = (-1 if Sc == -1 else int(str(Sc % 1).replace("0.", "")))
        level_lib.init(index)
    elif 0 <= key <= 4:
        level_lib.step(key)
    elif key == 6:
        PostSc = Sc + 1

    show = pygame.Surface(level_lib.width * 140 + (level_lib.width - 1) * 140 * ComSurLib.style["lvl_grid_wid"], level_lib.height * 140 + (level_lib.height - 1) * 140 * ComSurLib.style["lvl_grid_wid"])
    show.fill(ComSurLib.style["lvl_grid_col"])