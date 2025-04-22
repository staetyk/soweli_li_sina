import pygame
import ComSurLib
import level_lib
from math import *
from typing import Optional


def frame(dim: tuple[int, int], Sc: float, preSc: float, key: int, plus: bool) -> tuple[float, Optional[pygame.Surface]]:
    if Sc != preSc or key == 5:
        PostSc = Sc
        index = (5 if Sc == -1 else int(Sc * 100))
        if level_lib.init(index):
            return (2, None)
        try: pygame.mixer.music.load("sounds/lape_sona.mp3")
        except: pass
        else:
            pygame.mixer.music.set_volume(ComSurLib.settings["Music"] / ComSurLib.style["glob_vol_mus"] * ComSurLib.settings["Master"] / ComSurLib.style["glob_vol_main"])
            pygame.mixer.music.play()
        """else:
            if Sc != preSc:
                pygame.mixer.music.play(loops = -1, fade_ms = ComSurLib.style["glob_fade_dur"])
            else:
                pygame.mixer.music.fadeout(ceil(ComSurLib.style["glob_fade_dur"] / 2))
                pygame.mixer.music.play(loops = -1, fade_ms = ComSurLib.style["glob_fade_dur"] // 2)"""
                
    elif 0 <= key <= 4:
        win, sound = level_lib.step(key - 1)
        if sound:
            try: sfx = pygame.mixer.Sound(f"sounds/{0}.mp3".format(["pass", "move", "push", "fail", "trans", "lock", "die", "win"][sound - 1]))
            except: pass
            else:
                sfx.set_volume(ComSurLib.settings["SFX"] / ComSurLib.style["glob_vol_sfx"] * ComSurLib.settings["Master"] / ComSurLib.style["glob_vol_main"])
                sfx.play()
            
        if win & (Sc != -1): PostSc = 3 + Sc
        else: PostSc = Sc
    elif key == 6: PostSc = Sc + 1
    else: PostSc = Sc
    
    show = pygame.Surface((int(level_lib.width * 140 + (level_lib.width + 1) * 140 * ComSurLib.style["lvl_grid_wid"]), int(level_lib.height * 140 + (level_lib.height + 1) * 140 * ComSurLib.style["lvl_grid_wid"])))
    show.fill(ComSurLib.style["lvl_grid_col"])
    for i in range(level_lib.height):
        for j in range(level_lib.width):
            x = j * int(140 + ComSurLib.style["lvl_grid_wid"] * 140) + ComSurLib.style["lvl_grid_wid"] * 140
            y = i * int(140 + ComSurLib.style["lvl_grid_wid"] * 140) + ComSurLib.style["lvl_grid_wid"] * 140
            show.fill(ComSurLib.style["lvl_in_bg"], (x, y, 140, 140))
            if len(level_lib.map[level_lib.toi(j, i)]) > 0:
                for k in level_lib.map[level_lib.toi(j, i)]:
                    show.blit(k.draw(plus), (x, y, 140, 140))

    out = pygame.Surface(dim)
    out.fill(ComSurLib.style["lvl_out_bg"])
    if (dim[0] / show.get_width()) * show.get_height() > dim[1]: show = pygame.transform.scale(show, ((dim[1] / show.get_height()) * show.get_width(), dim[1]))
    else: show = pygame.transform.scale(show, (dim[0], (dim[0] / show.get_width()) * show.get_height()))
    out.blit(show, ((dim[0] - show.get_width()) // 2, (dim[1] - show.get_height()) // 2))
    return (PostSc, out) # type: ignore