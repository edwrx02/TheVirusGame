'''
Created on May 14, 2015

@author: ed.quinta
'''
import pygame, sys
from pygame.locals import *
import random
from bullet import Bullet
from player import Player
from enemy import Enemy
from the_wall import Wall
from enemy2 import Enemy2
from enemy3 import Enemy3
from boom import Boom
from enemy4 import Enemy4
from bullet2 import Bullet2
from full_health import Full_Health
from health_5 import Health_5
from health_4 import Health_4
from health_3 import Health_3
from health_2 import Health_2
from health_1 import Health_1
from death_health import  Dead_Health
from boss import The_Boss
from enemy1b import Enemy1b
from enemy2b import Enemy2b
from enemy3b import Enemy3b
from enemy4b import Enemy4b
from bullet2b import Bullet2b
from boss_bullet import Boss_Bullet


def main():
    """This is the main function of the game"""
    pygame.mixer.pre_init(22050, 16, 2, 4096)
    pygame.init()
    
    """Import effect sound"""
    effect = pygame.mixer.Sound('Arcade_Explosion.wav')

    """Constants through out the game"""
    BLACK = (0, 0, 0)
    WHITE = (250, 250, 250)
    RED = (227, 66, 103)
    PURPLE = (113, 49, 153)
    WIDTH = 1440
    HEIGHT = 800
    SIZE = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(SIZE)
    
    """Initial variables for the background placement"""
    x = 0
    y = 0
    x1 = 1440
    y1 = 0
    x2 = 2880
    y2 = 0
    
    """Text used in the game"""
    pygame.display.set_caption("The Virus")
    message1 = 'READY!'
    message2 = 'SET!'
    message3 = 'GO!!!'
    message4 = 'Score:'
    message5 = 'YOU WIN!'
    message6 = 'YOU LOSE!'
    font = pygame.font.SysFont("Comic Sans MS", 200, bold=True)
    font3 = pygame.font.SysFont("Comic Sans MS", 50, bold=True)
    text1 = font.render(message1, 1, RED)
    text2 = font.render(message2, 1, RED)
    text3 = font.render(message3, 1, RED)
    text5 = font3.render(message4, 1, BLACK)
    text6 = font.render(message5, 1, RED)
    text7 = font.render(message6, 1, RED)

    
    """Pictures for background and for the menu of the game"""
    background_imgage = pygame.image.load("Bubble_2.jpg").convert()
    background_image2 = pygame.image.load("Bubble_1_red.jpg").convert()
    background_image3 = pygame.image.load("Bubble_1_orange.jpg").convert()
    menu_image = pygame.image.load("Title_Virus_BG.png")
    menu_letters = pygame.image.load("Title_Virus.png")
    quit_pill = pygame.image.load("Quit_pill.png")
    quit_pill2 = pygame.image.load("Quit_pill2.png")
    play_pill = pygame.image.load("Play_pill.png")
    play_pill2 = pygame.image.load("Play_pill2.png")

    
    """The sprite list of all the things for the game"""
    hero_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()
    block_list = pygame.sprite.Group()
    bullet_list = pygame.sprite.Group()
    hanging_list = pygame.sprite.Group()
    wall_list = pygame.sprite.Group()
    bouncing_list = pygame.sprite.Group()
    green_list = pygame.sprite.Group()
    black_list = pygame.sprite.Group()
    bad_bullet_list = pygame.sprite.Group()
    boss_list = pygame.sprite.Group()
    
    """Creates the player"""
    player = Player(200, 200)
    hero_list.add(player)
    all_sprites_list.add(player)
    
    """Creates the boss"""
    boss = The_Boss(975, 0)
    boss_list.add(boss)
    
    """Used to manage how fast the screen updates"""
    clock = pygame.time.Clock()
    
    """Variables that change through out the game"""
    background_speed = 5
    dead = False
    deadx = 0
    deady = 0
    spawn = 0
    score = 0
    bgcounter = 0
    startGame = True
    startGame2 = False
    startGame3 = False
    health = 6
    stage1 = True
    stage2 = False
    stage3 = False
    falling = 5
    boss_life = 20
    healthx = 0
    healthy = 60
    hold = 10
    
    """Creating the health bar"""
    full_health_bar = Full_Health(healthx, healthy)
    all_sprites_list.add(full_health_bar)
    bar5 = Health_5(healthx, healthy)
    bar4 = Health_4(healthx, healthy)
    bar3 = Health_3(healthx, healthy)
    bar2 = Health_2(healthx, healthy)
    bar1 = Health_1(healthx, healthy)
    bar0 = Dead_Health(healthx, healthy)

    """Creates the wall so the player won't go out of screen."""
    walls = [[0, -20, WIDTH, 20, BLACK],
            [-20, 0, 20, HEIGHT, BLACK],
            [0, 800, WIDTH, 20, BLACK],
            [1440, 0, 20, HEIGHT, BLACK]]

    for item in walls:
        wall = Wall(item[0], item[1], item[2], item[3], item[4])
        wall_list.add(wall)
        
    player.walls = wall_list    
    
    """The different formations for the enemies"""    
    green = [[1500, 50], [1500, 200], [1500, 400], [1500, 600],
             [1700, 100], [1700, 300], [1700, 500], [1700, 650]]
    
    green2 = [[1500, 25], [1575, 125], [1650, 200], [1725, 275], [1800, 350],
             [1725, 425], [1650, 500], [1575, 575], [1500, 650]]
    
    green3 = [[1500, 50], [1500, 600], [1700, 300], [1700, 500], ]
    
    green4 = [[1000, 50], [1000, 200], [1000, 400], [1000, 600],
            [1200, 100], [1200, 300], [1200, 500], [1200, 650]]
    
    green5 = [[1000, 25], [1075, 125], [1150, 200], [1225, 275], [1300, 350],
            [1225, 425], [1150, 500], [1075, 575], [1000, 650]]
    
    
      
    def main_menu():
        """The function for the main menu""" 
        intro = True
        pygame.mixer.music.load('Halo3.ogg')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.5)           
        while intro == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            screen.blit(menu_image, (0, 0))
            screen.blit(menu_letters, (200, 125))
            intro = button(play_pill, 450, 500, intro)
            button2(quit_pill, 750, 500)      
            pygame.display.update()
            clock.tick(15)
            
            
    
    def button(name, x, y, intro):
        """Function for the play button """
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        screen.blit(name, (x, y))
        if 250 + x > mouse[0] > x and y + 103 > mouse[1] > y:
            screen.blit(play_pill2, (x, y))
            if click[0] == 1:
                intro = False
        return intro
            
    def button2(name, x, y):
        """Function for the quit button """
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        screen.blit(name, (x, y))
        if 250 + x > mouse[0] > x and y + 103 > mouse[1] > y:
            screen.blit(quit_pill2, (x, y))
            if click[0] == 1:
                pygame.quit()
                quit()
        
    def enemy1_level1():
        """Function that creates enemy1 for stage 1"""
        for item in green2:
            enemy1 = Enemy(item[0], item[1])
            all_sprites_list.add(enemy1)
            green_list.add(enemy1)
            block_list.add(enemy1)
                
    def enemy4_level1():
        """Function that creates enemy4 for stage 1"""
        for item in green3:
            enemy4 = Enemy4(item[0], item[1])
            all_sprites_list.add(enemy4)
            block_list.add(enemy4)
            black_list.add(enemy4)
            
    def enemy2_level1():
        """Function that creates enemy2 for stage 1"""
        enemy2 = Enemy2()
        enemy2.rect.x = 1440
        enemy2.rect.y = -10
        hanging_list.add(enemy2)
        all_sprites_list.add(enemy2)
        
    def enemy3_level1():
        """Function that creates enemy3 for stage 1"""
        enemy3 = Enemy3()
        enemy3.rect.x = 1500
        enemy3.rect.y = 700
        bouncing_list.add(enemy3)
        all_sprites_list.add(enemy3)
        
        
    def making_bad_bullet():
        """Function that creates enemy4's bullets for stage 1"""
        for enemy4 in black_list:
            if (enemy4.rect.x == 1440 or enemy4.rect.x == 800 
                or enemy4.rect.x == 200):
                bullet2 = Bullet2()
                bullet2.rect.y = enemy4.rect.y+75
                bullet2.rect.x = enemy4.rect.x
                all_sprites_list.add(bullet2)
                bad_bullet_list.add(bullet2)
    
    def enemy1_level2():
        """Function that creates enemy1 for stage 2"""
        for item in green2:
            enemy1 = Enemy1b(item[0], item[1])
            all_sprites_list.add(enemy1)
            green_list.add(enemy1)
            block_list.add(enemy1)
                
    def enemy4_level2():
        """Function that creates enemy4 for stage 2"""
        for item in green:
            enemy4 = Enemy4b(item[0], item[1])
            all_sprites_list.add(enemy4)
            block_list.add(enemy4)
            black_list.add(enemy4)
            
    def enemy2_level2():
        """Function that creates enemy2 for stage 2"""
        enemy2 = Enemy2b()
        enemy2.rect.x = 1440
        enemy2.rect.y = -10
        hanging_list.add(enemy2)
        all_sprites_list.add(enemy2)
        
    def enemy3_level2():
        """Function that creates enemy3 for stage 2"""
        enemy3 = Enemy3b()
        enemy3.rect.x = 1500
        enemy3.rect.y = 700
        bouncing_list.add(enemy3)
        all_sprites_list.add(enemy3)
        
    def making_bad_bullet2():
        """Function that creates enemy4's bullets for stage 2"""
        for enemy4 in black_list:
            if (enemy4.rect.x == 1440 or enemy4.rect.x == 1000 
                or enemy4.rect.x == 800 or enemy4.rect.x == 500):
                bullet2 = Bullet2b()
                bullet2.rect.y = enemy4.rect.y+75
                bullet2.rect.x = enemy4.rect.x
                all_sprites_list.add(bullet2)
                bad_bullet_list.add(bullet2)
    
    def making_boss_bullet():
        """This makes 1 set of the bullets for the boss"""
        for item in green4:
            bullet2 = Boss_Bullet(item[0], item[1])
            all_sprites_list.add(bullet2)
            bad_bullet_list.add(bullet2)
            
    def making_boss_bullet2():
        """This makes the other set of bullets for the boss"""
        for item in green5:
            bullet2 = Boss_Bullet(item[0], item[1])
            all_sprites_list.add(bullet2)
            bad_bullet_list.add(bullet2)
        
    def bullet_hero(score):
        """Keeps track of the bullets and increments the score"""
        for bullet in bullet_list:
            block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
            for enemy in block_hit_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                score += 100
            if bullet.rect.x > 1440 :
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
        return score
    
    def bad_bullet():
        """Checks to see if enemy4's bullet hits the hero bullet """
        for bullet2 in bad_bullet_list:
            block_hit_list = pygame.sprite.spritecollide(bullet2, bullet_list, True)
            for bullet in block_hit_list:
                bad_bullet_list.remove(bullet2)
                all_sprites_list.remove(bullet2)
    
    
    def health_bar(num):
        """Displays the correct health bar"""
        if num == 5:
            all_sprites_list.remove(full_health_bar)
            all_sprites_list.add(bar5)
        if num == 4:
            all_sprites_list.remove(bar5)
            all_sprites_list.add(bar4)
        if num == 3:
            all_sprites_list.remove(bar4)
            all_sprites_list.add(bar3)
        if num == 2:
            all_sprites_list.remove(bar3)
            all_sprites_list.add(bar2)
        if num == 1:
            all_sprites_list.remove(bar2)
            all_sprites_list.add(bar1)
        if num == 0:
            all_sprites_list.remove(bar1)
            all_sprites_list.add(bar0)
    
    """Calls the menu function"""
    main_menu()
    
    """Stops the music for the menu"""
    pygame.mixer.music.stop()
    
    """Starts the music for the game"""
    pygame.mixer.music.load('Mega_Man.ogg')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.2)  
    
    """ -------- Main Program Loop -----------"""
    while True:
        """Event handeling"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    player.changespeed(-5, 0)
                if event.key == K_RIGHT:
                    player.changespeed(5, 0)
                if event.key == K_UP:
                    player.changespeed(0, -5)
                if event.key == K_DOWN:
                    player.changespeed(0, 5)
                if event.key == K_SPACE:
                    # Fire a bullet if the user clicks the mouse button
                    bullet = Bullet()
                    # Set the bullet so it is where the player is
                    bullet.rect.x = player.rect.x + 155
                    bullet.rect.y = player.rect.y + 75
                    # Add the bullet to the lists
                    bullet_list.add(bullet)
                    all_sprites_list.add(bullet)
 
            if event.type == KEYUP:
                if event.key == K_LEFT:
                    player.changespeed(5, 0)
                if event.key == K_RIGHT:
                    player.changespeed(-5, 0)
                if event.key == K_UP:
                    player.changespeed(0, 5)
                if event.key == K_DOWN:
                    player.changespeed(0, -5)
                    
        """Update everything before things happen"""
        all_sprites_list.update()
        
        """Stage 1 placement for enemies"""
        if stage1 == True:
            if (x == 0 or x1 == 0 or x2 == 0):
                enemy1_level1()
                
            if (x == 800 or x1 == 800 or x2 == 800):
                enemy4_level1()
         
            making_bad_bullet()       
       
            if (x == 900 or x1 == 1000 or x2 == 800): 
                enemy2_level1()
            
            if ( x == 400 or x1 == 400 or x2 == 400):
                enemy3_level1()
            
            bad_bullet()
            score = bullet_hero(score)
         
        """Stage 2 placement for enemies"""    
        if stage2 == True:
            if (x == 0 or x1 == 0 or x2 == 0):
                enemy1_level2()
                
            if (x == 800 or x1 == 800 or x2 == 800):
                enemy4_level2()
         
            making_bad_bullet2()       
       
            if (x == 900 or x1 == 1000 or x2 == 800): 
                enemy2_level2()
            
            if ( x == 400 or x1 == 400 or x2 == 400):
                enemy3_level2()
            
            bad_bullet()
            score = bullet_hero(score)
            
        """Stage 3 placement for enemies"""
        if stage3 == True:
            all_sprites_list.add(boss)
            if (x == 1000 or x1 == 1000 or x2 == 1000):
                making_boss_bullet()
            if (x == 200 or x1 == 200 or x2 == 200):
                making_boss_bullet2()
            if (x == 900 or x1 == 1000 or x2 == 800): 
                enemy2_level2()
            if ( x == 400 or x1 == 400 or x2 == 400):
                enemy3_level1()
            bad_bullet()
            """Keeps track of the score and life for the boss"""
            for boss in boss_list:
                block_hit_list = pygame.sprite.spritecollide(boss, bullet_list, True)
                for bullet in block_hit_list:
                    bullet_list.remove(bullet)
                    all_sprites_list.remove(bullet)
                    score += 100
                    boss_life -= 1
                    
        """Check to see if enemy1 kills player and if it goes out of screen"""        
        for enemy1 in green_list:
            enemy_hit_list = pygame.sprite.spritecollide(enemy1, hero_list, True)
            for player in enemy_hit_list:
                deadx = player.rect.x
                deady = player.rect.y
                effect.play()
                hero_list.remove(player)
                all_sprites_list.remove(player)
                boom = Boom(deadx, deady)
                all_sprites_list.add(boom)
                dead = True
                spawn = x - 300
                health -= 1
                health_bar(health)
                if spawn < -1440:
                    spawn = spawn + 1440
                    spawn = spawn + 2880   
            if enemy1.rect.x < -50 :
                green_list.remove(enemy1)
                all_sprites_list.remove(enemy1)
                block_list.remove(enemy1)            
        
        """Check to see if enemy2 kills player and if it goes out of screen""" 
        for enemy2 in hanging_list:
            if  enemy2.rect.x < 500:
                enemy2.falling(falling)
            hanging_hit_list = pygame.sprite.spritecollide(enemy2, hero_list, True)
            for player in hanging_hit_list:
                deadx = player.rect.x
                deady = player.rect.y
                effect.play()
                hero_list.remove(player)
                all_sprites_list.remove(player)
                boom = Boom(deadx, deady)
                all_sprites_list.add(boom)
                dead = True
                spawn = x - 300 
                health -= 1
                health_bar(health) 
                if spawn < -1440:
                    spawn = spawn + 1440
                    spawn = spawn + 2880 
            if enemy2.rect.y > 850 :
                hanging_list.remove(enemy2)
                all_sprites_list.remove(enemy2)        
         
        """Check to see if enemy3 kills player and if it goes out of screen"""        
        for enemy3 in bouncing_list:
            bouncing_hit_list = pygame.sprite.spritecollide(enemy3, hero_list, True)
            for player in bouncing_hit_list:
                deadx = player.rect.x
                deady = player.rect.y
                effect.play()
                hero_list.remove(player)
                all_sprites_list.remove(player)
                dead = True
                boom = Boom(deadx, deady)
                all_sprites_list.add(boom)
                spawn = x - 300
                health -= 1
                health_bar(health)
                if spawn < -1440:
                    spawn = spawn + 1440
                    spawn = spawn + 2880 
            if enemy3.rect.x < -50 :
                bouncing_list.remove(enemy3)
                all_sprites_list.remove(enemy3)
                block_list.remove(enemy3)
                
        """Check to see if enemy4 kills player and if it goes out of screen"""         
        for enemy4 in black_list:
            enemy_hit_list = pygame.sprite.spritecollide(enemy4, hero_list, True)
            for player in enemy_hit_list:
                deadx = player.rect.x
                deady = player.rect.y
                effect.play()
                hero_list.remove(player)
                all_sprites_list.remove(player)
                boom = Boom(deadx, deady)
                all_sprites_list.add(boom)
                dead = True
                spawn = x - 300
                health -= 1
                health_bar(health)
                if spawn < -1440:
                    spawn = spawn + 1440
                    spawn = spawn + 2880   
            if enemy4.rect.x < -50 :
                black_list.remove(enemy4)
                all_sprites_list.remove(enemy4)
                block_list.remove(enemy4)
        
        """Check to see if bullets kills player and if it goes out of screen""" 
        for bullet2 in bad_bullet_list:
            enemy_hit_list = pygame.sprite.spritecollide(bullet2, hero_list, True)
            for player in enemy_hit_list:
                deadx = player.rect.x
                deady = player.rect.y
                effect.play()
                hero_list.remove(player)
                all_sprites_list.remove(player)
                boom = Boom(deadx, deady)
                all_sprites_list.add(boom)
                dead = True
                spawn = x - 300
                health -= 1
                health_bar(health)
                if spawn < -1440:
                    spawn = spawn + 1440
                    spawn = spawn + 2880   
            if bullet2.rect.x < -50 :
                bad_bullet_list.remove(bullet2)
                all_sprites_list.remove(bullet2)
                
        """Handles the respawn for the player when dead"""
        if dead == True:
            for bullet in bullet_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
            if x == spawn:
                all_sprites_list.remove(boom)
                player = Player(0, 200)
                all_sprites_list.add(player) 
                hero_list.add(player)
                player.changespeed(0, 0)
                player.change_x = 0
                player.change_y = 0
                player.walls = wall_list
                player.update()
                dead = False
                
        """Moves the background for stage1"""
        if bgcounter <= 2: 
            screen.blit(background_imgage, (x, y))
            x -= background_speed
            screen.blit(background_imgage, (x1, y1))
            x1 -= background_speed
            screen.blit(background_imgage, (x2, y2))
            x2 -= background_speed
            if x1 == 0:
                x = 2880
                bgcounter += 1 
            if x2 == 0:
                x1 = 2880
                bgcounter += 1 
            if x == 0:
                x2 = 2880
                bgcounter += 1 
        
        """Moves the background for stage2"""        
        if 2 < bgcounter <= 5: 
            stage1 = False
            stage2 = True
            falling = 15
            screen.blit(background_image3, (x, y))
            x -= background_speed
            screen.blit(background_image3, (x1, y1))
            x1 -= background_speed
            screen.blit(background_image3, (x2, y2))
            x2 -= background_speed
            if x1 == 0:
                x = 2880
                bgcounter += 1 
            if x2 == 0:
                x1 = 2880
                bgcounter += 1 
            if x == 0:
                x2 = 2880
                bgcounter += 1       
        
        """Moves the background for stage3"""
        if 5 < bgcounter:
            stage2 = False
            stage3 = True
            screen.blit(background_image2, (x, y))
            x -= background_speed
            screen.blit(background_image2, (x1, y1))
            x1 -= background_speed
            screen.blit(background_image2, (x2, y2))
            x2 -= background_speed
            if x1 == 0:
                x = 2880
                bgcounter += 1 
            if x2 == 0:
                x1 = 2880
                bgcounter += 1 
            if x == 0:
                x2 = 2880
                bgcounter += 1       
    
        
        """Draws all the sprites"""
        all_sprites_list.draw(screen) 
        wall_list.draw(screen)
        
        """The text for the score"""
        font2 = pygame.font.SysFont("Comic Sans MS", 50, bold=True)
        text4 = font2.render(str(score), 1, WHITE)
        screen.blit(text4, (175, 0))
        screen.blit(text5, (0, 0))

        
    
        """The beginning text of the game"""
        if startGame == True:
            screen.blit(text1, (400, 200))
        if startGame == True and x == -10:    
            pygame.time.delay(1500)
            startGame = False
            startGame2 = True
        if startGame2 == True:
            screen.blit(text2, (500, 200))
        if startGame2 == True and x == -20:    
            pygame.time.delay(1500)
            startGame2 = False
            startGame3 = True
        if startGame3 == True:
            screen.blit(text3, (500, 200))
        if startGame3 == True and x == -35:    
            pygame.time.delay(1500)
            startGame3 = False
        
        """When player dies end game"""   
        if health <= 0: 
            hold -= 1
            stage1 = False
            stage2 = False
            stage3 = False
            all_sprites_list.remove(player)
            screen.blit(text7, (200, 200))
            if hold == 0:
                pygame.time.delay(1500)
                pygame.quit()
                sys.exit()
        
        """When the boss dies end the game"""
        if boss_life == 0:
            stage3 = False
            all_sprites_list.remove(boss)
            screen.blit(text6, (200, 200))
            if (x == 0 or x1 == 0 or x2 == 0):
                pygame.quit()
                sys.exit()
            
        
        """Draws everything"""
        pygame.display.flip()

        
        clock.tick(70)

if __name__ == '__main__':
    main()
