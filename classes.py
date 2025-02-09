from pygame import image
from typing import *


class Thing:
    def __init__(self, name: str, prop: List[str, None] = [], sprite: image|None = None, transform: List["Thing", None] = None, facing: bool = False, I: bool = True):
        self._name = name
        self.propL = prop
        self.propA = []
        self.sprite = sprite
        self.transL = transform
        self.transA = []
        self.face = False
        self.turn = facing
        self.default = prop
        global ijo
        if I: ijo = ijo.append(self)
    
    def add(self, other: "Word"|"Thing", b: bool = True):
        if isinstance(other, Word):
            if b:
                self.propL = list(set(self.propL.append(other._name)))
            else:
                self.propA = list(set(self.propA.append(other._name)))
        elif b:
            self.transL = list(set(self.transL.append(other)))
        else:
            self.transA = list(set(self.transA.append(other)))
    
    def pop(self, other: "Word"|"Thing", b: bool = True):
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