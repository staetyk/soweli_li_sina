from pygame import Surface, image, transform
from typing import *


unique = lambda x : x if len(x) == 0 else list(set(x))


class Thing:
    def __init__(self, name: str, prop: list[str] = [], sprite: list[str]|str|None = None, transform: list["Thing"] = [], facing: int = 0, _I: bool = True):
        self._name = name
        self.propL: list = prop
        self.propA: list = []
        if isinstance(sprite, list):
            s = []
            for x in sprite:
                try:
                    s.append(image.load(f"images/{x}.png"))
                except:
                    a.append(image.load("images/placeholder.png"))
            self.sprite = s
        elif isinstance(sprite, str):
            try:
                self.sprite = image.load(f"images/{sprite}.png")
            except:
                self.sprite = image.load("images/placeholder.png")
        else: self.sprite = image.load("images/placeholder.png")
        self.transL: list = transform
        self.transA: list = []
        self.face = 1
        self.turn = facing
        self.default = prop
        global ijo
        if _I: ijo.append(self)
        self.start = facing
    
    def add(self, other, b: bool = True):
        if isinstance(other, Word):
            if b:
                self.propL.append(other._name)
                self.propL = unique(self.propL)
            else:
                self.propA.append(other._name)
                self.propA = unique(self.propA)
        elif b:
            self.transL.append(other)
            self.transL = unique(self.transL)
        else:
            self.transA.append(other)
            self.transA = unique(self.transA)
    
    def pop(self, other, b: bool = True):
        if isinstance(other, Word):
            if b:
                self.propL.remove(other._name)
            else:
                self.propA.remove(other._name)
        elif b:
            self.transL.remove(other)
        else:
            self.transA.remove(other)
    
    def clr(self):
        self.propL = self.default
        self.propA = []
        self.transL = []
        self.transA = []

    def fac(self, direction: int):
        if self.turn > 0: self.face = direction

    def draw(self):
        if self.turn == 0: return self.sprite
        elif self.turn == 1:
            if self.face == 0: return self.sprite[0] # type: ignore
            elif self.face == 2: return self.sprite[2] # type: ignore
            else:
                s = self.sprite[1] # type: ignore
                if self.face == 3: s = transform.flip(s, True, False)
                return s
        else:
            return transform.rotate(self.sprite, ((-90) * self.face) + 90) # type: ignore

    def rst(self):
        self.clr()
        self.face = self.start


class Word(Thing):
    def __init__(self, name: str, type: int, mean: Thing|None = None, sprite: Surface|None = None):
        super().__init__(name, ["tawa"], sprite = sprite, _I = False) # type: ignore
        self._mean = mean
        self._type = type
        global nimi
        nimi.update({name : self})


ijo = []

nimi = {}


def clear():
    for x in ijo: x.clr()

def reset():
    for x in ijo: x.rst()