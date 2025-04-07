import pygame
import ComSurLib
from math import *
from csv import reader
from typing import Optional



def check(i: int) -> bool:
    try: open(f"levels/lvl_{i}.csv", "r")
    except: return False
    else: return True


num, cursed = 1, 0

def init(page: int = 0):
    global num, cursed
    num = 0
    while check(num): num += 1
    num += 1
    cursed = ComSurLib.style["sel_num_x"] * ComSurLib.style["sel_num_y"] * page

init()


def frame(dim: tuple[int, int], scene: float, preSc: float, key: int) -> tuple[float, Optional[pygame.Surface]]:
    scene = int(str(scene).zfill(2).lstrip("2."))
    if preSc != scene: init(scene)

    if key == 0:
        try: pygame.mixer.Sound("sounds/click.mp3").play()
        except: pass
        return (cursed / 100, None)

    current = ComSurLib.load()[0]

    base = pygame.Surface(dim)
    base.fill(ComSurLib.style["sel_bg"])
    for i in range(ComSurLib.style["sel_num_y"]):
        for j in range(ComSurLib.style["sel_num_x"]):
            n = j + i * ComSurLib.style["sel_num_x"] + scene * ComSurLib.style["sel_num_x"] * ComSurLib.style["sel_num_y"]
            this = ["lock", "next", "done"][0 if n < current else (1 if n == current else 2)]
            
            cell = pygame.Rect(j * ComSurLib.style["sel_lvl_siz_x"] // ComSurLib.style["sel_num_x"], i * ComSurLib.style["sel_lvl_siz_y"] // ComSurLib.style["sel_num_y"], ComSurLib.style["sel_lvl_siz_x"] // ComSurLib.style["sel_num_x"], ComSurLib.style["sel_lvl_siz_y"] // ComSurLib.style["sel_num_y"])
            
            level = ComSurLib.button(str(n).zfill(2), ComSurLib.lang(), ComSurLib.style["sel_lvl_txt_font"], ComSurLib.style["sel_lvl_txt_var"], ComSurLib.style[f"sel_lvl_{this}_txt"], ComSurLib.style["sel_lvl_txt_pad_x"], ComSurLib.style["sel_lvl_txt_pad_y"], ComSurLib.style[f"sel_lvl_{this}_fill"], ComSurLib.style[f"sel_lvl_{this}_out"], ComSurLib.style["sel_lvl_wid"], ComSurLib.style["sel_lvl_siz_x"] * cell.width, ComSurLib.style["sel_lvl_siz_y"] * cell.height, ComSurLib.style["sel_lvl_rad"], cursed == n, ComSurLib.style["sel_cur_col"], ComSurLib.style["sel_cur_pad_x"], ComSurLib.style["sel_cur_pad_y"], ComSurLib.style["sel_cur_len_x"], ComSurLib.style["sel_cur_len_y"], ComSurLib.style["sel_cur_wid_x"], ComSurLib.style["sel_cur_wid_y"], True, True)

            padded = ((cell.width - level.get_width()) / 2, (cell.height - level.get_height()) / 2)
            base.blit(level, (cell.x + padded[0], cell.y + padded[1]))

    return (scene, base)