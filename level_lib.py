from components import *
from csv import reader
from classes import Word, Thing, ijo, nimi, clear, unique


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
        a = []
        for i in range(len(old)):
            x = old[i]
            prop = props(x)
            if "sina" in prop: s.append(i)
            if "pini" in prop:
                if "open" in prop: a.append(i)
                else: p.append(i)
            if "open" in prop: o.append(i)
            w = w | ("pona" in prop)
            m = m | ("moli" in prop)
        
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
            else: return False
        else: continue

    else:
        if len(out) == 0: next = True
        else: next = move_lili(out, coords1, direction)
        if next:
            coords2 = (coords[0] - [0, 1, 0, -1][direction], coords[1] - [-1, 0, 1, 0][direction])
            index2 = toi(*coords2)
            global map
            for x in [(y for y in A if y is not tKon)]:
                map[index2].remove(x)
                map[index0].append(x)
            return True
        else: return False


def move_suli(direction: int):
    for x,y in list(map.items())[::(-1 if direction % 3 == 0 else 1)]:
        if len(y) == 0: y = [tKon]
        out = []
        for z in y:
            if "sina" in props(z): out.append(z)
        if len(out) == 0: continue
        else: move_lili(out, toxy(x), direction)
    for x in ijo:
        if "sina" in props(x): x.fac(direction)


def parse(*phrases: str):
    for phrase in phrases:
        phrase = phrase.split(" li ")
        subject, predicate = phrase[0], phrase[1:]
        subject = subject.split(" en ")
        
        sub = []
        for x in subject:
            if "ala" in x:
                x = x.replace(" ala", "")
                sub.extend([(y for y in ijo if y._name != x)])
            else:
                sub.append(nimi[x]._mean)
        sub = unique(sub)

        for x in predicate:
            a = "ala" in x
            x = nimi[x.replace(" ala", "")]
            if x._type == 1: x = x._mean
            for y in sub: y.add(x, not a)


def search(coords: tuple[int, int], l):
    if not (0 <= coords[0] < width) or not (0 <= coords[1] < height): return None
    for x in map[toi(*coords)]:
        if isinstance(x, Word) & l(x): return x
    return None


def read():
    out = []
    for i in range(height):
        for j in range(width):
            for d in range(2):
                phrase = ""
                node = 0
                k = 0
                while node != 7:
                    phrase += " "
                    coords = (j + d * k, i + (1 - d) * k)
                    if node == 0:
                        n =  search(coords, lambda x : x._type == 1)
                        if n is not None:
                            phrase += n._name
                            node = 1
                            continue
                        break
                    elif node == 1:
                        n = search(coords, lambda x : x._name == "ala")
                        if n is not None:
                            phrase += n._name
                            node = 2
                            continue
                        n = search(coords, lambda x : x._name == "en")
                        if n is not None:
                            phrase += n._name
                            node = 3
                            continue
                        n = search(coords, lambda x : x._name == "li")
                        if n is not None:
                            phrase += n._name
                            node = 4
                            continue
                        break
                    elif node == 2:
                        n = search(coords, lambda x : x._name == "en")
                        if n is not None:
                            phrase += n._name
                            node = 3
                            continue
                        n = search(coords, lambda x : x._name == "li")
                        if n is not None:
                            phrase += n._name
                            node = 4
                            continue
                        break
                    elif node == 3:
                        n = search(coords, lambda x : x._type == 1)
                        if n is not None:
                            phrase += n._name
                            node = 1
                            continue
                        break
                    elif node == 4:
                        n = search(coords, lambda x : x._type > 0)
                        if n is not None:
                            phrase += n._name
                            node = 5
                            continue
                        break
                    elif node == 5:
                        n = search(coords, lambda x : x._name == "li")
                        if n is not None:
                            phrase += n._name
                            node = 4
                            continue
                        n = search(coords, lambda x : x._name == "ala")
                        if n is not None:
                            phrase += n._name
                            node = 6
                            continue
                        node = 7
                    elif node == 6:
                        n = search(coords, lambda x : x._name == "li")
                        if n is not None:
                            phrase += n._name
                            node = 4
                            continue
                        node = 7
                    k += 1

                else: continue
                phrase = phrase.strip()
                out.append(phrase)
    return out


def step(direction: int) -> bool:
    clear()
    phrases = read()
    if len(phrases) > 0: parse(phrases)
    if act(): return True
    if direction != -1:
      move(direction)
      clear()
      phrases = read()
      if len(phrases) > 0: parse(phrases)
      if act(): return True
    change()
    return act()