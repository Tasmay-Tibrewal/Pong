# Screen Tennis

# Import Section
import turtle
import random
import threading
import winsound
from time import perf_counter_ns
from tkinter import *
import csv


# Screen Setup
sc = turtle.Screen()
sc.title("Screen Tennis")
sc.bgcolor("Black")
sc.setup(width=1200, height=800)
sc._root.iconbitmap(r"Items\Screentennis_logo.ico")


# Global Variables/ OBJECTS
t = threading.Event()
n = 1
v = 0
z = 1
ch=0
copy1 = 0
copy2 = 0
l = 0
h = 5
high = 0
list=[]
m = 0
tas = 0
tascopy = 0
countf = 1
count = 0
count1 = 0
count2 = 0
count3 = 1
count4 = 0
count5 = 0
count6 = 0
count7 = 0


# Slider A Setup
t1 = turtle.Turtle()
t1.seth(90)
t1.speed(10)
t1.penup()
t1.hideturtle()
t1.goto(-550, 0)
t1.color('Red')
t1.shape('square')
t1.shapesize(stretch_len = 5, stretch_wid = 1)


# Slider B Setup
t2 = turtle.Turtle()
t2.seth(90)
t2.speed(10)
t2.penup()
t2.hideturtle()
t2.goto(550, 0)
t2.color('Blue')
t2.shape('square')
t2.shapesize(stretch_len = 5, stretch_wid = 1)


# Ball Setup
r = turtle.Turtle()
r.speed(0)
r.penup()
r.hideturtle()
r.shape('circle')
r.color('Green')


# Scorer
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.color('white')

a = 0
b = 0


# Boundary
x = turtle.Turtle()
x.hideturtle()
x.speed(8)
x.color('yellow')

def bound():    
    x.goto(0, 262)
    x.goto(575, 262)
    x.goto(575, -262)
    x.goto(-575, -262)
    x.goto(-575, 262)
    x.goto(0, 262)
    x.goto(0, -262)


# dx,dy,dt,mult set
dt = 0.005
dtcopy = dt
dx = 10
choice = random.randint(1, 2)
if choice == 2:
    z = -1
dx = z*dx
dy = 0
mult = 1.25
multcopy = mult

# Functions

def sety():
    
    global dy
    
    while dy == 0:
        dy = random.randint(-10, 10)


def a1():
    
    global dt, dtcopy, n, mult, multcopy, count1, count4
    
    if n == 1 and count1 == 1 and count4 == 0  and count == 0 :

        winsound.PlaySound(r"Items\Game_Action.wav", winsound.SND_ASYNC)

        p2.clear()
        p2.write("1", font=("Courier", 24, "normal"))

        dt = 0.010
        dtcopy = dt
        mult = 1 
        multcopy = mult


def b2():
    
    global dt, dtcopy, n, mult, multcopy, count1, count4
    
    if n == 1 and count1 == 1 and count4 == 0 and count == 0 :
        
        winsound.PlaySound(r"Items\Game_Action.wav", winsound.SND_ASYNC)

        p2.clear()
        p2.write("2", font=("Courier", 24, "normal"))

        dt = 0.005
        dtcopy = dt
        mult = 1.25
        multcopy = mult


def c3():
    
    global dt, dtcopy, n, mult, multcopy, count1, count4
    
    if n == 1 and count1 == 1 and count4 == 0 and count == 0 :
        
        winsound.PlaySound(r"Items\Game_Action.wav", winsound.SND_ASYNC)

        p2.clear()
        p2.write("3", font=("Courier", 24, "normal"))

        dt = 0.005
        dtcopy = dt
        mult = 1.5 
        multcopy = mult


def d4():
    
    global dt, dtcopy, n, mult, multcopy, count1, count4
    
    if n == 1 and count1 == 1 and count4 == 0 and count == 0 :

        winsound.PlaySound(r"Items\Game_Action.wav", winsound.SND_ASYNC)

        p2.clear()

        dt = 0.005
        dtcopy = dt
        mult = 1.25
        multcopy = mult

