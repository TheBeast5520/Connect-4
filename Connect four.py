import turtle
import os
graphics = turtle.Turtle()
graphics.speed("fastest")
screen= turtle.Screen()
screen.setup(1000, 1000)
turtle.bgcolor('black')
# the following lines make a function for creating a rectangle in any direction
def rectangle(t, side1, side2, direction):
    direction = direction.lower()
    sideDict = {'right': 0, 'up': 90, 'left': 180, 'down': 270}
    if direction in sideDict:
        t.setheading(sideDict[direction])
    else:
        t.setheading(direction)
    for i in range(2):
        t.forward(side1)
        t.right(90)
        t.forward(side2)
        t.right(90)
# the following lines create a function for creating circles in any direction
def circle(t, radius, direction):
    direction = direction.lower()
    sideDict = {'right': 0, 'up': 90, 'left': 180, 'down': 270}
    if direction in sideDict:
        t.setheading(sideDict[direction]+90)
    else:
        t.setheading(direction+90)
    t.circle(radius)
    if direction in sideDict:
        t.setheading(sideDict[direction])
    else:
        t.setheading(direction)
# The following lines create a function that creates a board for the connect-four game
def Board():
    global graphics
    graphics.fillcolor("yellow")
    graphics.penup()
    graphics.goto(-110, 95)
    graphics.pendown()
    graphics.begin_fill()
    rectangle(graphics, 220, 190, "right")
    graphics.end_fill()
    graphics.penup()
    graphics.goto(graphics.xcor(), graphics.ycor()+10)
    graphics.fillcolor("white")
    for i in range(6):
        graphics.hideturtle()
        graphics.penup()
        graphics.goto(graphics.xcor(), graphics.ycor()-30)
        for j in range(7):
            graphics.penup()
            graphics.goto(graphics.xcor()+30, graphics.ycor())
            graphics.pendown()
            graphics.begin_fill()
            circle(graphics, 10, "right")
            graphics.end_fill()
        graphics.penup()
        graphics.setheading(180)
        graphics.forward(210)
# The next lines create the turtles and sets their attributes
one = turtle.Turtle()
two = turtle.Turtle()
three = turtle.Turtle()
four = turtle.Turtle()
five = turtle.Turtle()
six = turtle.Turtle()
seven = turtle.Turtle()
write = turtle.Turtle()
write.speed("fastest")
columnTurtles = [one, two, three, four, five, six, seven]
import random
counter = random.randrange(0, 2)
for i in range(7):
    columnTurtles[i].speed("fastest")
# sets up an array containing all the slots in the board
board = [['n','n','n','n','n','n'],['n','n','n','n','n','n'],['n','n','n','n','n','n'],['n','n','n','n','n','n'],['n','n','n','n','n','n'],['n','n','n','n','n','n'],['n','n','n','n','n','n']]    
# function that inputs the players' names
def player_names():
    print("The player who goes first will be chosen at random.")
    player1 = input("Enter the first player's name. This player will be red.: \n")
    print("Player 1 is "+player1+".")
    player2 = input("Enter the second player's name. This player will be blue: \n")
    print("Player 2 is "+player2+".")
    return [player1, player2]
def winner_1():
    write.clear()
    write.write("The Game Is Over! "+player1+" has won!", align = "center", font = ("arial", 30, "normal"))
    print(player1, "is the winner.")
    input("Press any key to end the game.")
    os._exit(0)
def winner_2():
    write.clear()
    write.write("The Game Is Over! "+player2+" has won!", align = "center", font = ("arial", 30, "normal"))
    print(player2, "is the winner.")
    input("Press any key to end the game.")
    os._exit(0)

# creates a function that checks whether there is a winner or not
def winner():
    global board
    string = ""
    for i in range(7):
        for j in range(6):
            string += board[i][j]
        if "rrrr" in string:
            winner_1()
        elif "bbbb" in string:
            winner_2()
    for j in range(6):
        for i in range(7):
            string += board[i][j]
        if "rrrr" in string:
            winner_1()
        elif "bbbb" in string:
            winner_2()
    for i in range(0,4):
        for j in range(3, 6):
            if board[i][j]+board[i+1][j-1]+board[i+2][j-2]+board[i+3][j-3] == "rrrr":
                winner_1()
            elif board[i][j]+board[i+1][j-1]+board[i+2][j-2]+board[i+3][j-3] == "bbbb":
                winner_2()
    for i in range(3,7):
        for j in range(3, 6):
            if board[i][j]+board[i-1][j-1]+board[i-2][j-2]+board[i-3][j-3] == "rrrr":
                winner_1()
            elif board[i][j]+board[i-1][j-1]+board[i-2][j-2]+board[i-3][j-3] == "bbbb":
                winner_2()
