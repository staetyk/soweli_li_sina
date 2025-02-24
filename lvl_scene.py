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

    show = pygame.Surface(level_lib.width * 140 + (level_lib.width + 1) * 140 * ComSurLib.style["lvl_grid_wid"], level_lib.height * 140 + (level_lib.height + 1) * 140 * ComSurLib.style["lvl_grid_wid"])
    show.fill(ComSurLib.style["lvl_grid_col"])
    for i in range(level_lib.height):
        for j in range(level_lib.width):
            x = j * (140 + ComSurLib.style["lvl_grid_wid"])
            y = i * (140 + ComSurLib.style["lvl_grid_wid"])
            show.fill(ComSurLib.style["lvl_bg_in"], (x, y, 140, 140))
            if len(level_lib.map[level_lib.toi(j, i)]) > 0:
                for k in level_lib.map[level_lib.toi(j, i)]:
                    k.draw().blit(show, (x, y, 140, 140))

    out = pygame.Surface(dim)
    out.fill(ComSurLib.style["lvl_bg_out"])
    m = min(dim)
    show = pygame.transform.scale(show, (m, m))
    show.blit(out, ((dim[0] - m) // 2, (dim[1] - m) // 2))
    return (PostSc, out)