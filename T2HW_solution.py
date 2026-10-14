# Libraries

import pygame
import random
import time

# Screen Size

screenWidth = 320
screenHeight = 640

# Creating the Screen

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("TDC Window")

# Functions

def generateRandomLetter():
    letterIndex = random.randint(0,25)
    return alphabetArray[letterIndex]

def generateSlantValue():
    return random.randint(-5,5)/10

def generateHeightValue():
    return random.randint(0,10)/10

# Drawing Function

def draw():
    screen.fill("white")
    for i in range(len(mousePostionArray)):
        pygame.draw.rect(screen, "black", pygame.Rect((mousePostionArray[i][0]//10) *10, (mousePostionArray[i][1]//10) *10, 10, 10))

    pygame.display.update()

# Arrays

mousePostionArray = []
alphabetArray = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Loop keeping window 

running = True

letter = generateRandomLetter()
height = generateHeightValue()
slant = generateSlantValue()

print("Letter: " + letter)
print("Height: ", + height)
print("Slant: ", + slant)


while running == True:
    # Actions towards screen go in this loop

    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 2:

                with open("letter.txt", "a") as f:
                    f.write(str(letter) + "\n" )

                with open("height.txt", "a") as f:
                    f.write(str(height) + "\n" )

                with open("slant.txt", "a") as f:
                    f.write(str(slant) + "\n" )

                tempPixelData = ""

                for row in range(int(screenHeight/10)):
                    for col in range(int(screenWidth/10)):
                        tempPixelData += str((int((screen.get_at((col*10,row*10))[0]-255)/(-255))))

                with open("pixelData.txt", "a") as f:
                    f.write(str(tempPixelData) + "\n")

                letter = generateRandomLetter()
                height = generateHeightValue()
                slant = generateSlantValue()
                 
                print("Letter: " + letter)
                print("Height: ", + height)
                print("Slant: ", + slant)


    if pygame.mouse.get_pressed()[0] == True:
        mousePostionArray.append(pygame.mouse.get_pos())

    if pygame.mouse.get_pressed()[2] == True:
        mousePostionArray = []
