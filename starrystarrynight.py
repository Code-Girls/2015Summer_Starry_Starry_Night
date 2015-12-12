
# 1 - Import library
import pygame
from pygame.locals import *
import math
import random

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
# badguys = [[200,60],[380,60],[200,240],[380,240],[290,60],[380,150],[290,240],[200,150]]
badguys = [0,math.pi/2,math.pi,math.pi*3/2]
goodguys = [320,410]

pygame.mixer.init()

# 3 - Load image
badguyimg = pygame.image.load("resources/images/star.png")
grass = pygame.image.load("resources/images/starrynight.png")


gameover = pygame.image.load("resources/images/gameover.png")


# 3.1 - Load audio
shoot = pygame.mixer.Sound("resources/audio/up1.wav")
shoot.set_volume(1.00)
pygame.mixer.music.load('resources/audio/somewhere.mp3')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.6) 


# 4 - keep looping through
count = 0
# time = 0
# step = 0
running = 1
level = "infant"
level_num = 1
angle = math.pi/720

while running:
    # time += 1
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the player on the screen at X:100, Y:100
    screen.blit(grass,[0,0])
    
    #draw badguys
    for i in range(0,len(badguys)):
        screen.blit(badguyimg,[320+150*math.sin(badguys[i]),160+150*math.cos(badguys[i])])
        badguys[i] += angle   

    #draw goodguys
    screen.blit(badguyimg,[goodguys[0],goodguys[1]])

    # draw count
    font = pygame.font.Font(None,24)
    counttext = font.render("Count: "+str(count),True, (192,192,192))
    textRect = counttext.get_rect()
    textRect.topleft = [20,40]
    screen.blit(counttext,textRect)

    font = pygame.font.Font(None,24)
    counttext2 = font.render("Level: "+str(level),True, (192,192,192))
    textRect2 = counttext2.get_rect()
    textRect2.topleft = [20,20]
    screen.blit(counttext2,textRect2)


    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type==pygame.MOUSEBUTTONDOWN:
            shoot.play()
            index = 0
            
            goodguysrect = pygame.Rect(badguyimg.get_rect())
            goodguysrect.left = goodguys[0]
            goodguysrect.top = goodguys[1] - 100
            
            for badguy in badguys:
                badguyrect = pygame.Rect(badguyimg.get_rect())
                badguyrect.left =320+150*math.sin(badguy)
                badguyrect.top = 160+150*math.cos(badguy)
                if badguyrect.colliderect(goodguysrect):
                    
                    
                    running = 0
                    
                        
            # all the badguys donot meet the goodguy,add to the badguys queue,and delete it from the goodguys queue         
            if running == 1:
                badguys.append(0)  
                count += 1
                if count % 3 == 0:
                    
                    # angle +=  math.pi/720
                    level_num += 1
                    if level_num%2 == 0:
                        angle = -(abs(angle)+math.pi/720)
                    elif level_num%2 ==1:
                        angle = abs(angle)+math.pi/720
                    if level == "infant":
                        level = "teenager"
                    elif level == "teenager":
                        level ="adult"
                    elif level == "adult":
                        level = "the aged"
                    elif level =="the aged":
                        level = "celestial being"
                    
                    
    
#win or lose display
if running == 0:
    
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Count: "+str(count),True, (133,223,123))
    textRect = text.get_rect()
    textRect.topleft = [20,230]
    # textRect.centerx = screen.get_rect().centerx
    # textRect.centery = screen.get_rect().centery+24

    text2 = font.render("Level: "+str(level),True,(133,223,123))
    textRect2 = text2.get_rect()
    textRect2.topleft = [20,200]
    

    screen.blit(gameover, (0,0))
    screen.blit(text, textRect) 
    screen.blit(text2,textRect2)
    
    
    
while 1:
    pygame.mixer.music.set_volume(0.2) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            
    pygame.display.flip()
    

             
        
