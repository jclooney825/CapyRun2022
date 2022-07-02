import pygame 
from settings import Settings

settings = Settings()

class Points(pygame.sprite.Sprite):

    def __init__(self, x, type):
        super(Points, self).__init__()
        self.x = x 
        self.y = settings.ground_level

        self.hit = False 

        self.objs = {'orange': [5, 'images/orange.png', 40, 40], 
                    'watermelon': [25, 'images/watermelon.png', 60, 40]
                    }

        self.points, self.fruit_image, self.size_x, self.size_y = self.objs[type]
        self.image = pygame.image.load(self.fruit_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, ( self.size_x, self.size_y))

        self.up_speed = 0.5
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = self.y

    def blit_me(self, screen):
        if self.hit == False:
            screen.blit(self.image, (self.x,self.y))    
    
    def move(self, ground_speed):   

        self.y += self.up_speed
        if self.y > settings.ground_level + 20:
            self.up_speed *= -1 
        elif self.y < settings.ground_level - 10:
            self.up_speed *= -1 

        self.x -= ground_speed
        self.rect.centerx = self.x
    
    def collision(self, capy):
        hits = pygame.sprite.collide_mask(capy, self)
        if hits and self.hit == False:
            self.hit = True
            bite_sound = pygame.mixer.Sound('sound/aud_chomp.mp3')
            pygame.mixer.Sound.play(bite_sound)
            capy.points_earned += self.points

    def off_screen(self):
        if self.x < settings.screen_width - self.size_x:
            return False