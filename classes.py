import pygame
from typing import *


class Thing:
    def __init__(self, name: str, prop: List[str, None], sprite: pygame.image|None = None, transform: "Thing"|None = None):
        self._name = name
        self.prop = prop
        self.sprite = sprite
        self.trans = transform


class Word(Thing):
    def __init__(self, name: str, type: int, sprite: pygame.image|None = None, mean: Thing|str|None = None):
        super().__init__(name, ["tawa"], sprite)
        self._mean = mean
        self._type = type



