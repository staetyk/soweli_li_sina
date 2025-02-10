from pygame import image
from typing import *


unique = lambda x : x if len(x) == 0 else list(set(x))


class Thing:
    def __init__(self, name: str, prop: List[str] = [], sprite: image|None = None, transform: List["Thing"] = [], facing: bool = False, I: bool = True):
        self._name = name
        self.propL: list = prop
        self.propA: list = []
        self.sprite = sprite
        self.transL: list = transform
        self.transA: list = []
        self.face = False
        self.turn = facing
        self.default = prop
        global ijo
        if I: ijo = ijo.append(self)
    
    def add(self, other: Word|"Thing", b: bool = True):
        if isinstance(other, Word):
            if b:
                self.propL = unique(self.propL.append(other._name))
            else:
                self.propA = unique(self.propA.append(other._name))
        elif b:
            self.transL = unique(self.transL.append(other))
        else:
            self.transA = unique(self.transA.append(other))
    
    def pop(self, other: Word|"Thing", b: bool = True):
        if isinstance(other, Word):
            if b:
                self.propL = self.propL.remove(other._name)
            else:
                self.propA = self.propA.remove(other._name)
        elif b:
            self.transL = self.transL.remove(other)
        else:
            self.transA = self.transA.remove(other)
    
    def clr(self):
        self.propL = self.default
        self.propA = []
        self.transL = []
        self.transA = []


class Word(Thing):
    def __init__(self, name: str, type: int, mean: Thing|None = None, sprite: image|None = None):
        super().__init__(name, ["tawa"], sprite, I = False)
        self._mean = mean
        self._type = type


ijo = []


def clear():
    for x in ijo: x.clr()