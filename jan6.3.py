# jan6
import turtle
import random

turtle.colormode(255)
screen = turtle.Screen()

board = turtle.Turtle()


def getColor():
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)

    return r, g, b

def drawT(t, pen = "red", fill = "yellow"):

    board.speed(0)
    board.penup()
    board.goto(t[0][0], t[0][1])
    board.pendown()

    board.color(pen, fill) 
    board.begin_fill()
    board.goto(t[1][0], t[1][1])
    board.goto(t[2][0], t[2][1])
    board.goto(t[0][0], t[0][1])
    board.end_fill()
   
def getScreenDims(ts):
    maxx = 0
    minx = 0
    maxy = 0
    miny = 0
    for t in ts:
        for v in t:
            if v[0] > maxx: maxx = v[0]
            if v[0] < minx: minx = v[0]
            if v[1] > maxy: maxy = v[1]
            if v[1] < miny: miny = v[1]

    dimx = maxx - minx
    dimy = maxy - miny

    return dimx + 50, dimy + 50
    
def drawTs(ts, pen = "red", fill = "yellow"):

    dimx, dimy = getScreenDims(ts)
    screen.setup(dimx, dimy)

    for t in ts:
        drawT(t, getColor(), getColor())

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

def buildT(w, h, e):
    
    woff = (w * e) / 2
    hoff = (h * e) / 2
    ts = []
    for p in range(h):
        yoff = (e * p) - hoff
        for n in range(w):
            xoff = (e * n) + ((e/2) * p) - woff
            t1 = createT([xoff, yoff], [(e/2) + xoff, yoff + e], [e + xoff, yoff])
            ts.append(t1)
            if (p != 0):
                t2 = createT([xoff, yoff], [(e/2) + xoff, yoff - e], [e + xoff, yoff])
                ts.append(t2)
            

        w = w - 1
        
    return ts


ts = buildT(4, 4, 50)

drawTs(ts)
splits = ts
for x in range(3):
    splits = splitTs(splits, 0.25)
    drawTs(splits)


turtle.done()