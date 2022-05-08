# Simple Analog Clock in Python 3

import time
import turtle
import datetime

# Creating Window Screen 
wind = turtle.Screen() #creates screen variable
wind.bgcolor("antique white") #sets background colour to black
wind.setup(width=1540, height=800) #sets screen dimensions



# Create drawing pen
pen = turtle.Turtle() #creates drawing pen variable
pen.hideturtle() #hides pen when drawing
pen.speed(1) #sets pen to draw at fastest speed
pen.pensize(20)

back_pen = turtle.Turtle() #creates drawing pen variable
back_pen.hideturtle() #hides pen when drawing
back_pen.speed(0) #sets pen to draw at fastest speed
back_pen.pensize(5) #width that the pen is drawing


turtle.delay(0)
turtle.tracer(0,0)


# creating turtle pen 
t = turtle.Turtle()
t.speed(0)

col1 = "bisque"
col2 = "peach puff"
col3 = "moccasin"
col4 = "papaya whip"
col5 = "old lace"

    
# set the fillcolor 


# 1
t.pencolor(col1)
t.fillcolor(col1)
t.penup()
t.goto(100, -400)
t.pendown()

t.begin_fill() 
t.goto(-500, 400)
t.goto(-770, -400)
t.goto(400, -400)
t.end_fill() 


# 2
t.pencolor(col2)
t.fillcolor(col2)
t.penup()
t.goto(770, 400)
t.pendown()

t.begin_fill() 
t.goto(770, -400)
t.goto(-200, -400)
t.goto(770, 400)
t.end_fill()


# 3
t.pencolor(col3)
t.fillcolor(col3)
t.penup()
t.goto(-770, 400)
t.pendown()

t.begin_fill() 
t.goto(-350, 400)
t.goto(-500, -400)
t.goto(-770, -400)
t.goto(-770, 400)
t.end_fill()


# 4
t.pencolor(col4)
t.fillcolor(col4)
t.penup()
t.goto(770, -250)
t.pendown()

t.begin_fill() 
t.goto(770, 400)
t.goto(570, 260)
t.goto(770, -200)
t.end_fill()


# 5
t.pencolor(col5)
t.pencolor(col5)
t.penup()
t.goto(720, 450)
t.pensize(180)
t.setheading(225) # needed to adjust heading
t.pendown()

t.forward(1300)


    
# Drawing clock
    
class Clock:
    h_angle = 0  #hour hand angle
    m_angle = 0  #minute hand angle
    px = 0  #clock's position on x-axis
    py = 0 #clock's position on y-axis
    r = 54  #radius of clock

    def __init__(self,h_angle,m_angle,px,py,r):
        self.h_angle = h_angle
        self.m_angle = m_angle
        self.px = px
        self.py = py
        self.r = r

    def draw_background(self,back_pen):

        # Draw clock face
        back_pen.up() #does not draw clock
        back_pen.goto(self.px, self.py + self.r) #moves variable to centre of circle
        back_pen.setheading(180) #sets direction - left
        back_pen.color("cornflower blue") #sets color of drawing pen ink to white
        back_pen.pendown() #pen is on screen to draw
        back_pen.circle(self.r) #creates circle of radius 210

    def draw_clock(self,pen):
        
        # Draw hourhand
        pen.penup()
        pen.goto(self.px, self.py)
        pen.pencolor("cornflower blue")
        pen.setheading(90) #sets direction upwards
        pen.rt(self.h_angle)
        pen.pendown()
        pen.fd(45)

        pen.penup()
        pen.goto(self.px, self.py)
        pen.pencolor("cornflower blue")
        pen.setheading(90) #sets direction upwards
        pen.rt(self.m_angle)
        pen.pendown()
        pen.fd(45)

    def animate(self, new_angleH, new_angleM, anim_type): # general animation function to pick the correct animation type for all columns

        if anim_type == "normal":
            self.animate_normal(new_angleH, new_angleM)

        if anim_type == "before wavey":
            self.animate_normal(new_angleH, new_angleM)


    # Animates to digital clock    

    def animate_normal(self, new_angleH, new_angleM):
        if new_angleH != self.h_angle:
            self.h_angle += 3

        if new_angleM != self.m_angle:
            self.m_angle += 3
            

        if self.h_angle == 360: #if angle is 360, it should be at 0
            self.h_angle = 0

        if self.m_angle == 360: #if angle is 360, it should be at 0
            self.m_angle = 0


    # Animates Wavey animation
    
    def animate_col(self, anim_type): # continous animation function to pick the correct animation type for specified columns

        if anim_type == "wave":
            self.animate_wave()


    def animate_wave(self):

        self.h_angle += 3 #changes the angle every second differently 

        self.m_angle += 3
            

        if self.h_angle == 360: #if angle is 360, it should be at 0
            self.h_angle = 0

        if self.m_angle == 360: #if angle is 360, it should be at 0
            self.m_angle = 0


