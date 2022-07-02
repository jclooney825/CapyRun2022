import pygame 
from capy import Capy
from settings import Settings
from points import Points 
from rock import Rock
import random 
from pelican import Pelican

def main():

    lost_count = 0
    pygame.init()

    clock = pygame.time.Clock()

    settings = Settings()
    
    font = pygame.font.Font('fonts/ARCADECLASSIC.TTF', 35)

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    
    sky = pygame.image.load('images/sky.png').convert()
    sky = pygame.transform.scale(sky, (settings.screen_width, 200))

    trees = pygame.image.load('images/trees.png').convert()
    trees = pygame.transform.scale(trees, (settings.screen_width, 80))

    ground = pygame.image.load('images/ground.png').convert()
    ground = pygame.transform.scale(ground, (settings.screen_width, 100))

    i = 0 

    capy = Capy(50)
    rocks = [] 
    points = [] 
    pelicans = [] 

    start_time = pygame.time.get_ticks() 
    ptime  =  pygame.time.get_ticks() 
    ground_speed = settings.ground_speed
    
    pygame.mixer.music.load('sound/Friends.ogg')
    pygame.mixer.music.play(-1)

    rock_types = ['rock1', 'rock2', 'rock3']
    lost = False
    running = True
    while running:  

        clock.tick(settings.fps)

        # Draw background
        screen.fill((100,100,0))
        screen.blit(sky,(0, 0))
        screen.blit(trees,(i, 197))
        screen.blit(trees,(settings.screen_width + i - 3, 197))
        screen.blit(ground,(0, 300))
        
        i -= 1
        if (i == -settings.screen_width):
            screen.blit(trees,(settings.screen_width + i - 3, 197))
            i=0

        now = pygame.time.get_ticks() 

        if now - start_time > settings.rock_freq:
            rock = Rock(settings.off_screen, random.choice(rock_types))
            rocks.append(rock)
            x = random.randint(125, 400)
            if random.random() > 0.8:

                point = Points(settings.off_screen + x, 'watermelon')
                points.append(point)
            else:
                point = Points(settings.off_screen + x, 'orange')
                points.append(point)
            
            start_time = now

        idk = pygame.time.get_ticks() 
        if idk - ptime > 5000 and random.random() > 0.7:
            pelican = Pelican(settings.off_screen + random.randint(50, 200))
            pelicans.append(pelican)
            ptime = idk 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    capy.jump() 

        for rock in rocks[:]:
            rock.blit_me(screen)
            rock.move(ground_speed)
            rock.collision(capy)
            if rock.off_screen():
                rocks.remove(rock)

        for point in points[:]:
            point.blit_me(screen)
            point.move(ground_speed)
            point.collision(capy)
            if point.off_screen():
               points.remove(point)

        for pelican in pelicans[:]:
            pelican.blit_me(screen)
            pelican.move(ground_speed)
            pelican.collision(capy)
            if pelican.off_screen():
               pelicans.remove(pelican)

        # capy functions
        capy.blit_me(screen)
        capy.move()
        
        if capy.lives < 1:
            game_over = font.render(f'Game Over', 10, (255,255,255))
            screen.blit(game_over, (settings.screen_width/2 - 75, 150))
            pygame.mixer.music.stop()
            pygame.time.delay(1000)
            main()

        life_label = font.render(f'Lives  {capy.get_lives()}', 1, (255,255,255))
        score_label = font.render(f'Score   {capy.points_earned}', 1, (255,255,255))

        screen.blit(life_label, (25, settings.screen_height - 50))
        screen.blit(score_label, (settings.screen_width/2 - score_label.get_width()/2, 10))

        pygame.display.flip()
    pygame.quit()
    

if __name__ == '__main__':
    main()