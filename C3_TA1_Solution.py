# Importing pygame library
import pygame
# Initialzing pygame
pygame.init() 
# Creating a game screen with width=600 and height=600
screen = pygame.display.set_mode((600,600))
# Setting the title of the game screen to "Breakout Game" 
pygame.display.set_caption("Breakout Game")
# Creating a paddle and a ball rectangle objects
paddle = pygame.Rect(300,500,60,10)
ball = pygame.Rect(200,250,10,10)
# Creating variables "ballx" and "bally" and assigning the value 1 to both
ballx = -1
bally = -1
# Creating "paddlex" to track paddle movement and assigning a value 2 to it.
paddlex = 2
# Game loop
carryOn = True
while carryOn:
    for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # Checking if user clicked on close on game screen
                  carryOn = False # Flag that we are done so we exit this loop  
    # Filling the screen with darkblue color. RGB combination for darkblue is (36,90,190)                
    screen.fill((36,90,190))

    if event.type == pygame.KEYDOWN: # Checking if a key is pressed  
        if event.key == pygame.K_RIGHT: # Checking if key pressed is right key
            if paddle.x < 540:# Checking if paddle's x-coordinate is within screen boundary 
                paddle.x += paddlex # Update paddle position by the value in 'paddlex'
            
    # Drawing the lightblue colored paddle on screen. RGB combination for lightblue is (0,176,240)
    pygame.draw.rect(screen,(0,176,240),paddle)
    # Updating the x and y position of the ball on screen by 1 unit
    ball.x = ball.x + ballx
    ball.y = ball.y + bally
    
    # Limiting ball movement on screen along x-axis
    if ball.x >= 590:
      ballx = -ballx
    if ball.x <= 10:
      ballx = -ballx
    # Limiting ball movement on screen along y-axis 
    if ball.y >= 590:
      bally = -bally
    if ball.y <= 10:
      bally = -bally
    
    # Checking for paddle and ball collision
    if paddle.collidepoint(ball.x, ball.y):
        bally = -bally # If collision has happened change ball direction 
   
    # Drawing the white colored ball on screen. RGB combination for white is (255,255,255)  
    pygame.draw.rect(screen,(255,255,255) ,ball)
    # Update x and y positions of the ball every 20 milliseconds.    
    pygame.time.wait(15) # Adding this will enable us to monitor the speed with which ball moves.
    # Update the contents of entire display
    pygame.display.flip()
# Quit the game    
pygame.quit()