## TURNING SQUARES 
    def turning1(self):

        if self.h_angle == 0: #if angle is 360, it should be at 0
            self.h_angle = 360
        if self.m_angle == 360: #if angle is 360, it should be at 0
            self.m_angle = 0
            
        self.h_angle -= 3 #changes the angle every second differently 
        self.m_angle += 3


    def turning2(self):

        if self.h_angle == 360: #if angle is 360, it should be at 0
            self.h_angle = 0
        if self.m_angle == 0: #if angle is 360, it should be at 0
            self.m_angle = 360
            
        self.h_angle += 3 #changes the angle every second differently 
        self.m_angle -= 3


    def turning3(self):

        if self.h_angle == 360: #if angle is 360, it should be at 0
            self.h_angle = 0
        if self.m_angle == 0: #if angle is 360, it should be at 0
            self.m_angle = 360

        self.h_angle += 3 #changes the angle every second differently 
        self.m_angle -= 3


    def turning4(self):

        if self.h_angle == 0: #if angle is 360, it should be at 0
            self.h_angle = 360
        if self.m_angle == 360: #if angle is 360, it should be at 0
            self.m_angle = 0
            
        self.h_angle -= 3 #changes the angle every second differently 
        self.m_angle += 3
            

    def animatewide(self):
        
        self.h_angle += 3 #changes the angle every second differently 

        self.m_angle -= 3
            

        if self.h_angle == 360: #if angle is 360, it should be at 0
            self.h_angle = 0

        if self.m_angle == 0: #if angle is 360, it should be at 0
            self.m_angle = 360   


