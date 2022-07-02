import pygame 


class Settings:

    def __init__(self):
        self.screen_width, self.screen_height = 1000, 400
        self.fps = 60
    

        # Dimensions of capy image
        self.capy_length = 90 
        self.capy_height = 65

        self.ground_level = 280

          # Game settings
        self.gravity = 1.5
        self.jump_speed = 20
        self.ground_speed = 4 
        self.rock_freq = 2000

        self.off_screen = self.screen_width


        