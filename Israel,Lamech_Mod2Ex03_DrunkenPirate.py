#########################################
# CS 1110A - Programming in Python      #
# Module 2 - Exercise 3 - Drunken Pirate#
# Author: Lamech Israel                 #
# Date:   01/17/2023                    #
#########################################

import turtle
import random

# Input

wn = turtle.Screen()

pirate = turtle.Turtle()

random_path_length = random.randint(1, 25)


# Original path variable
# path = [45, -75, 160, -43, 270, -97, -43, 200, -940, 17, -86, 150, 25, 75, -90, 20, -145, 30,
#      -50, -70, -105]
path = []


# Processing

for p in range(random_path_length):
    random_turn = random.randint(-1000, 1000)
    path.append(random_turn)
    

for i in path:
    pirate.left(i)
    pirate.forward(100)
    pirate.stamp()
    
#Output
   
print('The amount of turns the pirate took was',random_path_length)
print('The angles he took were',path)


wn.mainloop()

print('\nDone!')