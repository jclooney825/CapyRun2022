import pygame 
from settings import Settings

settings = Settings()

class Pelican(pygame.sprite.Sprite):
    
    def __init__(self, x):
        super(Pelican, self).__init__()
        self.x = x 
        self.y = 200
        
        self.hit = False

        self.time = pygame.time.get_ticks() 
        self.index = 0 
        images = ["images/pelican.png", "images/pelican_flying.png"]
        self.pelican_images = [] 
        for image in images:
            image = pygame.image.load(image).convert_alpha()
            image = pygame.transform.scale(image, (50, 50))
            self.pelican_images.append(image)

        self.rect = self.pelican_images[self.index].get_rect()
        self.rect.centerx = x
        self.rect.centery = self.y
        self.mask = pygame.mask.from_surface(self.pelican_images[self.index])

        self.image = self.pelican_images[self.index]
        self.speed = 5

    def blit_me(self, screen):
        screen.blit(self.pelican_images[self.index], (self.x,self.y)) 
    
    def move(self, ground_speed):
        self.x -= 1.3*ground_speed
        self.rect.centerx = self.x

        time_now = pygame.time.get_ticks() 
        if time_now - self.time > 200:
            if self.index == 1:
                self.index = 0 
            elif self.index == 0:
                self.index = 1 
            self.time = time_now        
        
    def collision(self, capy):
        hits = pygame.sprite.collide_mask(capy, self)
        if hits and self.hit == False:
            self.hit = True
            hurt_sound = pygame.mixer.Sound('sound/capy_hurt.mp3')
            pygame.mixer.Sound.play(hurt_sound)
            capy.lives -= 1

    def off_screen(self):
        if self.x < settings.screen_width - 50:
            return False
