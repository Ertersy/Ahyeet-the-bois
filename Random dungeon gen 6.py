import random
import turtle
# You should avoid using * imports, they pollute your environment and make debug a lot harder
import turtle as trtl

# Functions should always be declared outside any code structure that is not a class,
# you may end up re-declaring the function at each loop
# Let's use parameters and returns for better code encapsulation
# assignig random 0's and 1's into the grid
def assignrandom(grid, gridlen):
    for z in range(gridlen):
        for x in range(gridlen):
            for y in range(len(grid[0][x])):
                grid[z][x][y] = random.choice([1,0])
    return grid

#correcting the 1's and 0's to make sure paths are joining right to left
def correctinglr(grid, gridlen):
    for x in range(gridlen):
        for y in range(gridlen - 1):
            while grid[x][y][2] + grid[x][y + 1][0] == 1:
                grid[x][y][2] = random.choice([1,0])
                grid[x][y + 1][0] = random.choice([1,0])
    return grid

#correcting the 1's and 0's to make sure paths are joining top to bottom
def correctingud(grid, gridlen):
    for x in range(gridlen):
        for y in range(gridlen):
            for z in range(gridlen - 1):
                while (grid[z][y][3] + grid[z + 1][y][1]) == 1:
                    grid[z][y][3] = random.choice([1,0])
                    grid[z][y][1] = random.choice([1,0])
    return grid

#making sure no paths go outside of the grid
def outeredges(grid, gridlen):
    for x in range(len(grid)):
        grid[0][x][1] = 0
        grid[gridlen - 1][x][3] = 0
        grid[x][0][0] = 0
        grid[x][gridlen - 1][2] = 0
    return grid

#used for resets:
another = 0
yn = "Y"
while yn.upper() == "Y":
    #setup of variables and functions
    grid_size_valid = False
    # Since the algorithm needs to work out the "middle line", the size must be
    # an odd number
    # -------------------------
    while not grid_size_valid:
        gridlen = int(input("How big do you want the grid to be?"))
        grid_size_valid = gridlen % 2 == 1
        if not grid_size_valid:
            print("The size of the grid must be an odd number")
    # -------------------------
    # This list comprehension creates a "gridlen by gridlen"
    # (like 7x7, 9x9, ...) grid filled with [0,0,0,0]
    grid = [
        [
            [0,0,0,0]
            for _ in range(gridlen)
        ]
        for _ in range(gridlen)]
    thrd = 600/gridlen/3

    # All the calls to the functions defined now assign to "grid", so that they can
    # modify it (For more info see the topic of "scoping" in Computer Science)
    grid = assignrandom(grid, gridlen)
    grid = correctinglr(grid, gridlen)
    grid = correctingud(grid, gridlen)
    grid = outeredges(grid, gridlen)
    #making sure the middle of the grid is a 1,1,1,1 pathway
    if (gridlen % 2) != 0:
        middle = int((gridlen + 1) / 2 - 1)
        middleline = int((len(grid) + 1) / 2 - 1)
    while grid[middleline][middle] != [1,1,1,1]:
            grid = assignrandom(grid, gridlen)
            grid = correctinglr(grid, gridlen)
            grid = correctingud(grid, gridlen)
            grid = outeredges(grid, gridlen)

 #animation of the turtle on / off
    anim = input("Do you want animation? Y/N?")
    #setup of turtle
    if anim.upper() == "N":
        turtle.tracer(False)
    elif anim.upper() == "Y":
        print("OK!")
        trtl.speed(100)
    if another == 1:
        turtle.clear()
        trtl.left(90)
        trtl.forward(600)
        trtl.right(90)
    else:
        trtl.penup()
        trtl.right(180)
        trtl.forward(300)
        trtl.right(90)
        trtl.forward(300 - thrd)
        trtl.right(90)
        another = 1
    #code for path drawing
    for x in range(gridlen):
        for y in range(gridlen):
            for g in range(4):
              if grid[x][y] == [0,0,0,0]:
                  trtl.penup()
                  trtl.forward(thrd/1.33333333)
              else:
                  if g == 0:
                    if grid[x][y][0] == 1:
                       trtl.pendown()
                       trtl.forward(thrd)
                       trtl.right(90)
                       trtl.penup()
                       trtl.forward(thrd)
                       trtl.pendown()
                       trtl.right(90)
                       trtl.forward(thrd)
                       trtl.penup()
                       trtl.right(90)
                       trtl.forward(thrd)
                       trtl.right(90)
                       trtl.forward(thrd)
                    else:
                       trtl.penup()
                       trtl.forward(thrd)
                       trtl.right(90)
                       trtl.pendown()
                       trtl.forward(thrd)
                       trtl.left(180)
                       trtl.penup()
                       trtl.forward(thrd)
                       trtl.right(90)
                  if g == 1:
                    if grid[x][y][1] == 1:
                        trtl.left(90)
                        trtl.pendown()
                        trtl.forward(thrd)
                        trtl.right(90)
                        trtl.penup()
                        trtl.forward(thrd)
                        trtl.right(90)
                        trtl.pendown()
                        trtl.forward(thrd)
                        trtl.left(90)
                    else:
                        trtl.pendown()
                        trtl.forward(thrd)
                  if g == 2:
                    if grid[x][y][2] == 1:
                          trtl.pendown()
                          trtl.forward(thrd)
                          trtl.right(90)
                          trtl.penup()
                          trtl.forward(thrd)
                          trtl.right(90)
                          trtl.pendown()
                          trtl.forward(thrd)
                          trtl.penup()
                          trtl.left(90)
                    else:
                        trtl.pendown()
                        trtl.right(90)
                        trtl.forward(thrd)
                        trtl.penup()
                  if g == 3:
                    if grid[x][y][3] == 1:
                          trtl.pendown()
                          trtl.forward(thrd)
                          trtl.right(90)
                          trtl.penup()
                          trtl.forward(thrd)
                          trtl.right(90)
                          trtl.pendown()
                          trtl.forward(thrd)
                          trtl.penup()
                          trtl.forward(thrd)
                          trtl.right(90)
                          trtl.forward(thrd)
                          trtl.forward(thrd)
                    else:
                        trtl.right(90)
                        trtl.pendown()
                        trtl.forward(thrd)
                        trtl.right(90)
                        trtl.penup()
                        trtl.forward(thrd)
                        trtl.right(90)
                        trtl.forward(thrd)
                        trtl.forward(thrd)
        trtl.right(90)
        trtl.penup()
        trtl.forward(thrd)
        trtl.forward(thrd)
        trtl.forward(thrd)
        trtl.right(90)
        trtl.forward(600)
        trtl.right(180)
    if anim.upper() == "N":
        turtle.tracer(True)

    yn = input("Another? Y/N: ")