def d5():
    
    global dt, dtcopy, n, mult, multcopy
    
    if n == 1 :

        p2.clear()

        dt = 0.005
        dtcopy = dt
        mult = 1.25
        multcopy = mult



def e5():
    
    global n, count1, count4, m
    
    if n == 1 and count1 == 1 and m == 1 and count == 0 and count4 == 0:

        n = 0
        m = 0
        count4 = 1
        
        winsound.PlaySound(r"Items\Game_Action.wav", winsound.SND_ASYNC)
        
        p.clear()
        p2.clear()
        p2.goto(0, 0)
        
        bound()
        
        t1.showturtle()
        t2.showturtle()
        
        r.goto(0,0)
        r.showturtle()
        
        p.goto(0, -320)
        p.write("Press L to exit game, Escape to Quit, P to Pause/ Play.", align = "center", font = ("Courier", 24, "normal"))
        
        pen.goto(0, 300)
        pen.write("Player A : 0    Player B : 0 ", align = "center", font = ("Courier", 24, "normal"))
        game()


def f6():
    
    winsound.PlaySound(r"Items\Game_Action.wav", winsound.SND_FILENAME)
    
    quit()


def f7():
    
    global n, a, b, countf

    n = 1
    
    winsound.PlaySound(r"Items\Game_Action.wav", winsound.SND_FILENAME)

    if countf == 0:

        countf = 1

        with open(r'Items\score.csv','a',newline='') as csvfile:
        
            csvwriter = csv.writer(csvfile)
        
            sc=[a,b]
        
            csvwriter.writerow(sc)
            csvfile.flush()
    
    quit()


def g7():

    global high, list, count, count1, count3, count4, count6, count7, l, h

    if count1 == 1 and count4 == 0 and count6 == 1 and count == 0 :

        count6 = 0
        count = 1
        
        count3 = 0
        l = 0
        h = 5
        list=[]
        
        p2.clear()
        p.clear()

        p.speed(0)
    
        p.goto(0,250)
        p.write('Score History:-', align = "center", font = ("Courier", 72, "normal"))
    
        p.color('red')
        p.goto(-430,225)
        p.pendown()
        p.begin_fill()
        p.goto(-275,225)
        p.goto(-275,175)
        p.goto(-430,175)
        p.end_fill()
        p.color('white')
        p.pensize(3)
        p.penup()
    
        p.goto(-250,160)
        p.write('Team A', font=("Courier", 48, "normal"))

        p.goto(30,160)
        p.write('Team B', font=("Courier", 48, "normal"))

        p.color('blue')
        p.goto(430,225)
        p.pendown()
        p.begin_fill()
        p.goto(275,225)
        p.goto(275,175)
        p.goto(430,175)
        p.end_fill()
        p.color('white')
        p.pensize(3)
        p.penup()

        p.goto(-460,162)
        p.pendown()
        p.goto(460,162)
        p.penup()

        p.goto(-460,253)
        p.pendown()
        p.goto(460,253)
        p.penup()

        p.goto(0,253)
        p.pendown()
        p.goto(0,-235)
        p.penup()

        p.goto(-460,253)
        p.pendown()
        p.goto(-460,-235)
        p.penup()

        p.goto(460,253)
        p.pendown()
        p.goto(460,-235)
        p.penup()

        p.goto(-460,-235)
        p.pendown()
        p.goto(460,-235)
        p.penup()

        with open(r'Items\score.csv','r',newline='') as csvfile:
            
            csvreader = csv.reader(csvfile)
            
            for row in csvreader:
                
                list.append(row)
    
        list.reverse()

        high=len(list)

        wr_score()

        p.goto(0, -300)
        p.write("Press 'N' for Next, 'P' for Previous or 'B' for Back", align = 'center', font = ("Courier", 24, "normal"))

        count3 = 2
        count7 = 0


        # Keypress
        turtle.listen()
        turtle.onkeypress(next, "n")
        turtle.onkeypress(prev, "p")
        turtle.onkeypress(initial, "b")