def clock_digits(connected_digits, clocks, frame_clocks): # Draws all digits out
    anim_type = "normal"
    clock_set = 0

    
    for i in connected_digits:
        
        if i == 0:
            clocks[clock_set][0].animate(90, 180, anim_type)
            clocks[clock_set][1].animate(0, 180, anim_type)
            clocks[clock_set][2].animate(0, 180, anim_type)
            clocks[clock_set][3].animate(0, 90, anim_type)
            clocks[clock_set][4].animate(180, 270, anim_type)
            clocks[clock_set][5].animate(0, 180, anim_type)
            clocks[clock_set][6].animate(0, 180, anim_type)
            clocks[clock_set][7].animate(0, 270, anim_type)
            
        elif i == 1:
            clocks[clock_set][0].animate(45, 225, anim_type)
            clocks[clock_set][1].animate(45, 225, anim_type)
            clocks[clock_set][2].animate(45, 225, anim_type)
            clocks[clock_set][3].animate(45, 225, anim_type)
            clocks[clock_set][4].animate(180, 180, anim_type)
            clocks[clock_set][5].animate(0, 180, anim_type)
            clocks[clock_set][6].animate(0, 180, anim_type)
            clocks[clock_set][7].animate(0, 0, anim_type)

        elif i == 2:
            clocks[clock_set][0].animate(90, 90, anim_type)
            clocks[clock_set][1].animate(90, 180, anim_type)
            clocks[clock_set][2].animate(0, 180, anim_type)
            clocks[clock_set][3].animate(0, 90, anim_type)
            clocks[clock_set][4].animate(180, 270, anim_type)
            clocks[clock_set][5].animate(0, 270, anim_type)
            clocks[clock_set][6].animate(45, 225, anim_type)
            clocks[clock_set][7].animate(270, 270, anim_type)

        elif i == 3:
            clocks[clock_set][0].animate(90, 90, anim_type)
            clocks[clock_set][1].animate(90, 90, anim_type)
            clocks[clock_set][2].animate(45, 225, anim_type)
            clocks[clock_set][3].animate(90, 90, anim_type)
            clocks[clock_set][4].animate(270, 180, anim_type)
            clocks[clock_set][5].animate(0, 270, anim_type)
            clocks[clock_set][6].animate(0, 180, anim_type)
            clocks[clock_set][7].animate(0, 270, anim_type)

        elif i == 4:
            clocks[clock_set][0].animate(180, 180, anim_type)
            clocks[clock_set][1].animate(0, 90, anim_type)
            clocks[clock_set][2].animate(45, 225, anim_type)
            clocks[clock_set][3].animate(45, 225, anim_type)
            clocks[clock_set][4].animate(180, 180, anim_type)
            clocks[clock_set][5].animate(0, 180, anim_type)
            clocks[clock_set][6].animate(0, 180, anim_type)
            clocks[clock_set][7].animate(0, 0, anim_type)
            
        elif i == 5:
            clocks[clock_set][0].animate(90, 180, anim_type)
            clocks[clock_set][1].animate(0, 90, anim_type)
            clocks[clock_set][2].animate(45, 225, anim_type)
            clocks[clock_set][3].animate(90, 90, anim_type)
            clocks[clock_set][4].animate(270, 270, anim_type)
            clocks[clock_set][5].animate(180, 270, anim_type)
            clocks[clock_set][6].animate(0, 180, anim_type)
            clocks[clock_set][7].animate(0, 270, anim_type)

        elif i == 6:
            clocks[clock_set][0].animate(90, 180, anim_type)
            clocks[clock_set][1].animate(0, 180, anim_type)
            clocks[clock_set][2].animate(0, 180, anim_type)
            clocks[clock_set][3].animate(0, 90, anim_type)
            clocks[clock_set][4].animate(270, 270, anim_type)
            clocks[clock_set][5].animate(45, 225, anim_type)
            clocks[clock_set][6].animate(180, 270, anim_type)
            clocks[clock_set][7].animate(0, 270, anim_type)

        elif i == 7:
            clocks[clock_set][0].animate(90, 90, anim_type)
            clocks[clock_set][1].animate(45, 225, anim_type)
            clocks[clock_set][2].animate(45, 225, anim_type)
            clocks[clock_set][3].animate(45, 225, anim_type)
            clocks[clock_set][4].animate(180, 270, anim_type)
            clocks[clock_set][5].animate(0, 180, anim_type)
            clocks[clock_set][6].animate(0, 180, anim_type)
            clocks[clock_set][7].animate(0, 0, anim_type)

        elif i == 8:
            clocks[clock_set][0].animate(90, 180, anim_type)
            clocks[clock_set][1].animate(0, 90, anim_type)
            clocks[clock_set][2].animate(0, 180, anim_type)
            clocks[clock_set][3].animate(0, 90, anim_type)
            clocks[clock_set][4].animate(180, 270, anim_type)
            clocks[clock_set][5].animate(0, 270, anim_type)
            clocks[clock_set][6].animate(0, 180, anim_type)
            clocks[clock_set][7].animate(0, 270, anim_type)

        elif i == 9:
            clocks[clock_set][0].animate(90, 180, anim_type)
            clocks[clock_set][1].animate(0, 90, anim_type)
            clocks[clock_set][2].animate(45, 225, anim_type)
            clocks[clock_set][3].animate(45, 225, anim_type)
            clocks[clock_set][4].animate(180, 270, anim_type)
            clocks[clock_set][5].animate(0, 180, anim_type)
            clocks[clock_set][6].animate(0, 180, anim_type)
            clocks[clock_set][7].animate(0, 0, anim_type)

        elif i == ":":
            clocks[2][0].animate(90, 180, anim_type)
            clocks[2][1].animate(0, 90, anim_type)
            clocks[2][2].animate(90, 180, anim_type)
            clocks[2][3].animate(0, 90, anim_type)
            clocks[2][4].animate(180, 270, anim_type)
            clocks[2][5].animate(0, 270, anim_type)
            clocks[2][6].animate(180, 270, anim_type)
            clocks[2][7].animate(0, 270, anim_type)

        clock_set += 1

    for i in range(10):
        frame_clocks[0][i].animate(270, 90, anim_type)

    frame_clocks[1][0].animate(90, 0, anim_type)

    for i in range(4):
        frame_clocks[1][i+1].animate(0,180, anim_type)

    frame_clocks[1][5].animate(180, 90, anim_type)

    for i in range(10):
        frame_clocks[2][i].animate(270, 90, anim_type)

    frame_clocks[3][0].animate(270, 180, anim_type)

    for i in range(4):
        frame_clocks[3][i+1].animate(0, 180, anim_type)

    frame_clocks[3][5].animate(270, 0, anim_type)


                
