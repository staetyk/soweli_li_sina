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

def init():
    global num, cursed
    num = 0
    while check(num): num += 1
    cursed = 0


def frame(dim: tuple[int, int], preSc: float, key: int) -> tuple[float, Optional[pygame.Surface]]:
    if preSc != 2: init()

    global cursed
    if key == 0:
        try: pygame.mixer.Sound("sounds/click.mp3").play()
        except: pass
        return (cursed / 100, None)
    elif key == 6: return (4, None)        

    page = cursed // (ComSurLib.style["sel_num_x"] * ComSurLib.style["sel_num_y"])

    current = ComSurLib.load()[0]

    base = pygame.Surface(dim)
    base.fill(ComSurLib.style["sel_bg"])
    for i in range(ComSurLib.style["sel_num_y"]):
        for j in range(ComSurLib.style["sel_num_x"]):
            n = j + i * ComSurLib.style["sel_num_x"] + page * ComSurLib.style["sel_num_x"] * ComSurLib.style["sel_num_y"]
            if n >= num: break
            this = ["lock", "next", "done"][0 if n < current else (1 if n == current else 2)]
            
            cell = pygame.Rect(j * ComSurLib.style["sel_lvl_siz_x"] // ComSurLib.style["sel_num_x"], i * ComSurLib.style["sel_lvl_siz_y"] // ComSurLib.style["sel_num_y"], ComSurLib.style["sel_lvl_siz_x"] // ComSurLib.style["sel_num_x"], ComSurLib.style["sel_lvl_siz_y"] // ComSurLib.style["sel_num_y"])
            
            level = ComSurLib.button(str(n).zfill(2), ComSurLib.lang(), ComSurLib.style["sel_lvl_txt_font"], ComSurLib.style["sel_lvl_txt_var"], ComSurLib.style[f"sel_lvl_{this}_txt"], ComSurLib.style["sel_lvl_txt_pad_x"], ComSurLib.style["sel_lvl_txt_pad_y"], ComSurLib.style[f"sel_lvl_{this}_fill"], ComSurLib.style[f"sel_lvl_{this}_out"], ComSurLib.style["sel_lvl_wid"], ComSurLib.style["sel_lvl_siz_x"] * cell.width, ComSurLib.style["sel_lvl_siz_y"] * cell.height, ComSurLib.style["sel_lvl_rad"], cursed == n, ComSurLib.style["sel_cur_col"], ComSurLib.style["sel_cur_pad_x"], ComSurLib.style["sel_cur_pad_y"], ComSurLib.style["sel_cur_len_x"], ComSurLib.style["sel_cur_len_y"], ComSurLib.style["sel_cur_wid_x"], ComSurLib.style["sel_cur_wid_y"], True, True)

            padded = ((cell.width - level.get_width()) / 2, (cell.height - level.get_height()) / 2)
            base.blit(level, (cell.x + padded[0], cell.y + padded[1]))

    return (2, base)