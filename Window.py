import pygame

pygame.init()



#Colors

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED   = (255, 0, 0)

#Numeric Constants
PI = 3.141592653

#Screen parameters
size = (700,500)
pygame.display.set_caption("Test")



screen = pygame.display.set_mode(size)


#Game clock parameters
done = False
clock = pygame.time.Clock()


while not done:
    
    #Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            print("User Exited the program.")
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            print("User Pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User released a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
            
#Clear Screen
    screen.fill(WHITE)
# Draw on the screen several lines from (0, 10) to (100, 110)
# 5 pixels wide using a while loop
    y_offset = 0
    while y_offset < 1000:
        pygame.draw.line(screen,RED,[0,10+y_offset],[100,110+y_offset],5)
        y_offset = y_offset + 10
#Update Screen
    pygame.display.flip()

    clock.tick(60)

    
    
