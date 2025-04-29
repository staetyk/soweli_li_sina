import pygame
import ComSurLib
import lvl_scene
import sel_scene
import csv


pygame.init()


demo = True


screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
pygame.display.set_caption("soweli li sina")
pygame.display.set_icon(pygame.image.load("images/logo.png"))
width, height = screen.get_size()
pygame.key.set_repeat(ComSurLib.style["glob_hold_del"], ComSurLib.style["glob_hold_int"])
pygame.event.set_blocked([pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.KEYUP])
clock = pygame.time.Clock()
pygame.mixer.init()


prescene = 4
scene = 2

i = 0
last = clock.get_time()

while True:
    ComSurLib.load()
    evnt = pygame.event.wait(ComSurLib.style["glob_frame"])
    
    
    if pygame.event.peek():
        post = pygame.event.poll()
        pygame.event.clear()
        pygame.event.post(post)
    else: pygame.event.clear()
    
    
    key = -1
    if evnt.type == pygame.QUIT: break
    elif evnt.type == pygame.NOEVENT: continue
    elif evnt.type == pygame.WINDOWSIZECHANGED: width, height = evnt.size
    elif evnt.type == pygame.event.Event(pygame.USEREVENT + 1): key = -1
    elif evnt.type == pygame.KEYDOWN:
        if evnt.key in [pygame.K_SPACE, pygame.K_RETURN]: key = 0
        elif evnt.key in [pygame.K_UP, pygame.K_w]: key = 1
        elif evnt.key in [pygame.K_RIGHT, pygame.K_d]: key = 2
        elif evnt.key in [pygame.K_DOWN, pygame.K_s]: key = 3
        elif evnt.key in [pygame.K_LEFT, pygame.K_a]: key = 4
        elif evnt.key == pygame.K_r: key = 5
        elif evnt.key in [pygame.K_BACKSPACE, pygame.K_ESCAPE]:
            prescene, scene = scene, 2
            pygame.event.post(pygame.event.Event(pygame.USEREVENT + 1))
            continue
        elif demo and evnt.key == pygame.K_n:
            ComSurLib.newsave(False)
            prescene, scene = 4, 2
            continue
        elif demo and evnt.key == pygame.K_f:
            sel_scene.init()
            ComSurLib.save(sel_scene.num)
            prescene, scene = 4, 2
    pygame.event.pump()

    if scene == -1:
        new, nextS = lvl_scene.frame(screen.get_size(), scene, prescene, key, ComSurLib.plus)
        prescene, scene = scene, new
        screen.blit(nextS, (0, 0))
        pygame.display.flip()

    elif int(scene) == 0:
        new, nextS = lvl_scene.frame(screen.get_size(), scene, prescene, key, ComSurLib.plus)
        if nextS == None:
            pygame.event.post(pygame.event.Event(pygame.USEREVENT + 1))
            continue
        prescene, scene = scene, new
        screen.blit(nextS, (0, 0))
        pygame.display.flip()
        if int(scene) == 3:
            ComSurLib.save(int(prescene * 100) + 1)

    else:
        try: pygame.mixer.music.stop()
        except: pass

    if scene == 2:
        new, nextS = sel_scene.frame(screen.get_size(), prescene, key)
        prescene, scene = scene, new
        if nextS is not None:
            screen.blit(nextS, (0, 0))
            pygame.display.flip()
        else:
            pygame.event.post(pygame.event.Event(pygame.USEREVENT + 1))

    elif int(scene) == 3:
        scene = 2
        pygame.event.post(pygame.event.Event(pygame.USEREVENT + 1))