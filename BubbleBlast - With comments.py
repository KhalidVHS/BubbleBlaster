"""
568789
Abdur Khalid

This is my pygame with the name of "Bubble Blast" The goal of the game is to avoid the incoming bullets, and if you get hit by it, then the bubble pops and you lose.
Ive used many different modules in order to make the game stylistic but as simple as possible and using the least amount of lines.
If you have any questions or concerns about the program or how some of the code is constructed, then feel free to ask!
Thank you!
"""

#This imports pygame and the random function for the rectangles inital x positioning. 
import pygame , random

#This initiates the module for pygame, the font, and gets the standard fonts that are on the computer. 
pygame.init()
pygame.font.init()
pygame.font.get_fonts()

#This is the colours defined by RGB that are used later for the definitions of the colours. 
BLACK = (0,  0,  0)
WHITE  = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED  = ( 255,   0,   0)
BLUE = (0, 191, 255)
YELLOW = (227,207,87)
LIGHT_BLUE = (240,248,255)

#This is for defining the screen width and height. I assigned them to variables to make it easier to use later in the code. 
screenx = 800
screeny = 600

#This sets up the display for the screen, and sets the dimensions for the size, with the main screen surface being called "maindisplay", and the caption at the top of the program being bubble blast. 
screen_size  = (screenx,screeny)
maindisplay = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Bubble Blast")

#This loads the game icon for the program, and the wand that you see at the start of the program. 
gameIcon = pygame.image.load('bubbleblower.jpg')
bubble_blower = pygame.image.load('arcanebubbleblower.png')
pygame.display.set_icon(gameIcon)

#Setting the display with white allows for better rendering of other objects onto the screen. 
maindisplay.fill(WHITE)
pygame.display.flip()

#Setting the clock variable and then the tick sets the fps of the program. 
clock = pygame.time.Clock()
clock.tick(60)

#This is used later for the collisions of the bubble with other objects.
bubble_height = 125
bubble_width = 125

#This function takes in the parameters for the size of text, colour, what the text says, and the position.
#It basically blits text onto the main display object at the position specified before hand when its instantiated. 
def text_usage(size,colour,text,posx,posy):
    global font_used
    global text_surface
    font_used = pygame.font.SysFont('OptimusPrinceps',size)
    text_Surface = font_used.render(text,True,colour)
    maindisplay.blit(text_Surface, (posx,posy))

#This function is called when the bubble collides with one of the bullets, (Rectangles), displaying the crsah message. 
def crash():
    crashing = True  
    while crashing:
        text_usage(70,RED,"You Have Been Popped!" ,50,100)
        text_usage(70,RED,"Let the bubble blowing" ,50,200)
        text_usage(70,RED,"Continue!" ,250,300)
        pygame.display.update()
        pygame.time.delay(3000)
        game_loop()

#This loads the sprite for the bubble, which is a png file, and then states the coordinates of the bubble at x and y, determined in the game logic later on.     
def charecter(x,y):
    bubble = pygame.image.load('bubble.2.png')
    maindisplay.blit(bubble, (x,y))

#This function is for the creation of the rectangles when istantiated. 
def rectangle_creation(x_rect,y_rect,width_rect,height_rect,colour):
    pygame.draw.rect(maindisplay, colour , (x_rect,y_rect,width_rect,height_rect))

#This loads and blits the background to the maindisplay surface. 
def background():
    main_back = pygame.image.load('beach.jpg')
    maindisplay.blit(main_back,(0,0))

#This loads the music for the game, and plays it 5 times as determined within its parameters.
#I set the volume to 0.1, which is the equivalent to 10 percent. 
def background_music():
    pygame.mixer.music.load('popcorn.mp3')
    pygame.mixer.music.play(0,5)
    pygame.mixer.music.set_volume(0.1)

#The collisions between the bubbkles and the recctangles are defined here.
# It passes trhough the coordinates of the rectangle and the width and height of the bubble.
#It detects whether there is a crossover between the x and y values of the bubble and the rectangle. 
def collisions(x,y,pw,ex,ey,ew,eL):
#As the range for loop only takes in int types, I set the parameters as ints. 
    x = int(x)
    y = int(y)
    pw = int(pw)
    ex = int(ex)
    ey = int(ey)
    ew = int(ew)
    eL = int(eL)
#This first looks for whether the point of the bubble at the x is within the recctangle, then the y value, and then blits the crash message if true. 
    if ex in range(x,x+pw) and ex+ew in range(x,x+pw):
        if ey+eL >= y and ey <= y+pw:
            crash()
#This starts playing the background music.      
background_music()

