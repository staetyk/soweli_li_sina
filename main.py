import pygame
import ComSurLib
import lvl_scene


pygame.init()


screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
pygame.display.set_caption("soweli li sina")
pygame.display.set_icon(pygame.image.load("images/logo.png"))
width, height = screen.get_size()
pygame.key.set_repeat(ComSurLib.style["glob_hold_del"], ComSurLib.style["glob_hold_int"])
pygame.event.set_blocked([pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.KEYUP])
clock = pygame.time.Clock()
pygame.mixer.init()

prescene = 4
scene = -1

i = 0
last = clock.get_time()

while True:
    i += 1
    clock.tick()
    evnt = pygame.event.wait(ComSurLib.style["glob_frame"])
    between, last = clock.get_time() - last, clock.get_time()
    print(i, clock.get_fps(), between, sep = " | ")
    
    """
    if pygame.event.peek():
        post = pygame.event.poll()
        pygame.event.clear()
        pygame.event.post(post)
    else: pygame.event.clear()
    """
    
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
    print(key)
    pygame.event.pump()

    if scene == -1:
        new, next = lvl_scene.frame(screen.get_size(), scene, prescene, key)
        prescene, scene = scene, new
        screen.blit(next, (0, 0))
        pygame.display.flip()

    elif int(scene) == 0:
        new, next = lvl_scene.frame(screen.get_size(), scene, prescene, key)
        prescene, scene = scene, new
        screen.blit(next, (0, 0))
        pygame.display.flip()

    else:
        try: pygame.mixer.music.fadeout(ComSurLib.style["glob_fade_dur"])
        except: pass