def analog_clock(h, m, clocks): #turns all clock to analog clock
    anim_type = "normal"

    hour = (((h%12) + m/60) / 12) * 360  #changed hour hand to angle of cirlce
    hour = hour - (hour % 3)

    minute = (m / 60) * 360 #changed minute hands to angle of circle
    minute = minute - (minute % 3)

    

    for i in clocks[0:9]:
        for clock in i:
            clock.animate(hour, minute, anim_type)


def wavey_getready(clocks):
    anim_type = "normal"
    
    hour = 0

    minute = 0

    for i in clocks[0:9]:
        for clock in i:
            clock.animate(hour, minute, anim_type)


def AFTER_GROUPS(groups):
    anim_type = "normal"
    
    hour = 0

    minute = 0

    for i in groups:
        for clock in i:
            clock.animate(hour, minute, anim_type)
            

def wavey(clocks, clock_cols):
    anim_type = "wave"
    
    for i in clock_cols:
        for clock in columns[i]: #every time clock_cols increases, one column is increased 
            clock.animate_col(anim_type)



def turningsquare_getready(groups):
    anim_type = "normal"

    for i in range(18):
        groups[0][i].animate(90,180, anim_type)
        groups[1][i].animate(270,180, anim_type)
        groups[2][i].animate(90,0, anim_type)
        groups[3][i].animate(270, 0, anim_type)

def turningsquare(clocks):

    for i in range(18):
        groups[0][i].turning1()
        groups[1][i].turning2()
        groups[2][i].turning3()
        groups[3][i].turning4()


                
## BEFORE ACTIONS        
clocks = [[],[],[],[],[],[],[],[],[]] #a list represnting set of 8 clocks that represents a digit and framed clocks
columns = [[],[],[],[],[],[],[],[],[],[],[],[]]
groups = [[],[],[],[]]
frame_clocks = [[],[],[],[]]

## INITIAL CLOCKS
x = 18
n_column = 0

# Adds initial clocks to list


for i in range(5):
    clocks[i].append(Clock(0, 0, -770 + 11*x + n_column, 400 - 11*x, 3*x))
    clocks[i].append(Clock(0, 0, -770 + 11*x + n_column, 400 - 18*x, 3*x))
    clocks[i].append(Clock(0, 0, -770 + 11*x + n_column, 400 - 25*x, 3*x))
    clocks[i].append(Clock(0, 0, -770 + 11*x + n_column, 400 - 32*x, 3*x))
    clocks[i].append(Clock(0, 0, -770 + 18*x + n_column, 400 - 11*x, 3*x))
    clocks[i].append(Clock(0, 0, -770 + 18*x + n_column, 400 - 18*x, 3*x))
    clocks[i].append(Clock(0, 0, -770 + 18*x + n_column, 400 - 25*x, 3*x))
    clocks[i].append(Clock(0, 0, -770 + 18*x + n_column, 400 - 32*x, 3*x))
    n_column += 14*x




# Adds initial frame around clocks

n_column = 0

## BOTTOM FRAME CLOCKS
for _ in range(10):
    frame_clocks[0].append(Clock(0, 0, - 770 + 74*x - n_column, 400 - 39*x, 3*x))
    n_column += 7*x

n_column = 0

