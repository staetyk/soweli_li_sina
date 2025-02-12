from pygame import Surface as image
from typing import *


unique = lambda x : x if len(x) == 0 else list(set(x))


class Thing:
    def __init__(self, name: str, prop: list[str] = [], sprite: image|None = None, transform: list["Thing"] = [], facing: int = 0, _I: bool = True):
        self._name = name
        self.propL: list = prop
        self.propA: list = []
        self.sprite = sprite
        self.transL: list = transform
        self.transA: list = []
        self.face = 1
        self.turn = facing
        self.default = prop
        global ijo
        if _I: ijo.append(self)
    
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
        if (self.turn > 0 & direction % 2 == 1) or self.turn == 2: self.face = direction


class Word(Thing):
    def __init__(self, name: str, type: int, mean: Thing|None = None, sprite: image|None = None):
        super().__init__(name, ["tawa"], sprite, _I = False)
        self._mean = mean
        self._type = type
        global nimi
        nimi.update({name : self})


ijo = []

nimi = {}


def clear():
    for x in ijo: x.clr() #type: ignore