from components import *
from csv import reader
from classes import Word, Thing


width = 1
height = 1
map = {0: []}

def init(level: int):
    global width
    global height
    global map

    with open("levels.lvl_{level}.csv") as file:
        lines = reader(file)
        i = -1
        for x in lines:
            if i == -1:
                width, height = int(x[0]), int(x[1])
                map = dict.fromkeys(range(width * height), [])
            elif x[0] != "0":
                map.update({i : [eval(y) for y in x]})
            i += 1



def act() -> str|None:
    global map
    for index, cell in map.items():
        old = (cell if len(cell) > 0 else [tkon])

        s = []
        p = []
        o = []
        w = False
        m = False
        for i in range(len(old)):
            x = old[i]
            if isinstance(x, Word): continue
            lprop = []
            aprop = []
            for y in x.prop:
                if y[0] == "-": aprop.append(y.replace("-", ""))
                else: lprop.append(y)
            prop = [(y for y in lprop if y not in aprop)]
            if "sina" in prop: s.append(i)
            if "pini" in prop: p.append(i)
            if "open" in prop: o.append(i)
            w = w | "pona" in prop
            m = m | "moli" in prop
        
        a = []
        if len(s) > 0:
            if w: return "win"
            if m: a.extend(s)
        n = min(len(p), len(o))
        if n > 0:
            for i in range(n):
                a.append(p[i])
                a.append(o[i])
        
        new = [(old[i] for i in range(len(old)) if i not in a)]
        map.update({index : new})