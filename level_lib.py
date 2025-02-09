from components import *
from csv import reader
from classes import Word, Thing, ijo


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


def act() -> bool:
    global map
    for index, cell in map.items():
        old = (cell if len(cell) > 0 else [tKon])

        s = []
        p = []
        o = []
        w = False
        m = False
        for i in range(len(old)):
            x = old[i]
            prop = [(y for y in x.propL if y not in x.propA)]
            if "sina" in prop: s.append(i)
            if "pini" in prop: p.append(i)
            if "open" in prop: o.append(i)
            w = w | "pona" in prop
            m = m | "moli" in prop
        
        a = []
        if len(s) > 0:
            if w: return True
            if m: a.extend(s)
        n = min(len(p), len(o))
        if n > 0:
            for i in range(n):
                a.append(p[i])
                a.append(o[i])
        
        new = [(old[i] for i in range(len(old)) if i not in a & old[i] not is tKon)]
        map.update({index : new})
    return False


def change() -> None:
    global map
    for index, cell in map.items():
        old = (cell if len(cell) > 0 else [tKon])

        new = []
        for x in old:
            trans = [(y for y in x.transL if y not in x.transA)]
            if len(trans) == 0: new = new.append(x)
            else: new = new.extend(trans)
        new = [(x for x in new if x not is tKon)]
        map.update({index : new})