# sets function for checking if there is a draw
def draw():
    global board
    a = 0
    for i in board:
        if "n" in i:
            a = 1
    if a == 0:
        print("The game was a draw.")
        input("Press any key to end the game.")
        os._exit(0)
# the next seven functions are the outlines of buttons that will do the actual graphics for inserting tokens into board.
def column1(x,y):
    global board
    global one
    global counter
    global write
    if x > -110 and x < -110 + 35 and y < 95 and y > -95:
        if counter == 0:
            if "n" in board[0]:
                one.penup()
                index = board[0].index("n")
                board[0][index] = "r"
                one.fillcolor("red")
                one.begin_fill()
                circle(one, 10, "down")
                one.end_fill()
                one.left(180)
                one.forward(30)
                counter = (counter + 1)%2
                write.clear()
                write.write("It is "+player2+"'s turn! Click on a column", align = "center", font = ("arial", 30, "normal"))
        elif counter == 1:
            if "n" in board[0]:
                one.penup()
                index = board[0].index("n")
                board[0][index] = "b"
                one.fillcolor("blue")
                one.begin_fill()
                circle(one, 10, "down")
                one.end_fill()
                one.left(180)
                one.forward(30)
                counter = (counter + 1)%2
                write.clear()
                write.write("It is "+player1+"'s turn! Click on a column", align = "center", font = ("arial", 30, "normal"))
        winner()
        draw()
def column2(x,y):
    global board
    global two
    global counter
    global write
    if x > -110 +35 and x < -110 + 35+30 and y < 95 and y > -95:
        if counter == 0:
            if "n" in board[1]:
                two.penup()
                index = board[1].index("n")
                board[1][index] = "r"
                two.fillcolor("red")
                two.begin_fill()
                circle(two, 10, "down")
                two.end_fill()
                two.left(180)
                two.forward(30)
                counter = (counter + 1)%2
                write.clear()
                write.write("It is "+player2+"'s turn! Click on a column", align = "center", font = ("arial", 30, "normal"))
        elif counter == 1:
            if "n" in board[1]:
                two.penup()
                index = board[1].index("n")
                board[1][index] = "b"
                two.fillcolor("blue")
                two.begin_fill()
                circle(two, 10, "down")
                two.end_fill()
                two.left(180)
                two.forward(30)
                counter = (counter + 1)%2
                write.clear()
                write.write("It is "+player1+"'s turn! Click on a column", align = "center", font = ("arial", 30, "normal"))
        winner()
        draw()
def column3(x,y):
    global board
    global three
    global counter
    global write
    if x > -110 +35+30 and x < -110 + 35+(2*30) and y < 95 and y > -95:
        if counter == 0:
            if "n" in board[2]:
                three.penup()
                index = board[2].index("n")
                board[2][index] = "r"
                three.fillcolor("red")
                three.begin_fill()
                circle(three, 10, "down")
                three.end_fill()
                three.left(180)
                three.forward(30)
                counter = (counter + 1)%2
                write.clear()
                write.write("It is "+player2+"'s turn! Click on a column", align = "center", font = ("arial", 30, "normal"))
        elif counter == 1:
            if "n" in board[2]:
                three.penup()
                index = board[2].index("n")
                board[2][index] = "b"
                three.fillcolor("blue")
                three.begin_fill()
                circle(three, 10, "down")
                three.end_fill()
                three.left(180)
                three.forward(30)
                counter = (counter + 1)%2
                write.clear()
                write.write("It is "+player1+"'s turn! Click on a column", align = "center", font = ("arial", 30, "normal"))
        winner()
        draw()
def column4(x,y):
    global board
    global four
    global counter
    global write
    if x > -110 +35+(2*30) and x < -110 + 35+(3*30) and y < 95 and y > -95:
        if counter == 0:
            if "n" in board[3]:
                four.penup()
                index = board[3].index("n")
                board[3][index] = "r"
                four.fillcolor("red")
                four.begin_fill()
                circle(four, 10, "down")
                four.end_fill()
                four.left(180)
                four.forward(30)
                counter = (counter + 1)%2
                write.clear()
                write.write("It is "+player2+"'s turn! Click on a column", align = "center", font = ("arial", 30, "normal"))
        elif counter == 1:
            if "n" in board[3]:
                four.penup()
                index = board[3].index("n")
                board[3][index] = "b"
                four.fillcolor("blue")
                four.begin_fill()
                circle(four, 10, "down")
                four.end_fill()
                four.left(180)
                four.forward(30)
                counter = (counter + 1)%2
                write.clear()
                write.write("It is "+player1+"'s turn! Click on a column", align = "center", font = ("arial", 30, "normal"))
        winner()
        draw()
