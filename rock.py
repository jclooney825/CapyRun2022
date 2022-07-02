import pygame 
from settings import Settings

settings = Settings()

class Rock(pygame.sprite.Sprite):

    def __init__(self, x, type):
        super(Rock, self).__init__()
        self.x = x 
        self.y = settings.ground_level + 20

        self.hit = False 

        self.objs = {'rock1': [5, 'images/rock1.png', 120, 60], 
                    'rock2': [25, 'images/rock2.png', 110, 60],
                    'rock3': [25, 'images/rock3.png', 140, 60]
                    }

        self.points, self.fruit_image, self.size_x, self.size_y = self.objs[type]
        self.image = pygame.image.load(self.fruit_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size_x, self.size_y))

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = self.y

        self.mask = pygame.mask.from_surface(self.image)

    def blit_me(self, screen):
        screen.blit(self.image, (self.x,self.y))    
    
    def move(self, ground_speed):
        self.x -= ground_speed
        self.rect.centerx = self.x
    
    def collision(self, capy):
        hits = pygame.sprite.collide_mask(capy, self)
        if hits and self.hit == False:
            self.hit = True
            hurt_sound = pygame.mixer.Sound('sound/capy_hurt.mp3')
            pygame.mixer.Sound.play(hurt_sound)
            capy.lives -= 1
    
    def off_screen(self):
        if self.x < settings.screen_width - self.size_x:
            return False