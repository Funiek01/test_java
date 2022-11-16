import pygame
from sys import exit


#starting variables
pygame.init() #initialize the pygame
screen = pygame.display.set_mode((1200, 600)) #display for game
pygame.display.set_caption("Mario") #name of our game/window
clock = pygame.time.Clock() #minimum framerate
test_font = pygame.font.Font("localization", 50) #localization file and size of graphic on the screen

#test_surface = pygame.Surface((100,200)) #first image
#test_surface.fill("Red") # set colour of image
sky_surface = pygame.image.load("mario_image/background.png").convert() # convert to make pygame faster
ground_surface = pygame.image.load("mario_image/ground.png").convert_alpha() # dodge alpha error 
text_surface = test_font.render("Mario by Funiek", True, "Black")

mario_surface = pygame.image.load("mario_image/mario.png").convert_alpha # alpha because of the white background
mario_surface = pygame.transform.smoothscale(mario_surface, (30,60)) #resize the image of mario
mario_x_pos = 600


# player_surf = pygame.image.load("mar")

while True: # draw all of out elements and update
    for event in pygame.event.get(): # all of the events included
        if event.type == pygame.QUIT:
            pygame.quit() #exit button
            exit() # escape from error


    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,0))
    screen.blit(text_surface, (400,50))
    mario_x_pos -= 4
    if mario_x_pos <= -100:
        mario_x_pos = 1200
    screen.blit(mario_surface, (mario_x_pos, 445))

    pygame.display.update()
    clock.tick(60)