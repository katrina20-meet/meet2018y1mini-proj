import turtle
import random #We'll need this later in the lab
import time
turtle.bgcolor("black")

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(1000, 1000) #Curious? It's the turtle window  
                             #size. 
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.pencolor("yellow")
snake.shape("square")


#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

line= turtle.clone()
turtle.hideturtle()
line.pencolor("white")
line.penup()
line.goto(-410, 280)
line.pendown()
line.goto(410, 280)
line.goto(410, -280)
line.goto(-410,-280)
line.goto(-410, 280)
line.penup()
line.goto(0, 400)
line.pendown()
line.write("~~SNAKE GAME~~", align="center", font=("Arial",20,"normal"))
line.penup()
scores= turtle.clone()
scores.penup()
scores.pencolor("white")
scores.goto(0,-400)
line.goto(0,0)

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for strt_lngth in range(START_LENGTH) :
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1]
    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE

    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    SNAKE = snake.stamp()
    stamp_list.append(SNAKE)


UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 0
DOWN= 1
LEFT=2
RIGHT=3

#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!

direction = UP
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400


def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
    print("You pressed the up key!")


turtle.onkeypress(up, UP_ARROW) # Create listener for up key


def down():
    global direction #snake direction is global (same everywhere)
    direction=DOWN #Change direction to up
    print("You pressed the down key!")


turtle.onkeypress(down, DOWN_ARROW) # Create listener for up key


def left():
    global direction #snake direction is global (same everywhere)
    direction=LEFT #Change direction to up
    print("You pressed the left key!")


turtle.onkeypress(left, LEFT_ARROW) # Create listener for up key


def right():
    global direction #snake direction is global (same everywhere)
    direction=RIGHT #Change direction to up
    print("You pressed the right key!")


turtle.onkeypress(right, RIGHT_ARROW) # Create listener for up key
turtle.listen()

turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif")
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

turtle.register_shape("rock.gif")
rock= turtle.clone()
rock.shape("rock.gif")
rock_pos=[(60,60), (-60, 60), (-60, -60), (60, -60)]
rock_stamps=[]

x=0
for this_rock_pos in rock_pos:
    rock.goto(rock_pos[x])
    rock_stamp= rock.stamp()
    rock_stamps.append(rock_stamp)
    x= x+1

    
def make_rocks():
    global rock
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
    rock_x = random.randint(min_x,max_x)*SQUARE_SIZE
    rock_y = random.randint(min_y,max_y)*SQUARE_SIZE
    rock.goto(rock_x, rock_y)
    rock_pos.append(rock.pos())
    rock_stamp=rock.stamp()
    rock_stamps.append(rock_stamp)
    
    

x=0   
for this_food_pos in food_pos :
    food.goto(food_pos[x])
    food_stamp= food.stamp()
    food_stamps.append(food_stamp)
    x=x+1

    
def make_food():
    global food
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x, food_y)
    food_pos.append(food.pos())
    food_stmp=food.stamp()
    food_stamps.append(food_stmp)
    
score= 0

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("you moved up!")
    elif direction==DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE) 
        print("you moved down!")
    #Grab position of snake
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    
    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        line.write("haha! you lose!", align="center", font=("arial", 30, "normal"))
        time.sleep(3)
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        line.write("haha! you lose!", align="center", font=("arial", 30, "normal"))
        time.sleep(3)
        quit()
    elif new_y_pos >= UP_EDGE:
        print("You hit the top edge! Game over!")
        line.write("haha! you lose!", align="center", font=("arial", 30, "normal"))
        time.sleep(3)
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print("You hit the bottom edge! Game over!")
        line.write("haha! you lose!", align="center", font=("arial", 30, "normal"))
        time.sleep(3)
        quit()

    if pos_list[-1] in pos_list[0:-1]:
        line.write("didn't your parents tell you not to eat yourself!?", align="center", font=("arial", 30, "normal"))
        time.sleep(3)
        quit()
   

    #4. Write the conditions for UP and DOWN on your own
    ##### YOUR CODE HERE

    #Stamp new element and append new stamp in list
    #Remember: The snake position changed - update my_pos()

    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5
    #pop zeroth element in pos_list to get rid of last the last 
    #piece of the tail
    global food_stamps, food_pos, score
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food                 
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
        print("You have eaten the food!")
        score=score+10
        print(score)
        scores.pendown()
        scores.clear()
        scores.write((score), align="center", font=("arial",18,"normal"))
        global TIME_STEP
        TIME_STEP= TIME_STEP-1
    else:   
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)

        
    if len(food_stamps) <= 6 :
        make_food()
                                
    
    turtle.ontimer(move_snake,TIME_STEP)
move_snake()




         
