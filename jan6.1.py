# jan6
import turtle
import random

turtle.colormode(255)
board = turtle.Turtle()

def getColor():
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)

    return r, g, b

def drawT(t, pen = "red", fill = "yellow"):

    board.penup()
    board.goto(t[0][0], t[0][1])
    board.pendown()

    board.color(pen, fill) 
    board.begin_fill()
    board.goto(t[1][0], t[1][1])
    board.goto(t[2][0], t[2][1])
    board.goto(t[0][0], t[0][1])
    board.end_fill()
   
def drawTs(ts, pen = "red", fill = "yellow"):
    for t in ts:
        drawT(t, pen, fill)

def createT(v1, v2, v3):
    return [v1, v2, v3]

def multV(v, x):
    return [v[0] * x, v[1] * x]

def diffE(e):
    return [e[0][0] - e[1][0], e[0][1] - e[1][1]]

def addV(v1, v2):
    return [v1[0] + v2[0], v1[1] + v2[1]]

def splitT(t, r = 0):

    v1 = t[0]
    v2 = t[1]
    v3 = t[2]

    e1 = [v1, v2]
    e2 = [v2, v3]
    e3 = [v3, v1]

    rr = 0
    if r != 0:
        rr = random.uniform(-r, r)

    vd1 = diffE(e1)
    vd1 = multV(vd1, -0.5 + rr)
    ve1 = addV(v1, vd1)

    vd2 = diffE(e2)
    vd2 = multV(vd2, -0.5 + rr)
    ve2 = addV(v2, vd2)
    
    vd3 = diffE(e3)
    vd3 = multV(vd3, -0.5 + rr)
    ve3 = addV(v3, vd3)
    
    t1 = [v1, ve1, ve3]
    t2 = [ve3, ve1, ve2]
    t3 = [ve1, v2, ve2]
    t4 = [ve3, ve2, v3]

    return [t1, t2, t3, t4]

def splitTs(ts, r = 0):
    newts = []
    for t in ts:
        splits = splitT(t, r)
        newts = newts + splits

    return newts

t1 = createT([0,0], [50,100], [100,0])
t2 = createT([0,0], [50,-100], [100,0])

ts = [t1, t2]

drawTs(ts)

splits = splitTs(ts, 0.5)

drawTs(splits, getColor(), getColor())

splits = splitTs(splits, 0.5)

drawTs(splits, getColor(), getColor())

turtle.done()