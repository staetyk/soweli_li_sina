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

    