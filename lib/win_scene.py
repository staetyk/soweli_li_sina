import pygame
import ComSurLib
from math import *
from typing import Optional
import sel_scene



num, cursed = 1, 0

def init():
    global num, cursed
    sel_scene.init()
    num = sel_scene.num
    cursed = 0

init()


def frame(dim: tuple[int, int], Sc: float, preSc: float, key: int) -> tuple[float, Optional[pygame.Surface]]:
    if preSc != Sc: init()
    lvl = int(Sc * 100 - 300)

    global cursed
    
    if key == 0:
        if cursed == 0:
            if lvl + 1 < num: 
                try: sfx = pygame.mixer.Sound("sounds/click.mp3")
                except: pass
                else: sfx.set_volume(ComSurLib.settings["SFX"] / ComSurLib.style["glob_vol_sfx"] * ComSurLib.settings["Master"] / ComSurLib.style["glob_vol_main"])
                return (Sc - 2.99, None)
            else:
                try: sfx = pygame.mixer.Sound("sounds/fail.mp3")
                except: pass
                else: sfx.set_volume(ComSurLib.settings["SFX"] / ComSurLib.style["glob_vol_sfx"] * ComSurLib.settings["Master"] / ComSurLib.style["glob_vol_main"])
                return (2, None)
        else:
            try: sfx = pygame.mixer.Sound("sounds/click.mp3")
            except: pass
            else: sfx.set_volume(ComSurLib.settings["SFX"] / ComSurLib.style["glob_vol_sfx"] * ComSurLib.settings["Master"] / ComSurLib.style["glob_vol_main"])
            return (4, None)
    elif key == 6:
        try: sfx = pygame.mixer.Sound("sounds/click.mp3")
        except: pass
        else: sfx.set_volume(ComSurLib.settings["SFX"] / ComSurLib.style["glob_vol_sfx"] * ComSurLib.settings["Master"] / ComSurLib.style["glob_vol_main"])
        return (2, None)
    elif 1 <= key <= 4:
        cursed = 1 - cursed


    base = pygame.Surface(dim)
    base.fill(ComSurLib.style["win_bg"])

    """
    txt pad y [screen] {frame}
    txt [screen] {pic}
    but pad y [screen] {frame}
    body [screen] {pic}
        but [body] {pic}
        but lin [but] {frame}
        but [body] {pic}
    padding
    """

    """
    b = but_siz_y
    S = body
    p = but_lin
    B = final button size
    P = final padding size
    R = final real button size

    B = S / (p + 2)
    P = p * S / (p + 2)
    R = min(b * S, S / (p + 2))
    """

    txt = pygame.Rect((dim[0] * ComSurLib.style["win_txt_pad_x"], dim[1] * ComSurLib.style["win_txt_pad_y"]), (dim[0] * (1 - 2 * ComSurLib.style["win_txt_pad_x"]), dim[1] * ComSurLib.style["win_txt_siz_y"]))

    body = pygame.Rect((dim[0] * ComSurLib.style["win_but_pad_x"], dim[1] * (ComSurLib.style["win_txt_pad_y"] + ComSurLib.style["win_txt_siz_y"] + ComSurLib.style["win_but_pad_y"])), (dim[0] * (1 - 2 * ComSurLib.style["win_but_pad_x"]), dim[1] * ComSurLib.style["win_body"]))