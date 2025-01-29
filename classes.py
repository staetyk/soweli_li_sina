import pygame
from typing import *


class Thing:
    def __init__(self, name: str, prop: List[str, None] = [], sprite: pygame.image|None = None, transform: "Thing"|None = None):
        self._name = name
        self.prop = prop
        self.sprite = sprite
        self.trans = transform
    
    def add(self, other: Word|"Thing"):
        if isinstance(other, Word):
            self.prop = list(set(self.prop.append(other._name)))
        else:
            self.trans = other
    
    def pop(self, other: Word|"Thing"):
        if isinstance(other, Word):
            self.prop = list(set(self.prop.remove(other._name)))
        else:
            self.trans = None


class Word(Thing):
    def __init__(self, name: str, type: int, mean: Thing|None = None, sprite: pygame.image|None = None):
        super().__init__(name, ["tawa"], sprite)
        self._mean = mean
        self._type = type