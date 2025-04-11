import pygame
import ComSurLib
from math import *
from csv import reader
from typing import Optional



def check(i: int) -> bool:
    try: open(f"levels/lvl_{i}.csv", "r")
    except: return False
    else: return True


num, curse = 1, [0, 0, 0]

def init():
    global num, curse
    num = 0
    while check(num): num += 1
    curse = [0, 0, 0]


cursed = lambda : curse[0] * ComSurLib.style["sel_num_x"] * ComSurLib.style["sel_num_y"] + curse[2] * ComSurLib.style["sel_num_x"] + curse[1]


def frame(dim: tuple[int, int], preSc: float, key: int) -> tuple[float, Optional[pygame.Surface]]:
    if preSc != 2: init()

    current = ComSurLib.load()[0]

    global curse
    if key == 0:
        if cursed() <= current:
            try: sfx = pygame.mixer.Sound("sounds/click.mp3")
            except: pass
            else:
                sfx.set_volume(ComSurLib.settings["SFX"] / ComSurLib.style["glob_vol_sfx"] * ComSurLib.settings["Master"] / ComSurLib.style["glob_vol_main"])
                sfx.play()
            return (cursed() / 100, None)
        else:
            try: sfx = pygame.mixer.Sound("sounds/fail.mp3")
            except: pass
            else:
                sfx.set_volume(ComSurLib.settings["SFX"] / ComSurLib.style["glob_vol_sfx"] * ComSurLib.settings["Master"] / ComSurLib.style["glob_vol_main"])
                sfx.play()
    elif key == 6: return (4, None) 
    elif key == 1:
        if curse[2] > 0: curse[2] -= 1
        else:
            try: sfx = pygame.mixer.Sound("sounds/fail.mp3")
            except: pass
            else:
                sfx.set_volume(ComSurLib.settings["SFX"] / ComSurLib.style["glob_vol_sfx"] * ComSurLib.settings["Master"] / ComSurLib.style["glob_vol_main"])
                sfx.play()
    elif key == 3:
        if cursed() + ComSurLib.style["sel_num_x"] > num:
            try: sfx = pygame.mixer.Sound("sounds/fail.mp3")
            except: pass
            else:
                sfx.set_volume(ComSurLib.settings["SFX"] / ComSurLib.style["glob_vol_sfx"] * ComSurLib.settings["Master"] / ComSurLib.style["glob_vol_main"])
                sfx.play()
        elif curse[2] < ComSurLib.style["sel_num_y"]: curse[2] += 1
        else:
            try: sfx = pygame.mixer.Sound("sounds/fail.mp3")
            except: pass
            else:
                sfx.set_volume(ComSurLib.settings["SFX"] / ComSurLib.style["glob_vol_sfx"] * ComSurLib.settings["Master"] / ComSurLib.style["glob_vol_main"])
                sfx.play()
    elif key == 2:
        if cursed() + 1 >= num:
            try: sfx = pygame.mixer.Sound("sounds/fail.mp3")
            except: pass
            else:
                sfx.set_volume(ComSurLib.settings["SFX"] / ComSurLib.style["glob_vol_sfx"] * ComSurLib.settings["Master"] / ComSurLib.style["glob_vol_main"])
                sfx.play()
        elif curse[1] < ComSurLib.style["sel_num_x"]: curse[1] += 1
        elif cursed() + ComSurLib.style["sel_num_x"] * ComSurLib.style["sel_num_y"] - curse[1] >= num:
            try: sfx = pygame.mixer.Sound("sounds/fail.mp3")
            except: pass
            else:
                sfx.set_volume(ComSurLib.settings["SFX"] / ComSurLib.style["glob_vol_sfx"] * ComSurLib.settings["Master"] / ComSurLib.style["glob_vol_main"])
                sfx.play()
        elif curse[0] < ceil(num / (ComSurLib.style["sel_num_x"] * ComSurLib.style["sel_num_y"])):
            curse[1] = 0
            curse[0] += 1
        else:
            try: sfx = pygame.mixer.Sound("sounds/fail.mp3")
            except: pass
            else:
                sfx.set_volume(ComSurLib.settings["SFX"] / ComSurLib.style["glob_vol_sfx"] * ComSurLib.settings["Master"] / ComSurLib.style["glob_vol_main"])
                sfx.play()
    elif key == 4:
        if curse[1] > 0: curse[1] -= 1
        elif curse[0] > 0:
            curse[1] = ComSurLib.style["sel_num_x"]
            curse[0] -= 1
        else:
            try: sfx = pygame.mixer.Sound("sounds/fail.mp3")
            except: pass
            else:
                sfx.set_volume(ComSurLib.settings["SFX"] / ComSurLib.style["glob_vol_sfx"] * ComSurLib.settings["Master"] / ComSurLib.style["glob_vol_main"])
                sfx.play()

    page = cursed() // (ComSurLib.style["sel_num_x"] * ComSurLib.style["sel_num_y"])

    base = pygame.Surface(dim)
    base.fill(ComSurLib.style["sel_bg"])
    for i in range(ComSurLib.style["sel_num_y"]):
        for j in range(ComSurLib.style["sel_num_x"]):
            n = j + i * ComSurLib.style["sel_num_x"] + page * ComSurLib.style["sel_num_x"] * ComSurLib.style["sel_num_y"]
            if n >= num: break
            this = ["done", "next", "lock"][0 if n < current else (1 if n == current else 2)]
            
            cell = pygame.Rect(dim[0] * j * ComSurLib.style["sel_lvl_siz_x"] // ComSurLib.style["sel_num_x"], dim[1] * i * ComSurLib.style["sel_lvl_siz_y"] // ComSurLib.style["sel_num_y"], dim[0] * ComSurLib.style["sel_lvl_siz_x"] // ComSurLib.style["sel_num_x"], dim[1] * ComSurLib.style["sel_lvl_siz_y"] // ComSurLib.style["sel_num_y"])
            
            level = ComSurLib.button(str(n).zfill(2), ComSurLib.lang(), ComSurLib.style["sel_lvl_txt_font"], ComSurLib.style["sel_lvl_txt_var"], ComSurLib.style[f"sel_lvl_{this}_txt"], ComSurLib.style["sel_lvl_txt_pad_x"], ComSurLib.style["sel_lvl_txt_pad_y"], ComSurLib.style[f"sel_lvl_{this}_fill"], ComSurLib.style[f"sel_lvl_{this}_out"], ComSurLib.style["sel_lvl_wid"], ComSurLib.style["sel_lvl_siz_x"] * cell.width * (1 - 2 * (ComSurLib.style["sel_cur_wid_y"] + ComSurLib.style["sel_cur_pad_x"])), ComSurLib.style["sel_lvl_siz_y"] * cell.height * (1 - 2 * (ComSurLib.style["sel_cur_wid_x"] + ComSurLib.style["sel_cur_pad_y"])), ComSurLib.style["sel_lvl_rad"], n == cursed(), ComSurLib.style["sel_cur_col"], ComSurLib.style["sel_cur_pad_x"], ComSurLib.style["sel_cur_pad_y"], ComSurLib.style["sel_cur_len_x"], ComSurLib.style["sel_cur_len_y"], ComSurLib.style["sel_cur_wid_x"], ComSurLib.style["sel_cur_wid_y"], True, True, ComSurLib.style["sel_bg"])

            padded = ((cell.width - level.get_width()) / 2, (cell.height - level.get_height()) / 2)
            base.blit(level, (cell.x + padded[0], cell.y + padded[1]))

    return (2, base)