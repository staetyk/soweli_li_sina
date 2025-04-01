from re import L
import pygame
from csv import reader
import copy


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


script = {}
with open("script.csv", "r") as file:
    i = 0
    for row in reader(file):
        i += 1
        if len(row) < 2: continue
        script.update({i : list(row)})


# eng, sl, sp
def translate(txt: str, system: int) -> str:
    if system == 2:
        out = txt
    else:
        if system == 1:
            txt = txt.replace("-", " ").replace("[", "").replace("]", "")
            txt2 = ""
            for x in txt.split():
                txt2 += " "
                txt2 += (x if x.islower() else x.title())
            txt = txt2.lstrip(" ")
        out = txt
        for x in txt:
            out += x
            out += " "
        out = out.rstrip(" ")
    return out


settings = {
    "English" : False,
    "Sitelen Pona" : True,
    "Master" : style["glob_vol_main"],
    "Music" : style["glob_vol_mus"],
    "SFX" : style["glob_vol_sfx"]
}


def text(line: int, system: int, font: pygame.font.Font, var: str, col: pygame.Color, x: float, y: float) -> pygame.Surface:
    txt = translate(script[line][(0 if system == 0 else 1)], system)
    font = copy.copy(font)
    font.set_bold("b" in var)
    font.set_italic("i" in var)
    font.set_underline("u" in var)
    font.set_strikethrough("s" in var)
    new = scale((x, y), font.size(txt))
    out = font.render(txt, True, col)
    return pygame.transform.scale(out, new)


def button(line: int, system: int, font: pygame.font.Font, var: str, txtcol: pygame.Color, xpad: float, ypad: float, incol: pygame.Color, outcol: pygame.Color, outwid: float, width: float, height: float, rad: float, cursor: bool, curscol: pygame.Color, cpadx: float, cpady: float, clenx: float, cleny: float, cwidx: float, cwidy: float, cinx: bool, ciny: bool) -> pygame.Surface:
    base = pygame.Surface((width, height))

    r = rad * min(width, height)
    pygame.draw.polygon(base, outcol, ((r, 0), (width - r, 0), (width, r), (width, height - r), (width - r, height), (r, height), (0, height - r), (0, r)))
    for i in range(2):
        for j in range(2):
            pygame.draw.circle(base, outcol, ([r, width - r][i], [r, height - r][j]), r)

    r = rad * min(width, height) * (1 - outwid)
    w = width * (1 - outwid)
    h = height * (1 - outwid)
    w0 = w * outwid
    h0 = h * outwid
    pygame.draw.polygon(base, incol, ((w0 + r, h0), (w0 + w - r, h0), (w0 + w, h0 + r), (w0 + w, h0 + h - r), (w0 + w - r, h0 + h), (w0 + r, h0 + h), (w0, h0 + h - r), (w0, h0 + r)))
    for i in range(2):
        for j in range(2):
            pygame.draw.circle(base, incol, ([w0 + r, w0 + w - r][i], [h0 + r, h0 + h - r][j]), r)

    txt = text(line, system, font, var, txtcol, w - 2 * xpad * w, h - 2 * ypad * h)
    base.blit(txt, (w0 + xpad * w, h0 + ypad * h))

    new = pygame.Surface((width + 2 * width * (cpadx + cwidy) if cursor or cinx else width, height + 2 * height * (cpady + cwidx) if cursor or ciny else height))
    new.blit(base, (width * (cpadx + cwidy), height * (cpady + cwidx)))
    base = new

    if cursor:
        points = [(0, 0), (clenx * width, 0), (clenx * width, cwidx * height), (cwidy * width, cwidx * height), (cwidy * width, cleny * height), (0, cleny * height)]
        for i in range(2):
            for j in range(2):
                p = []
                for k in points:
                    p.append((k[0] if i == 0 else width - k[0], k[1] if j == 0 else height - k[1]))
                pygame.draw.polygon(base, curscol, p)

    return base