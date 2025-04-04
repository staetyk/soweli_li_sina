import pygame
import ComSurLib
from math import *
from csv import reader



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


def frame(dim: tuple[int, int], scene: float, preSc: float, key: int) -> tuple[float, pygame.Surface]:
    scene = int(str(scene).lstrip("2."))
    if preSc != scene: init(scene)

    if key == 0:
        try: pygame.mixer.Sound("sounds/click.mp3").play()
        except: pass

    current = ComSurLib.load()[0]

    base = pygame.Surface(dim)
    base.fill(ComSurLib.style["sel_bg"])
    for i in range(ComSurLib.style["sel_num_y"]):
        for j in range(ComSurLib.style["sel_num_x"]):
            n = j + i * ComSurLib.style["sel_num_x"] + scene * ComSurLib.style["sel_num_x"] * ComSurLib.style["sel_num_y"]
            this = ["lock", "next", "done"][0 if n < current else (1 if n == current else 2)]
            
            cell = pygame.Rect(j * (dim[0] - 2 * ComSurLib.style["sel_pad_x"]) // ComSurLib.style["sel_num_x"], i * (dim[1] - 2 * ComSurLib.style["sel_pad_y"]) // ComSurLib.style["sel_num_y"], (dim[0] - 2 * ComSurLib.style["sel_pad_x"]) // ComSurLib.style["sel_num_x"], (dim[1] - 2 * ComSurLib.style["sel_pad_y"]) // ComSurLib.style["sel_num_y"])
            
            level = ComSurLib.button(str(n).zfill(2), ComSurLib.lang(), ComSurLib.style["sel_lvl_txt_font"], ComSurLib.style["sel_lvl_txt_var"], ComSurLib.style[f"sel_lvl_{this}_txt"], ComSurLib.style["sel_lvl_txt_pad_x"], ComSurLib.style["sel_lvl_txt_pad_y"], ComSurLib.style[f"sel_lvl_{this}_fill"], ComSurLib.style[f"sel_lvl_{this}_out"], ComSurLib.style["sel_lvl_wid"], ComSurLib.style["sel_lvl_siz_x"] * cell.width, ComSurLib.style["sel_lvl_siz_y"] * cell.height, ComSurLib.style["sel_lvl_rad"], cursed == n, ComSurLib.style["sel_cur_col"], ComSurLib.style["sel_cur_pad_x"], ComSurLib.style["sel_cur_pad_y"], ComSurLib.style["sel_cur_len_x"], ComSurLib.style["sel_cur_len_y"], ComSurLib.style["sel_cur_wid_x"], ComSurLib.style["sel_cur_wid_y"], True, True)