def column5(x,y):
    global board
    global five
    global counter
    global write
    if x > -110 +35+(3*30) and x < -110 + 35+(4*30) and y < 95 and y > -95:
        if counter == 0:
            if "n" in board[4]:
                five.penup()
                index = board[4].index("n")
                board[4][index] = "r"
                five.fillcolor("red")
                five.begin_fill()
                circle(five, 10, "down")
                five.end_fill()
                five.left(180)
                five.forward(30)
                counter = (counter + 1)%2
                write.clear()
                write.write("It is "+player2+"'s turn! Click on a column", align = "center", font = ("arial", 30, "normal"))
        elif counter == 1:
            if "n" in board[4]:
                five.penup()
                index = board[4].index("n")
                board[4][index] = "b"
                five.fillcolor("blue")
                five.begin_fill()
                circle(five, 10, "down")
                five.end_fill()
                five.left(180)
                five.forward(30)
                counter = (counter + 1)%2
                write.clear()
                write.write("It is "+player1+"'s turn! Click on a column", align = "center", font = ("arial", 30, "normal"))
        winner()
        draw()
def column6(x,y):
    global board
    global six
    global counter
    global write
    if x > -110 +35+(4*30) and x < -110 + 35+(5*30) and y < 95 and y > -95:
        if counter == 0:
            if "n" in board[5]:
                six.penup()
                index = board[5].index("n")
                board[5][index] = "r"
                six.fillcolor("red")
                six.begin_fill()
                circle(six, 10, "down")
                six.end_fill()
                six.left(180)
                six.forward(30)
                counter = (counter + 1)%2
                write.clear()
                write.write("It is "+player2+"'s turn! Click on a column", align = "center", font = ("arial", 30, "normal"))
        elif counter == 1:
            if "n" in board[5]:
                six.penup()
                index = board[5].index("n")
                board[5][index] = "b"
                six.fillcolor("blue")
                six.begin_fill()
                circle(six, 10, "down")
                six.end_fill()
                six.left(180)
                six.forward(30)
                counter = (counter + 1)%2
                write.clear()
                write.write("It is "+player1+"'s turn! Click on a column", align = "center", font = ("arial", 30, "normal"))
        winner()
        draw()
def column7(x,y):
    global board
    global seven
    global counter
    global write
    if x > -110 +35+(5*30) and x < -110 + 35+(6*30) and y < 95 and y > -95:
        if counter == 0:
            if "n" in board[6]:
                seven.penup()
                index = board[6].index("n")
                board[6][index] = "r"
                seven.fillcolor("red")
                seven.begin_fill()
                circle(seven, 10, "down")
                seven.end_fill()
                seven.left(180)
                seven.forward(30)
                counter = (counter + 1)%2
                write.clear()
                write.write("It is "+player2+"'s turn! Click on a column", align = "center", font = ("arial", 30, "normal"))
        elif counter == 1:
            if "n" in board[6]:
                seven.penup()
                index = board[6].index("n")
                board[6][index] = "b"
                seven.fillcolor("blue")
                seven.begin_fill()
                circle(seven, 10, "down")
                seven.end_fill()
                seven.left(180)
                seven.forward(30)
                counter = (counter + 1)%2
                write.clear()
                write.write("It is "+player1+"'s turn! Click on a column", align = "center", font = ("arial", 30, "normal"))
        winner()
        draw()
# sets up some of the turtles
def playing():
    global columnTurtles
    global one
    global two
    global three
    global four
    global five
    global six
    global seven
    global write
    for i in columnTurtles:
        i.penup()
        i.goto(-90, -85)
        i.hideturtle()
    for i in range(len(columnTurtles)):
        columnTurtles[i].forward(i*30)
    write.hideturtle()
    write.penup()
    write.goto(0, 105)
players = player_names()
player1 = players[0]
player2 = players[1]
# puts all of it together into one game
def connect_four():
    global player1
    global player2
    Board()
    playing()
    if counter == 0:
        write.clear()
        write.write(player1+ """ goes first.
Click on one of the columns of the
connect-four board to place your piece""", align = "center", font = ("arial", 30, "normal"))
    elif counter == 1:
        write.clear()
        write.write(player2+ """ goes first.
Click on one of the columns of the
connect-four board to place your piece""", align = "center", font = ("arial", 30, "normal"))
# sets up all the buttons into action
turtle.onscreenclick(column1, 1, add = False)
turtle.onscreenclick(column2, 1, add = True)
turtle.onscreenclick(column3, 1, add = True)
turtle.onscreenclick(column4, 1, add = True)
turtle.onscreenclick(column5, 1, add = True)
turtle.onscreenclick(column6, 1, add = True)
turtle.onscreenclick(column7, 1, add = True)
connect_four()
turtle.listen()
turtle.done()

