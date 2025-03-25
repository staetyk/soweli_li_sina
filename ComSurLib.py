import pygame
from csv import reader

pygame.init()


style = {}
with open("style.csv", "r") as file:
    for row in reader(file):
        row = [x.strip() for x in row]
        if row[2] == "": style.update({row[0] : None})
        elif row[1] == "n": style.update({row[0] : int(row[2])})
        elif row[1] == "c": style.update({row[0] : pygame.Color(row[2])})
        elif row[1] == "p": style.update({row[0] : eval(row[2])})
        elif row[1] == "s": style.update({row[0] : row[2]})
        elif row[1] == "fs": style.update({row[0] : pygame.font.SysFont(row[2], 12)})
        elif row[1] == "fc": style.update({row[0] : pygame.font.Font(f"fonts/{row[2]}", 12)})


scale = lambda frame, pic : (int(frame[1] / pic[1] * pic[0]), int(frame[1])) if frame[0] / pic[0] * pic[1] > frame[1] else (int(frame[0]), int(frame[0] / pic[0] * pic[1]))


def translate(txt: str, system: int) -> str:
    if system == 2:
        out = txt
    else:
        out = ""
        for x in txt:
            out += x
            out += " "
        if system == 1:
            out = out.replace("-", " ")
        out = out.rstrip(" ")
    return out


settings = {
    "English" : False,
    "Sitelen Pona" : True,
    "Master" : style["glob_vol_main"],
    "Music" : style["glob_vol_mus"],
    "SFX" : style["glob_vol_sfx"]
}