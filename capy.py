import pygame 
from settings import Settings

settings = Settings()

class Capy(pygame.sprite.Sprite):
    
    def __init__(self, x):
        super(Capy, self).__init__()
        self.x = x 
        self.y = settings.ground_level 
        
        self.lives = 3
        self.points_earned = 0 

        self.jump_count = 0 
        self.angle = 0 

        self.time = pygame.time.get_ticks() 
        self.index = 0 
        images = ["images/capy.png", "images/capy_running.png"]
        self.capy_images = [] 
        for image in images:
            image = pygame.image.load(image).convert_alpha()
            image = pygame.transform.scale(image, (settings.capy_length, settings.capy_height))
            self.capy_images.append(image)

        self.rect = self.capy_images[self.index].get_rect()
        self.rect.centerx = x
        self.rect.centery = self.y
        self.mask = pygame.mask.from_surface(self.capy_images[self.index])

        self.image = self.capy_images[self.index]
        self.speed = 0

    def blit_me(self, screen):
        screen.blit(self.capy_images[self.index], (self.x,self.y)) 
    
    def move(self):
        
        if self.rect.centery < 0:
            self.speed = 0 
            self.y = 0 
            self.rect.centery = self.y

        elif self.rect.centery >= settings.ground_level:
            self.speed = 0 
            self.y = settings.ground_level
            self.rect.centery = self.y
        else:
            self.speed += settings.gravity 
            self.y += 0.25*self.speed
            self.rect.centery = self.y 

        time_now = pygame.time.get_ticks() 
        if time_now - self.time > 150:
            if self.index == 1:
                self.index = 0 
            elif self.index == 0:
                self.index = 1 
            self.time = time_now        
        
        if self.is_on_ground():
            self.jump_count = 0
        elif self.jump_count == 1:
            self.index = 1 
        else:
            self.index = 0     

    def jump(self):
        if self.jump_count < 2:
            if self.jump_count == 0:
                jump1_sound = pygame.mixer.Sound('sound/jump_02.wav')
                pygame.mixer.Sound.play(jump1_sound)
            elif self.jump_count == 1:
                jump2_sound = pygame.mixer.Sound('sound/jump_03.wav')
                pygame.mixer.Sound.play(jump2_sound)
                
            self.speed = 0 
            self.speed -= settings.jump_speed
            self.y += self.speed
            self.rect.centery = self.y
            self.jump_count += 1 

    def is_on_ground(self):
        if self.y == settings.ground_level:
            return True 
        else:
            return False

    def get_lives(self):
        return self.lives