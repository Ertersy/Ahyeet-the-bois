import random
import turtle
from turtle import *

#I attempted to implement user choice  of grid size but failed. If you have an idea as to how I can do that please feel free to message me!
#gridlen = int(input("How big do you want the grid to be?"))



#used for resets:
another = 0
yn = "Y"
while yn == "Y":
    #setup of variables and functions
    gridlen = 7
    line1 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    line2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    line3 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    line4 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    line5 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    line6 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    line7 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    grid = [line1,line2,line3,line4,line5,line6,line7]
    thrd = 600/gridlen/3
  #assignig random 0's and 1's into the grid
    def assignrandom():
        for z in range(gridlen):
            for x in range(gridlen):
                for y in range(len(line1[x])):
                  grid[z][x][y] = random.choice([1,0])

  #correcting the 1's and 0's to make sure paths are joining right to left
    def correctinglr():
        for x in range(gridlen):
            for y in range(gridlen - 1):
              while grid[x][y][2] + grid[x][y + 1][0] == 1:
                grid[x][y][2] = random.choice([1,0])
                grid[x][y + 1][0] = random.choice([1,0])

  #correcting the 1's and 0's to make sure paths are joining top to bottom
    def correctingud():
        for x in range(gridlen):
          for y in range(gridlen):
              for z in range(gridlen - 1):
                  while (grid[z][y][3] + grid[z + 1][y][1]) == 1:
                      grid[z][y][3] = random.choice([1,0])
                      grid[z][y][1] = random.choice([1,0])

  #making sure no paths go outside of the grid
    def outeredges():
        for x in range(len(grid)):
            grid[0][x][1] = 0
            grid[6][x][3] = 0
            grid[x][0][0] = 0
            grid[x][6][2] = 0

    #line1 = [[0,0,0,0] for _ in range(gridlen)] #duplicates [0,0,0,0] a number of times
    #grid = [line1.copy() for _ in range(gridlen)]

    assignrandom()
    correctinglr()
    correctingud()
    outeredges()
    #making sure the middle of the grid is a 1,1,1,1 pathway
    if (gridlen % 2) != 0:
        middle = int((gridlen + 1) / 2 - 1)
        middleline = int((len(grid) + 1) / 2 - 1)
    while grid[middleline][middle] != [1,1,1,1]:
            assignrandom()
            correctinglr()
            correctingud()
            outeredges()


 #animation of the turtle on / off
    anim = input("Do you want animation? Y/N?")
    #setup of turtle
    if anim == "N":
        turtle.tracer(False)
    elif anim == "Y":
        print("OK!")
        speed(100)
    if another == 1:
        turtle.clear()
        left(90)
        forward(600)
        right(90)
    else:
        penup()
        right(180)
        forward(300)
        right(90)
        forward(300 - thrd)
        right(90)
        another = 1
    #code for path drawing
    for x in range(7):
        for y in range(7):
            for g in range(4):
              if grid[x][y] == [0,0,0,0]:
                  penup()
                  forward(thrd/1.33333333)
              else:
                  if g == 0:
                    if grid[x][y][0] == 1:
                       pendown()
                       forward(thrd)
                       right(90)
                       penup()
                       forward(thrd)
                       pendown()
                       right(90)
                       forward(thrd)
                       penup()
                       right(90)
                       forward(thrd)
                       right(90)
                       forward(thrd)
                    else:
                       penup()
                       forward(thrd)
                       right(90)
                       pendown()
                       forward(thrd)
                       left(180)
                       penup()
                       forward(thrd)
                       right(90)

                  if g == 1:
                    if grid[x][y][1] == 1:
                        left(90)
                        pendown()
                        forward(thrd)
                        right(90)
                        penup()
                        forward(thrd)
                        right(90)
                        pendown()
                        forward(thrd)
                        left(90)
                    else:
                        pendown()
                        forward(thrd)
                  if g == 2:
                    if grid[x][y][2] == 1:
                          pendown()
                          forward(thrd)
                          right(90)
                          penup()
                          forward(thrd)
                          right(90)
                          pendown()
                          forward(thrd)
                          penup()
                          left(90)
                    else:
                        pendown()
                        right(90)
                        forward(thrd)
                        penup()
                  if g == 3:
                    if grid[x][y][3] == 1:
                          pendown()
                          forward(thrd)
                          right(90)
                          penup()
                          forward(thrd)
                          right(90)
                          pendown()
                          forward(thrd)
                          penup()
                          forward(thrd)
                          right(90)
                          forward(thrd)
                          forward(thrd)
                    else:
                        right(90)
                        pendown()
                        forward(thrd)
                        right(90)
                        penup()
                        forward(thrd)
                        right(90)
                        forward(thrd)
                        forward(thrd)
        right(90)
        penup()
        forward(thrd)
        forward(thrd)
        forward(thrd)
        right(90)
        forward(600)
        right(180)
    if anim == "N":
        turtle.tracer(True)

    yn = input("another? Y/N: ")
