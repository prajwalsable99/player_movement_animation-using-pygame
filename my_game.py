
import time
# Import and initialize the pygame library
import pygame
from pygame.locals import *
pygame.init()
pygame.display.set_caption('my game')
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
screen_w=800
screen_h=600
screen_size=[screen_w,screen_h]

screen = pygame.display.set_mode(screen_size)


#grid
def drawGrid():
    screen.fill(WHITE)
    blockSize = 20 #Set the size of the grid block
    for x in range(0, screen_w, blockSize):
        for y in range(0, screen_h, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)


            pygame.draw.rect(screen, BLACK, rect, 1)



# road

road_h=100

img= pygame.image.load('bg1.jpg').convert_alpha()
img = pygame.transform.smoothscale(img, (screen_w, road_h)) 

# bg 
img2= pygame.image.load('bg2.png').convert_alpha()
img2 = pygame.transform.smoothscale(img2, (screen_w, screen_h-road_h)) 


#title
# heading= pygame.image.load('wallpaper.jpg').convert_alpha()
# heading= pygame.transform.smoothscale(heading, (200, 100)) 

# hero
hero_size=80
h_x=0
h_y=screen_h-road_h-hero_size



mov_x=0
mov_y=0

left=False
right=False

right_walks=['walking\walk_ (1).png','walking\walk_ (2).png','walking\walk_ (3).png','walking\walk_ (4).png','walking\walk_ (5).png','walking\walk_ (6).png','walking\walk_ (7).png','walking\walk_ (8).png']

left_walks=['walkingop\left_1.png','walkingop\left_2.png','walkingop\left_3.png','walkingop\left_4.png','walkingop\left_5.png','walkingop\left_6.png','walkingop\left_7.png','walkingop\left_8.png']


r_index=0
l_index=0



jump=False

c=0

# heroine 
img4= pygame.image.load('heroine.png').convert_alpha()
img4 = pygame.transform.smoothscale(img4, (hero_size,hero_size)) 



#audio 
sound = pygame.mixer.Sound('audio_1.mp3')


# objects

obj1=pygame.image.load('grass-removebg-preview.png').convert_alpha()
obj1= pygame.transform.smoothscale(obj1, (100,50)) 

objf=False




# Run until the user asks to quit
running = True
while running:
    clock.tick(18)
    drawGrid()
    screen.blit(img,(0,screen_h-road_h))
    screen.blit(img2,(0,0))
    
    # screen.blit(heading,(300,100))
    screen.blit(img4,(500,430))


    #objects
    screen.blit(obj1, (300,400))
  


    if(not left and  not right):
        img3= pygame.image.load('fighting/00.png').convert_alpha()
        img3 = pygame.transform.smoothscale(img3, (hero_size,hero_size)) 

    screen.blit(img3,(h_x,h_y))
    # Did the user click the window close button?
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                right=True
                left=False
                mov_x=3
                
                    
               
            if event.key == pygame.K_LEFT:
                left=True
                right=False
                mov_x=-3
            if event.key == pygame.K_DOWN :
                left=False
                right=False
        

                img5= pygame.image.load("fighting\sample.png").convert_alpha()
                img5 = pygame.transform.smoothscale(img5, (hero_size,hero_size)) 
                screen.blit(img5,(h_x,h_y))
                 
                
                mov_x=0
                mov_y=0
                
            
                pygame.mixer.Sound.play(sound)
                pygame.mixer.music.stop()

            if event.key == pygame.K_UP and jump==False:
                # left=False
                # right=False
                jump=True
                # mov_x=0
                c=7
                mov_y=20
                d=0
                # if(right):
                #     d=20
                # if(left):
                #     d=-20
                # h_x=h_x+d
                i_y=h_y


                 
               
    h_x+=mov_x
    
  
        
    
        
        

      
        

    
    if(right):
        left=False
        r_index= (r_index+1)%(len(right_walks)) 
        img3= pygame.image.load(right_walks[r_index]).convert_alpha()
        img3 = pygame.transform.smoothscale(img3, (hero_size,hero_size)) 
        if(jump):
            h_x=h_x+10
        pass


    if (left):
        right=False
        l_index= (l_index+1)%(len(left_walks))
        img3= pygame.image.load(left_walks[l_index]).convert_alpha()
        img3 = pygame.transform.smoothscale(img3, (hero_size,hero_size)) 
        if(jump):
            h_x=h_x-10
        pass
   
    if(h_x>=screen_w-20):
        mov_x=-3
        left=True
        right=False
    if(h_x<0):
        mov_x=3
        right=True 
        left=False       
    
    if(jump and c):
        h_y-=mov_y
        c=c-1
        
        if(not c):
            jump=False
            # d=0
            # if(right):
            #     d=40
            # if(left):
            #     d=-40
            # h_x=h_x+d
            
            h_y=i_y
   
   

        
       
    
            
    

        


            

    pygame.display.update()

# Done! Time to quit.
pygame.quit()

