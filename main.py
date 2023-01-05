import pygame
#intializing
pygame.init()
#display resolution
window = pygame.display.set_mode((1080, 720))

#variable for the the loop
running = True

#background image
bg_img = pygame.image.load('pygame.jpg')
bg_img = pygame.transform.scale(bg_img,(1080,720))

while running:


    for event in pygame.event.get():
        window.blit(bg_img, (0, 0))
        if event.type == pygame.QUIT:
            running = False


        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            print("You pressed the left mouse button at (%d, %d)" % event.pos)

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:

            print("You released the left mouse button at (%d, %d)" % event.pos)

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:

            print("You pressed the right mouse button at (%d, %d)" % event.pos)

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:

            print("You released the right mouse button at (%d, %d)" % event.pos)

    pygame.display.update()
pygame.quit()