def wr_score():

    global l, h, high, list 

    hcopy=h

    p2.clear()

    if h > high :
        h=high

    for i in range(l,h):
        
        p2.goto(-215, 75 - (i-l)*75)
        p2.write(list[i][0], align ='center', font=("Courier", 48, "normal"))

    for i in range(l,h):
        
        p2.goto(215, 75 - (i-l)*75)
        p2.write(list[i][1], align ='center', font=("Courier", 48, "normal"))
        
        if i != h-1:
            
            p.goto(-460, 75 - (i-l)*75)
            p.pendown()
            p.goto(460, 75 - (i-l)*75)
            p.penup()

    h=hcopy


def next():
    
    global l, h, high, count3
    
    if count3 == 2:
        
        count3 = 0
        
        if h < high:
            
            l = l + 5
            h = h + 5
            
            wr_score() 
        
        count3 = 2


def prev():                                                
    
    global l, h, count3
    
    if count3 == 2:
    
        count3 = 0
    
        if l >=5:
    
            l = l - 5
            h = h - 5
    
            wr_score() 
    
        count3 = 2


# Move-Slider A
def up():

    global dx, count2, tascopy
    
    if (t1.ycor() < 200 and not dx == 0) and count2 == 1  and  tascopy == 0 :
        
        for i in range(2):
            t1.forward(15)


def down():
    
    global dx, count2, tascopy
    
    if (t1.ycor() > -200 and not dx == 0) and count2 == 1 and  tascopy == 0 :
        
        for i in range(2):
            t1.backward(15)


# Move-Slider B
def up2():
    
    global dx, count2, tascopy
    
    if (t2.ycor() < 200 and not dx == 0) and count2 == 1 and  tascopy == 0 :
        
        for i in range(2):
            t2.forward(15)


def down2():
    
    global dx, count2, tascopy
    
    if (t2.ycor() > - 200 and not dx == 0) and count2 == 1 and  tascopy == 0 :
        
        for i in range(2):
            t2.backward(15)