## LEFT FRAME CLOCKS
for _ in range(6):
    frame_clocks[1].append(Clock(0, 0, - 770 + 4*x, 400 - 39*x + n_column, 3*x))
    n_column += 7*x


n_column = 0

## TOP FRAME CLOCKS
for _ in range(10):
    frame_clocks[2].append(Clock(0, 0, - 770 + 11*x + n_column, 400 - 4*x, 3*x))
    n_column += 7*x


n_column = 0

## RIGHT FRAME CLOCKS
for _ in range(6):
    frame_clocks[3].append(Clock(0, 0, - 770 + 81*x, 400 - 4*x - n_column, 3*x))
    n_column += 7*x

clocks[5] = frame_clocks[0]
clocks[6] = frame_clocks[1]
clocks[7] = frame_clocks[2]
clocks[8] = frame_clocks[3]

# Add column group
columns[0] = frame_clocks[1][0:6]
columns[1] = clocks[0][0:4]
columns[1].append(frame_clocks[0][9])
columns[1].append(frame_clocks[2][0])
columns[2] = clocks[0][4:8]
columns[2].append(frame_clocks[0][8])
columns[2].append(frame_clocks[2][1])
columns[3] = clocks[1][0:4]
columns[3].append(frame_clocks[0][7])
columns[3].append(frame_clocks[2][2])
columns[4] = clocks[1][4:8]
columns[4].append(frame_clocks[0][6])
columns[4].append(frame_clocks[2][3])
columns[5] = clocks[2][0:4]
columns[5].append(frame_clocks[0][5])
columns[5].append(frame_clocks[2][4])
columns[6] = clocks[2][4:8]
columns[6].append(frame_clocks[0][4])
columns[6].append(frame_clocks[2][5])
columns[7] = clocks[3][0:4]
columns[7].append(frame_clocks[0][3])
columns[7].append(frame_clocks[2][6])
columns[8] = clocks[3][4:8]
columns[8].append(frame_clocks[0][2])
columns[8].append(frame_clocks[2][7])
columns[9] = clocks[4][0:4]
columns[9].append(frame_clocks[0][1])
columns[9].append(frame_clocks[2][8])
columns[10] = clocks[4][4:8]
columns[10].append(frame_clocks[0][0])
columns[10].append(frame_clocks[2][9])
columns[11] = frame_clocks[3][0:6]


# Add clocks to list group

groups[0].append(clocks[6][5]) # 1
groups[1].append(clocks[7][0])
groups[2].append(clocks[6][4])
groups[3].append(clocks[0][0])

groups[0].append(clocks[7][1])
groups[1].append(clocks[7][2])
groups[2].append(clocks[0][4])
groups[3].append(clocks[1][0])

groups[0].append(clocks[7][3])
groups[1].append(clocks[7][4])
groups[2].append(clocks[1][4])
groups[3].append(clocks[2][0])

groups[0].append(clocks[7][5])
groups[1].append(clocks[7][6])
groups[2].append(clocks[2][4])
groups[3].append(clocks[3][0])

groups[0].append(clocks[7][7])
groups[1].append(clocks[7][8])
groups[2].append(clocks[3][4])
groups[3].append(clocks[4][0])

groups[0].append(clocks[7][9])
groups[1].append(clocks[8][0])
groups[2].append(clocks[4][4])
groups[3].append(clocks[8][1])

groups[0].append(clocks[6][3]) # 2
groups[1].append(clocks[0][1])
groups[2].append(clocks[6][2])
groups[3].append(clocks[0][2])

groups[0].append(clocks[0][5])
groups[1].append(clocks[1][1])
groups[2].append(clocks[0][6])
groups[3].append(clocks[1][2])

groups[0].append(clocks[1][5])
groups[1].append(clocks[2][1])
groups[2].append(clocks[1][6])
groups[3].append(clocks[2][2])

groups[0].append(clocks[2][5])
groups[1].append(clocks[3][1])
groups[2].append(clocks[2][6])
groups[3].append(clocks[3][2])

groups[0].append(clocks[3][5])
groups[1].append(clocks[4][1])
groups[2].append(clocks[3][6])
groups[3].append(clocks[4][2])

