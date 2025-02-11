from components import *
from csv import reader
from classes import Word, Thing, ijo, clear


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


toi = lambda x, y : x + y * width
toxy = lambda i : (i % width, i // width)

props = lambda x : [(y for y in x.propL if y not in x.propA)]


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
            prop = props(x)
            if "sina" in prop: s.append(i)
            if "pini" in prop: p.append(i)
            if "open" in prop: o.append(i)
            w = w | ("pona" in prop)
            m = m | ("moli" in prop)
        
        a = []
        if len(s) > 0:
            if w: return True
            if m: a.extend(s)
        n = min(len(p), len(o))
        if n > 0:
            for i in range(n):
                a.append(p[i])
                a.append(o[i])
        
        new = [(old[i] for i in range(len(old)) if (i not in a) & (old[i] is not tKon))]
        map.update({index : new})
    return False


def change() -> None:
    global map
    for index, cell in map.items():
        old = (cell if len(cell) > 0 else [tKon])

        new = []
        for x in old:
            trans = [(y for y in x.transL if y not in x.transA)]
            if len(trans) == 0: new.append(x)
            else: new.extend(trans)
        new = [(x for x in new if x is not tKon)]
        map.update({index : new})


def move_lili(A: list[Thing | Word], coords: tuple[int, int], direction: int) -> bool:
    coords1 = (coords[0] + [0, 1, 0, -1][direction], coords[1] + [-1, 0, 1, 0][direction])
    if not (0 <= coords1[0] < width) or not (0 <= coords1[1] < height): return False
    index0 = toi(*coords)
    index1 = toi(*coords1)
    B = map[index1]
    if len(B) == 0: B = [tKon]

    nasin = 0
    for x in A:
        if "pini" in props(x): nasin += 1
        if "open" in props(x): nasin -= 1
        if ("pini" in props(x)) & ("open" in props(x)): A.remove(x)

    out = []
    for x in B:
        p = props(x)
        if "tawa" in p: out.append(x)
        elif "awen" in p:
            if (("pini" if nasin < 0 else "open") in p) & abs(nasin) > 0: out.append(x)