import pygame
import random


class Sounds:
    def __init__(self):
        self.background_sound = None
        self.mute = False

    @staticmethod
    def button_click():
        rnd = random.randint(1, 3)
        pygame.mixer.init()
        if rnd == 1:
            button_sound_path = "assets/ogg/button_a.ogg"
        elif rnd == 2:
            button_sound_path = "assets/ogg/button_b.ogg"
        else:
            button_sound_path = "assets/ogg/button_c.ogg"
        button_sound = pygame.mixer.Sound(button_sound_path)
        button_sound.set_volume(0.25)
        button_sound.play()
        pygame.time.wait(int(button_sound.get_length() * 500))

    @staticmethod
    def play_fx(name):
        if name == "transition":
            fx_path = "assets/ogg/transition.ogg"
            transition = pygame.mixer.Sound(fx_path)
            transition.set_volume(0.6)
            transition.play()
        elif name == "error":
            fx_path = "assets/ogg/error.ogg"
        elif name == "end_win":
            fx_path = "assets/ogg/end_win.ogg"
        elif name == "end_defeat":
            fx_path = "assets/ogg/end_defeat.ogg"
        elif name == "end_draw":
            fx_path = "assets/ogg/end_draw.ogg"
        else:
            fx_path = "assets/ogg/off.ogg"
            off = pygame.mixer.Sound(fx_path)
            off.set_volume(0.25)
            off.play()
            pygame.time.wait(int(off.get_length() * 1000))
        fx_sound = pygame.mixer.Sound(fx_path)
        fx_sound.set_volume(0.4)
        fx_sound.play()

    def play_theme(self, theme):
        self.stop_theme()
        pygame.mixer.init()
        if theme == "main":
            theme_sound_path = "assets/ogg/main_theme.ogg"
        elif theme == "game":
            theme_sound_path = "assets/ogg/game_theme.ogg"
        else:
            theme_sound_path = "assets/ogg/end_theme.ogg"

        theme_sound = pygame.mixer.Sound(theme_sound_path)
        if self.mute:
            theme_sound.set_volume(0)
        else:
            theme_sound.set_volume(0.25)
        self.background_sound = theme_sound
        theme_sound.play(loops=-2)

    def stop_theme(self):
        if self.background_sound is not None:
            self.background_sound.stop()

    def switch_mute_mode(self):
        if self.mute:
            self.background_sound.set_volume(0.25)
            self.mute = False
        else:
            self.background_sound.set_volume(0)
            self.mute = True
        return self.mute

    def get_mute_flag(self):
        return self.mute