#This is the main game logic for the bubble and the rectangles. 
def game_loop():
    done = False
    global rect_starty
    #Setting the starting point for the bubble. 
    x = screenx * 0.5
    y = screeny * 0.5

    #This predefines the amount of movement that occurs to the bubble. 
    x_change = 0
    y_change = 0
    #This defines the dimensions and the starting points for the rectangles. 
    rect_starty = -100
    rect_speed = 20
    rect_width = 10
    rect_height = 50

    #When the rectangle goes of screen, then the width of the rectangles increses until 250, where it resets but moves faster. 
    rectx_increase = 15

    #This is for the starting point of the three rectangles. When the rectangles goes off-screen, then it appears at a different position.  
    rect_startx = random.randint(0, screenx)
    rect_startx_second = random.randint(0, screenx)
    rect_startx_third = random.randint(0, screenx)
    #Main game loop  
    while not done:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                quit()
            #All the code below with the if statements defines the movement of the bubble by manipulating the x and y, which are the coordinates for the image.
            #If the user presses the key down for either up or down, then it increases the x and y position respectively.
            #If the user lets go of the key, I made it so the image will stop moving.(xchange = 0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -10
                if event.key == pygame.K_DOWN:
                    y_change = 10
                if event.key == pygame.K_LEFT:
                    x_change = -10
                if event.key == pygame.K_RIGHT:
                    x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        #This calls the background function and the bubble function. 
        background()
        charecter(x,y)

        #This is for the creation of the rectangles, or bullets, using the prior information of the variables. 
        rectangle_creation(rect_startx, rect_starty, rect_width, rect_height, RED)
        rectangle_creation(rect_startx_second, rect_starty, rect_width, rect_height, BLUE)
        rectangle_creation(rect_startx_third, rect_starty, rect_width, rect_height, GREEN)

        #The chunk of code below is the collision definition of each rectangle.
        #It takes in the rectangle dimensions and the bubble dimensions. 
        #collisions(x,y,pw,ex,ey,ew,eL)
        collisions(x,y,bubble_width,rect_startx,rect_starty,rect_width,rect_height)
        collisions(x,y,bubble_width,rect_startx_second,rect_starty,rect_width,rect_height)
        collisions(x,y,bubble_width,rect_startx_third,rect_starty,rect_width,rect_height)
        #This says that if the y position of the rectangle goes off the screen, then it increases the rectangle width.
        #Then, it resets the x position of the rectangle and makes it go down the screen again.
        if rect_starty > screeny:
            rect_starty  = 0 - rect_height
            rect_width += rectx_increase
            if rect_width >= 250:
                rect_width = 10
                rect_speed += 5
            rect_startx = random.randint(0, 225)
            rect_startx_second = random.randint(250, 475)
            rect_startx_third = random.randint(500, 725)
        #This adds onto the initial y position of the rectangle, giving it the movement effect.
        rect_starty += rect_speed
        pygame.display.flip()
        pygame.display.update()
        #This adds the x and y movement change to the original positioning of the bubble. 
        x += x_change
        y += y_change

        #This defines the boundries of the bubble.
        #If it goes past the left and right side, then it makes it equal to the edge.
        #The same is true for the top and bottom. 
        if x <=0:
            x = 0
        if x >= screenx - bubble_width:
            x = screenx - bubble_width
        if y <=0:
            y = 0
        if y >= screeny - bubble_height:
            y = screeny - bubble_height
        clock.tick(60)
#The function below is for the start screen that you see for the play and quit button.         
def game_intro():
    pygame.font.get_default_font()
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                quit()

        #Getting the mouse position is vital for checking whether the mouse position is within the button boundries. 
        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()
        background()

        #This puts the starting messages onto the screen. 
        text_usage(65,BLACK,"Bubble Blast",240,200)
        text_usage(40,BLACK,"PLAY",250,300)
        text_usage(40,BLACK,"QUIT",475,300)

        #This puts the arcane blowing wand onto the screen. 
        maindisplay.blit(bubble_blower,(304,361))

        #As the position of the mouse is a tuple, with index 0 being x and 1 being the y, I can say that
        #If the x and y of the mouse is within a certain area of pixels on the screen, then run the block below.
        #If my mouse is within those boundries and I were to click, then it either runs the game, or it quits the game depending on whether you click play or quit. 
        if 250 < mouse[0] < 250 + 100 and 300 < mouse[1] < 300 + 50:
            if clicked[0] == 1:
                game_loop()

        if 475 < mouse[0] < 475 + 100 and 300 < mouse[1] < 300 + 50:
            if clicked[0] == 1:
                pygame.quit()
                quit()
                
        pygame.display.update()
#This calls for the start of the game intro. As the game loop only runs after I click on the play button during the start screen, I only have to call the intro. 
game_intro()        







