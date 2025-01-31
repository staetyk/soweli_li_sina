import pygame
from typing import *


class Thing:
    def __init__(self, name: str, prop: List[str, None] = [], sprite: pygame.image|None = None, transformL: List["Thing", None] = None, transformA: List["Thing", None] = None):
        self._name = name
        self.prop = prop
        self.sprite = sprite
        self.transL = transformL
        self.transA = transformA
    
    def add(self, other: "Word"|"Thing", b: bool = True):
        if isinstance(other, Word):
            self.prop = list(set(self.prop.append(("" if b else "-") + other._name)))
        elif b:
            self.transL = list(set(self.transL.append(other)))
        else:
            self.transA = list(set(self.transA.append(other)))
    
    def pop(self, other: "Word"|"Thing", b: bool = True):
        if isinstance(other, Word):
            self.prop = self.prop.remove(("" if b else "-") + other._name)
        elif b:
            self.transL = self.transL.remove(other)
        else:
            self.transA = self.transA.remove(other)
    
    def clr(self):
        self.prop = []
        self.transL = []
        self.transA = []


class Word(Thing):
    def __init__(self, name: str, type: int, mean: Thing|None = None, sprite: pygame.image|None = None):
        super().__init__(name, ["tawa"], sprite)
        self._mean = mean
        self._type = type