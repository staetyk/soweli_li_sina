import pygame
from csv import reader


style = {}
with open("style.csv", "r") as file:
    for row in reader(file):
        if row[1] == "n": style.update({row[0] : int(row[2])})
        elif row[1] == "c": style.update({row[0] : int(row[2], 16)})
        elif row[1] == "p": style.update({row[0] : eval(row[2])})
        elif row[1] == "s": style.update({row[0] : row[2]})
        elif row[1] == "fs":
            style.update({row[0] : pygame.font.SysFont(row[2], 12)})
        elif row[1] == "fc": style.update({row[0] : pygame.font.Font(f"fonts/{row[2]}", 12)})