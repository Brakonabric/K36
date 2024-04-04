import pygame
import random


class Sounds:
    def __init__(self):
        self.theme_object = None
        self.mute = False

    @staticmethod
    def button_click():
        rnd = random.randint(1, 3)
        if rnd == 1:
            button_sound_path = "assets/wav/button_a.wav"
            # button_sound_path = "wav/button_a.wav"
        elif rnd == 2:
            button_sound_path = "assets/wav/button_b.wav"
            # button_sound_path = "wav/button_b.wav"
        else:
            button_sound_path = "assets/wav/button_c.wav"
            # button_sound_path = "wav/button_c.wav"
        pygame.mixer.init()
        button_sound = pygame.mixer.Sound(button_sound_path)
        button_sound.set_volume(0.2)
        button_sound.play()
        pygame.time.wait(int(button_sound.get_length()*500))

    def main_theme(self):
        pygame.mixer.init()
        theme_sound_path = "assets/wav/mirror_theme.wav"
        # theme_sound_path = "assets/wav/mirror_theme.wav"
        theme_sound = pygame.mixer.Sound(theme_sound_path)
        theme_sound.set_volume(0.1)
        self.theme_object = theme_sound
        theme_sound.play(loops=-1)

    def main_theme_mute(self):
        self.theme_object.stop()

    def switch_mute_mode(self):
        if self.mute:
            self.theme_object.play(loops=-1)
            self.mute = False
        else:
            self.theme_object.stop()
            self.mute = True
