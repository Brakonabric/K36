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
            button_sound_path = "assets/wav/button_a.wav"
        elif rnd == 2:
            button_sound_path = "assets/wav/button_b.wav"
        else:
            button_sound_path = "assets/wav/button_c.wav"
        button_sound = pygame.mixer.Sound(button_sound_path)
        button_sound.set_volume(0.2)
        button_sound.play()
        pygame.time.wait(int(button_sound.get_length() * 500))

    @staticmethod
    def play_fx(name):
        if name == "transition":
            fx_path = "assets/wav/transition.wav"
        elif name == "error":
            fx_path = "assets/wav/error.wav"
        elif name == "end_win":
            fx_path = "assets/wav/end_win.wav"
        elif name == "end_defeat":
            fx_path = "assets/wav/end_defeat.wav"
        elif name == "end_draw":
            fx_path = "assets/wav/end_draw.wav"
        elif name == "on":
            fx_path = "assets/wav/on.wav"
        elif name == "set":
            fx_path = "assets/wav/set.wav"
        else:
            fx_path = "assets/wav/off.wav"
            off = pygame.mixer.Sound(fx_path)
            off.set_volume(0.2)
            off.play()
            pygame.time.wait(int(off.get_length() * 1000))
        fx_sound = pygame.mixer.Sound(fx_path)
        fx_sound.set_volume(0.2)
        fx_sound.play()

    def play_theme(self, theme):
        self.stop_theme()
        pygame.mixer.init()
        if theme == "main":
            theme_sound_path = "assets/wav/main_theme.wav"
        elif theme == "game":
            theme_sound_path = "assets/wav/game_theme.wav"
        else:
            theme_sound_path = "assets/wav/end_theme.wav"

        theme_sound = pygame.mixer.Sound(theme_sound_path)
        if self.mute:
            theme_sound.set_volume(0)
        else:
            theme_sound.set_volume(0.1)
        self.background_sound = theme_sound
        theme_sound.play(loops=-2)

    def stop_theme(self):
        if self.background_sound is not None:
            self.background_sound.stop()

    def switch_mute_mode(self):
        if self.mute:
            self.background_sound.set_volume(0.1)
            self.mute = False
        else:
            self.background_sound.set_volume(0)
            self.mute = True
        return self.mute

    def get_mute_flag(self):
        return self.mute
