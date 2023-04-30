#Name: Aryan Patel
#Student ID: 101260400


import pygame
import sys
import random

#uses sys.argv to get the users input and stores it in the variable image_name
image_name = sys.argv[1]

#loads the images file name and stores it as a image in a variable
src_image = pygame.image.load(image_name)

#gets the total width and total height of the image
(w,h) = src_image.get_size()

#sets the size of the window by taking the size of the image inputted and scaling it up by 4 and storing it in the variable screen
screen = pygame.display.set_mode((w*2,h*2))


#Loop goes through each x and y value
for y in range(h):
    for x in range(w):

        # while the loop is true each pixels rgb value is taken, divided by 50 which sets the ratio of red, green and blue rectangles per pixel


        (r,g,b,_) = src_image.get_at((x,y))
       
        a = r // 50
        k = g // 50
        d = b // 50
    
#For the range of each colour prints that amount of rectangles per pixel then ends the loop
        for red_colour in range(a):
            pygame.draw.rect(screen, (255,0, 0), ((x * 2) + random.randint(0, 4), (y * 2) + random.randint(0, 4), 1, 1))
           
        for green_colour in range(k):
            pygame.draw.rect(screen, (0, 255, 0), ((x * 2) + random.randint(0, 4), (y * 2) + random.randint(0, 4), 1, 1))
              
        for blue_colour in range(d):
            pygame.draw.rect(screen, (0, 0, 255), ((x * 2) + random.randint(0, 4), (y * 2) + random.randint(0, 4), 1, 1))
   

            
                
#updates the screen to display the image  
pygame.display.update()
#Keep window open until closed by user
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
