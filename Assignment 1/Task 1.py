from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

def draw_points(x, y):
    glPointSize(4) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def iterate(): #display
    glViewport(0, 0, 1000,1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000,0.0, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw_tri():
    #outer
    glColor3f(.3, .7, .5)
    glBegin(GL_TRIANGLES)
    glVertex3f(70, 270,0)
    glColor3f(.3, .7, .5)
    glVertex3f(250, 350,0)
    glColor3f(.3, .7, .5)
    glVertex3f(430, 270,0)
    glColor3f(.3, .7, .5)

    #inner
    glColor3f(1,1,1)
    glVertex3f(135, 285, 0)#l
    glColor3f(0,1,1)
    glVertex3f(250, 330, 0)#mid
    glColor3f(1,1,1)
    glVertex3f(365, 285, 0)#r
    glColor3f(1,1,1)

    glEnd()

def draw_line(stx,sty,ex,ey,width):
    glLineWidth(width)
    glBegin(GL_LINES)
    glColor3f(.3,.7,.5)
    glVertex2f(stx, sty)
    glVertex2f(ex,ey)
    glEnd()

def drawhouse():
    # body
    draw_line(100, 70, 100, 270, 10)  # L
    draw_line(400, 70, 400, 270, 10)  # R
    draw_line(95, 70, 405, 70, 10)  # B

    glBegin(GL_QUADS)  # outer
    glColor3f(.5, .5, .5)
    glVertex2d(70, 50)
    glColor3f(.5, .5, .5)
    glVertex2d(70, 80)
    glColor3f(.5, .5, .5)
    glVertex2d(420, 80)
    glColor3f(.5, .5, .5)
    glVertex2d(420, 50)
    glColor3f(.5, .5, .5)
    glEnd()

    # roof
    draw_tri()

    # door
    draw_line(170, 80, 170, 180, 1)  # L
    draw_line(230, 80, 230, 180, 1)  # R
    draw_line(170, 180, 230, 180, 1)  # T
    draw_points(220, 120)  # knob

    # window

    glBegin(GL_QUADS)  # outer
    glColor3f(.3,.7,.5)
    glVertex2d(300, 150)
    glColor3f(.3,.7,.5)
    glVertex2d(365, 150)
    glColor3f(.3,.7,.5)
    glVertex2d(365, 220)
    glColor3f(.3,.7,.5)
    glVertex2d(300, 220)
    glColor3f(.3,.7,.5)
    glEnd()


    glBegin(GL_QUADS)  # inner
    glColor3f(0.5, .5, .5)
    glVertex2d(301, 151)
    glColor3f(0.5, .5, .5)
    glVertex2d(364, 151)
    glColor3f(0.5, .5, .5)
    glVertex2d(364, 219)
    glColor3f(0.5, .5, .5)
    glVertex2d(301, 219)
    glColor3f(0.5, .5, .5)
    glEnd()

    draw_line(332.5, 150, 332.5, 220, 1)  # Y- Axis
    draw_line(300, 185, 365, 185, 1)  # X- axis



num_raindrops = 100
drops = [(random.uniform(10, 490), random.uniform(100, 500)) for _ in range(num_raindrops)]

def rain():
    global angle
    global drops
    for i in range(len(drops)):
        a, b = drops[i]
        a += angle
        b -= speed  # Adjust raindrop position based on speed
                    # fistly used parameters
        if b < 50 or (70 < a < 430 and 100 < b < 270):
            a = random.uniform(10, 490)
            b = random.uniform(10, 500)


        drops[i] = (a, b)

def drawdrop(x, y):
    glColor3f(0, 0, 1)
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def draw_raindrops():
    glBegin(GL_LINES)
    glColor3f(0.5, 0.5, 0.5)
    for x, y in drops:
        glVertex2f(x, y)
        glVertex2f(x, y - 0.02)
    glEnd()

def startrain():
    for i in drops:
        drawdrop(i[0], i[1])


def animate():
    global speed
    rain()
    glutPostRedisplay()






daynight=(1,1,1,1)
def keyboardListener(key, x, y): # day night shift
    global daynight
    if (key == b'n'):
        daynight= (0,0,0,0)
        print("Night mode")
    if (key == b'd'):
        daynight= (1,1,1,1)
        print("Day mode")
    glutPostRedisplay()

angle= 0
speed= 3
def specialKeyListener(key, x, y):
    global angle
    global speed
    if key == GLUT_KEY_RIGHT:
        angle += 0.2
        print("Right Tilt")
    if key == GLUT_KEY_LEFT:
        angle -= 0.2
        print("Left Tilt")

    if key == GLUT_KEY_UP:
        speed *= 2
        print("Speed Increased",'Current speed:', speed)
    if key == GLUT_KEY_DOWN:  # // up arrow key
        speed /= 2
        print("Speed Decreased",'Current speed:', speed)
    if key == GLUT_KEY_END:
        speed=0
        print("Paused Rain")
    if key == GLUT_KEY_HOME:
        speed= 1
        print("Started rain")

    glutPostRedisplay()

def showScreen():
    glClearColor(*daynight)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    #call the draw methods here
    drawhouse()
    startrain()
    glutSwapBuffers()




glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b" A1 T1 ") #window name
glutDisplayFunc(showScreen)
glutIdleFunc(animate)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMainLoop()