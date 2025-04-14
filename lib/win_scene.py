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
    ...