def game():
    
    global dt, dtcopy, a, b, z, dx, dy, n, mult, multcopy, ch, countf, count2, tas, tascopy
    
    countf = 0

    p2.goto(0, -60)

    count2 = 0

    # Timer
    for i in range(5, -1, -1):
        
        winsound.PlaySound(r"Items\Game_Action.wav", winsound.SND_ASYNC)
        
        p2.write(i, align = "center", font = ("Courier", 72, "bold"))
        t.wait(1)
        p2.clear()

    count2 = 1

    # GameLoop
    while n == 0:
        
        # Updating Screen
        sc.update()

        no = 0

        # Ball move
        
        # Time Delay
        if tascopy== tas:

            s=perf_counter_ns()
            k=s+1000000000*dt
            e=perf_counter_ns()

            while e<k:
                e=perf_counter_ns()
        

        else:
            
            tascopy=tas
            t1.goto(-550, 0)
            t2.goto(550, 0)


        #Move
        l=int(r.xcor()+dx*mult)

        if abs(l) <= 530 or ch == 1 :
            
            r.goto(int(r.xcor()+dx*mult), int(r.ycor()+dy))
        
        elif ch == 0 :
            
            r.goto(int(530*dx/abs(dx)), int(r.ycor()+(((530-abs(r.xcor()))/abs(dx*mult))*dy)))
            ch = 1


        # Hit
        if ((r.xcor() == -530 and ((r.ycor() < t1.ycor() + 55) and (r.ycor() > t1.ycor() - 55))) or (r.xcor() == 530 and ((r.ycor() < t2.ycor() + 55) and (r.ycor() > t2.ycor() - 55)))) and abs(r.ycor()) >= 240 :
            
            ch = 0
            no = 1
            
            winsound.PlaySound(r"Items\Bounce.wav", winsound.SND_ASYNC)
            
            dx = -dx
            dy = -dy
            
            if dy <= 0:
                
                dy = 0
                sety()
                dy = -abs(dy)
            
            elif dy > 0:
                
                dy = 0
                sety()
                dy = abs(dy)


        elif (r.xcor() == -530 and ((r.ycor() < t1.ycor() + 55) and (r.ycor() > t1.ycor() - 55))) or (r.xcor() == 530 and ((r.ycor() < t2.ycor() + 55) and (r.ycor() > t2.ycor() - 55))):
            
            ch = 0
            
            winsound.PlaySound(r"Items\Bounce.wav", winsound.SND_ASYNC)
            
            dx = -dx
            
            if dy <= 0:
                
                dy = 0
                sety()
                dy = -abs(dy)
            
            elif dy > 0:
                
                dy = 0
                sety()
                dy = abs(dy)
    

        # Boundary
        if abs(r.xcor()) >= 550:
            
            tas = 1
            tascopy = 1

            z = z*(-1)

            winsound.PlaySound(r"Items\Game_Action.wav", winsound.SND_ASYNC)
            
            ch = 0
            
            r.color("black")
            
            if r.xcor() <= -550:
            
                b += 15
            
            elif r.xcor() >= 550:
            
                a += 15
            
            r.goto(0, 0)
            r.color("green")
            
            if not dy == 0:
            
                dy = 0
            
            pen.clear()
            pen.write("Player A : {}  Player B : {}".format(a, b), align = "center", font=("Courier", 24, "normal"))
            
            dx = z*abs(dx)
            
            t1.goto(-550, 0)
            t2.goto(550, 0)

            t.wait(1.5)

            tas = 0

            t1.goto(-550, 0)
            t2.goto(550, 0)


        elif abs(r.ycor()) >= 240 and no == 0 :
            winsound.PlaySound(r"Items\Bounce_Wall.wav", winsound.SND_ASYNC)
            dy = -dy

        sc._root.protocol("WM_DELETE_WINDOW", f7)


        # Keypress
        turtle.listen()
        turtle.onkey(up, "w")
        turtle.onkey(down, "s")
        turtle.onkey(up2, "Up")
        turtle.onkey(down2, "Down")
        turtle.onkeypress(pause, "p")
        turtle.onkeypress(end, "l")
        turtle.onkeypress(f7, "Escape")
        turtle.onkeypress(menu, "Return")
        

def pause():
    
    if count2 == 1:
    
        global dx, dy, copy1, copy2
    
        winsound.PlaySound(r"Items\Game_Action.wav", winsound.SND_ASYNC)
    
        if not dx == 0:
    
            copy1, copy2 = dx, dy
            dx, dy = 0, 0
            
            p2.write("Paused.", align = "center", font = ("Courier", 72, "bold"))
        
        else:
        
            p2.clear()
            dx, dy = copy1, copy2
            
            t.wait(1)


def end():
    
    global n, a, b, v, ch, countf, count2, count5
    
    if count2 == 1 :
        
        countf = 1
        count2 = 0
    
        winsound.PlaySound(r"Items\Game_Action.wav", winsound.SND_FILENAME)
    
        winsound.PlaySound(r"Items\Game_Music_WAV.wav", winsound.SND_LOOP+winsound.SND_ASYNC)
    
        p2.clear()
    
        ch = 0
        n = 1
        v = 1
    
        x.clear()
    
        r.hideturtle()
        r.goto(0, 0)
    
        t1.hideturtle()
        t2.hideturtle()
        t1.goto(-550, 0)
        t2.goto(550, 0)
    
        p2.goto(0, 0)
        p.clear()
    
        pen.clear()
    
        p.goto(-330, 200)
        p.color('white')
        p.write("Player A : {}  Player B : {}".format(a, b), font=("Courier", 24, "normal"))
        p.goto(-330, 150)
    
        if a > b:
    
            p.write("Congratulations to Player A", font=("Courier", 24, "normal"))
    
        elif a < b:
    
            p.write("Congratulations to Player B", font=("Courier", 24, "normal"))
    
        else:
    
            p.write("Congratulations to both Player A and Player B.", font=("Courier", 24, "normal"))
    
        p.goto(-330, 100)
        p.write("Press Enter for Menu.", font=("Courier", 24, "normal"))
        p.goto(-330, 50)
        p.write("Press Esc to Quit.", font=("Courier", 24, "normal"))
    
        with open(r'Items\score.csv','a',newline='') as csvfile:
        
            csvwriter = csv.writer(csvfile)
        
            sc=[a,b]
        
            csvwriter.writerow(sc)
            csvfile.flush()
        
        count5 = 1
    


