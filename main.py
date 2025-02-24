import pygame
import ComSurLib
import lvl_scene


pygame.init()


screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
pygame.display.set_caption("soweli li sina")
pygame.display.set_icon(pygame.image.load("images/logo.png"))
width, height = screen.get_size()
pygame.key.set_repeat(ComSurLib.style["glob_hold_del"], ComSurLib.style["glob_hold_int"])
prescene = 4
scene = -1


while True:
    evnt = pygame.event.wait(ComSurLib.style["glob_evnt_wait"])
    key = -1
    if evnt.type == pygame.QUIT: break
    elif evnt.type == pygame.NOEVENT: continue
    elif evnt.type == pygame.WINDOWSIZECHANGED: width, height = evnt.size
    elif evnt.type == pygame.KEYDOWN:
        if evnt.key in [pygame.K_SPACE, pygame.K_RETURN]: key = 0
        elif evnt.key in [pygame.K_UP, pygame.K_w]: key = 1
        elif evnt.key in [pygame.K_RIGHT, pygame.K_d]: key = 2
        elif evnt.key in [pygame.K_DOWN, pygame.K_s]: key = 3
        elif evnt.key in [pygame.K_LEFT, pygame.K_a]: key = 4
        elif evnt.key == pygame.K_r: key = 5
        elif evnt.key in [pygame.K_BACKSPACE, pygame.K_ESCAPE]: key = 6

    if scene == -1:
        prescene = scene
        scene, next = lvl_scene.frame(screen.get_size(), scene, prescene, key)
        next.blit(screen, (0, 0))
        pygame.display.update()