groups[0].append(clocks[4][5])
groups[1].append(clocks[8][2])
groups[2].append(clocks[4][6])
groups[3].append(clocks[8][3])

groups[0].append(clocks[6][1]) # 3
groups[1].append(clocks[0][3])
groups[2].append(clocks[6][0])
groups[3].append(clocks[5][9])

groups[0].append(clocks[0][7])
groups[1].append(clocks[1][3])
groups[2].append(clocks[5][8])
groups[3].append(clocks[5][7])

groups[0].append(clocks[1][7])
groups[1].append(clocks[2][3])
groups[2].append(clocks[5][6])
groups[3].append(clocks[5][5])

groups[0].append(clocks[2][7])
groups[1].append(clocks[3][3])
groups[2].append(clocks[5][4])
groups[3].append(clocks[5][3])

groups[0].append(clocks[3][7])
groups[1].append(clocks[4][3])
groups[2].append(clocks[5][2])
groups[3].append(clocks[5][1])

groups[0].append(clocks[4][7])
groups[1].append(clocks[8][4])
groups[2].append(clocks[5][0])
groups[3].append(clocks[8][5])




# Prints initial clocks

for i in clocks[0:9]:
    for clock in i:
        clock.draw_background(back_pen)
        clock.draw_clock(pen)


while True:
    current_time=datetime.datetime.now().time()
    h = int(current_time.hour) #gives string formatted time and gives hour
    m = int(current_time.minute) #gives #gives string formatted time and gives minutes
    s = int(current_time.second) #gives string formatted time and gives hour
    ms = current_time.strftime("%f")
    ms = int(ms[:-4]) #cuts off the last four digits

    hour = [int(i) for i in str(h)] #turns it into list 
    minute = [int(i) for i in str(m)] #turns it into list
    second = [int(i) for i in str(s)] #turns seconds into list = seperates digits

    if len(hour) == 1:
        hour.insert(0, int(0))

    hour.append(":")

    if len(minute) == 1:
        minute.insert(0, int(0))

    connected_digits = hour + minute #list of digits in clock



    ## IF MINUTE HAND IS EVEN:
    if m % 3 == 0:
        
        if s >= 0 and s < 20:
            clock_digits(connected_digits, clocks, frame_clocks)  #changes angle to correct angle

        elif s >= 20 and s < 30: #changes all clocks to diagonal position
            wavey_getready(clocks)


        elif s >= 30 and s < 45: #between 18 and 30 seconds
            if s < 42:
                
                clock_cols = range(s-29) #creates a list that changes every second (increased each column (total shoudl have all columns


            wavey(clocks, clock_cols)
            

        elif s >= 45 and s <= 59:
            analog_clock(h, m, clocks) # at 30 seconds, it shows analog clocks


    ## IF MINUTE HAND IS ODD:
    if m % 3 == 1:
        
        if s >= 0 and s < 20:
            clock_digits(connected_digits, clocks, frame_clocks)  #changes angle to correct angle

        elif s >= 20 and s < 37: #changes all clocks to diagonal position
            turningsquare_getready(groups)

        elif s >= 37  and s < 50:
            turningsquare(groups)


        elif s >= 50 and s <= 59:
            analog_clock(h, m, clocks) # at 30 seconds, it shows analog clocks


    ## IF MINUTE HAND IS ODD:  
    if m % 3 == 2:

        if s >= 0 and s < 25:
            clock_digits(connected_digits, clocks, frame_clocks)  #changes angle to correct angle

        elif s >= 25 and s < 40: #between 18 and 30 seconds
            if s < 37:
                
                clock_cols = range(s-24) #creates a list that changes every second (increased each column (total shoudl have all columns

            wavey(clocks, clock_cols)

        elif s >= 40 and s < 49:
            for i in clocks:
                for clock in i:
                    clock.animatewide()

        elif s >= 49 and s <= 59:
            analog_clock(h, m, clocks) # at 30 seconds, it shows analog clocks
    # Draws clock
    
    for i in clocks:
        for clock in i:
            clock.draw_clock(pen)
            

    turtle.update()

    pen.clear()

        






wind.mainloop() #otherwise window will open and close automatically
    