def menu():
    
    global n, a, b, v, dt, z, dx, dy, copy1, copy2, dtcopy, mult, multcopy, ch, count1, count2, count5, count7
    
    if v == 1 and count2 == 0 and count5 == 1 :

        count5 = 0
    
        p.clear()
        
        a = 0
        b = 0
        v = 0
        ch = 0
        dt = 0.005
        dtcopy = dt
        mult = 1.25
        multcopy = mult
        z = 1
        dx = 10
        choice = random.randint(1, 2)
        if choice == 2:
            z = -1
        dx = z*dx
        dy = 0
        n = 1
        copy1 = 0
        copy2 = 0
        count1 = 0
        count7 = 0
        
        initial()
    
 
# 1st initial Turtle
p = turtle.Turtle()
p.penup()
p.hideturtle()
p.color('white')

# 2nd initial Turtle
p2 = turtle.Turtle()
p2.hideturtle()
p2.penup()
p2.color('white')


def initial():

    # Initial writing
    global count, count1, count3, count4, count6, count7, m

    if count3 == 2:
        
        count3 = 1

    if count3 == 1 and count7 == 0 :

        count1 = 0
        count4 = 0
        count7 = 1
        count = 0

        p2.clear()
        p.clear()

        winsound.PlaySound(r"Items\Game_Action.wav", winsound.SND_ASYNC)
        
        winsound.PlaySound(r"Items\Game_Music_WAV.wav", winsound.SND_LOOP+winsound.SND_ASYNC)

        d5()
        
        p2.goto(250, 50)
        p.goto(-330, 250)
        p.write("Select Mode(By default- Medium) :-", font=("Courier", 24, "underline"))
        
        p.goto(-330, 200)
        p.write("1) Easy", font=("Courier", 24, "normal"))
        
        p.goto(-330, 150)
        p.write("2) Medium", font=("Courier", 24, "normal"))
        
        p.goto(-330, 100)
        p.write("3) Pro", font=("Courier", 24, "normal"))
        
        p.goto(-330, 50)
        p.write("Enter Your Choice (1,2 or 3) :", font=("Courier", 24, "normal"))
        
        p.goto(-330, 0)
        p.write("Press Backspace to choose again.", font=("Courier", 24, "normal"))
        
        p.goto(-330, -50)
        p.write("Press Enter to start a new game.", font=("Courier", 24, "normal"))
        
        p.goto(-330, -100)
        p.write("Game Instructions :-", font=("Courier", 24, "underline"))
        
        p.goto(-330, -150)
        p.write("Use W, S (for moving Player A racket).", font=("Courier", 24, "normal"))
        
        p.goto(-330, -200)
        p.write("Use Up, Down keys (for moving Player B racket).", font=("Courier", 24, "normal"))
        
        p.goto(-330, -250)
        p.write("Press 'H' to view scores of previous matches.", font=("Courier", 24, "normal"))
        
        p.goto(-330, -300)
        p.write("Press Esc to exit.", font=("Courier", 24, "normal"))

        count1 = 1
        m = 1
        count6 = 1


        # KeyPress
        turtle.listen()
        turtle.onkeypress(a1, "1")
        turtle.onkeypress(b2, "2")
        turtle.onkeypress(c3, "3")
        turtle.onkeypress(d4, "BackSpace")
        turtle.onkeypress(e5, "Return")
        turtle.onkeypress(f6, "Escape")
        turtle.onkeypress(g7, "h")



initial()


turtle.done()
