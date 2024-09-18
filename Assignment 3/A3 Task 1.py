from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 500, 0, 500)
    glMatrixMode(GL_MODELVIEW)

def drawpixel(x, y):
    glPointSize(1)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()

initialz = 0
def zonefinder(x1, y1, x2, y2):
    zone = 0
    global initialz
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) >= abs(dy):
        if dx >= 0:
            if dy >= 0:
                zone=0
            else:
                zone= 7
        else:
            if dy >= 0:
                zone = 3
            else:
                zone = 4
    else:
        if dx >= 0:
            if dy >= 0:
                zone = 1
            else:
                zone = 6
        else:
            if dy >= 0:
                zone = 2
            else:
                zone = 5
    initialz = zone


def drawasZero(x, y, zone):
    if zone == 0:
        drawpixel(x, y)
    elif zone == 1:
        drawpixel(y, x)
    elif zone == 2:
        drawpixel(-y, x)
    elif zone == 3:
        drawpixel(-x, y)
    elif zone == 4:
        drawpixel(-x, -y)
    elif zone == 5:
        drawpixel(-y, -x)
    elif zone == 6:
        drawpixel(y, -x)
    elif zone == 7:
        drawpixel(x, -y)


def MPLDraw(x1, y1, x2, y2, zone):
    dx = x2 - x1
    dy = y2 - y1
    delE = 2 * dy
    delNE = 2 * (dy - dx)
    d = 2 * dy - dx
    x = x1
    y = y1
    while x < x2:
        drawasZero(x, y, zone)
        if d < 0:
            d += delE
            x += 1
        else:
            d += delNE
            x += 1
            y += 1


def drawLine(x1, y1, x2, y2):
    zonefinder(x1, y1, x2, y2)
    global initialz
    if initialz ==0:
        MPLDraw(x1, y1, x2, y2, 0)
    elif initialz == 1:
        MPLDraw(y1, x1, y2, x2, 1)
    elif initialz == 2:
        MPLDraw(y1, -x1, y2, -x2, 2)
    elif initialz == 3:
        MPLDraw(-x1, y1, -x2, y2, 3)
    elif initialz == 4:
        MPLDraw(-x1, -y1, -x2, -y2, 4)
    elif initialz == 5:
        MPLDraw(-y1, -x1, -y2, -x2, 5)
    elif initialz == 6:
        MPLDraw(-y1, x1, -y2, x2, 6)
    elif initialz == 7:
        MPLDraw(x1, y1, -x2, -y2, 7)


def restart():
    glColor3f(0.0, 0, 1)
    drawLine(30, 450, 5, 470)
    drawLine(5, 470, 30, 490)
    drawLine(5, 470, 60, 470)

def pauseonoff():
    global pause
    if pause == True:
        glColor3f(0, 1.0, 0.0)
        drawLine(270, 470, 230, 490)
        drawLine(270, 470, 230, 450)
        drawLine(230, 450, 230, 490)
    else:
        glColor3f(1, 1, 1)
        drawLine(250, 490, 250, 450)
        drawLine(270, 490, 270, 450)


def exitbutton():
    glColor3f(1.0, 0.0, 0.0)
    drawLine(460, 490, 490, 450)
    drawLine(460, 450, 490, 490)

def buttonborder():
    glColor3f(.3, .3, .3)
    drawLine(0, 445, 500, 445)




def MPCDraw(cx, cy, r):
    x = 0
    y = r
    d = 1 - r
    while y > x:
        drawpixel(cx + x, cy + y)
        drawpixel(cx + y, cy + x)
        drawpixel(cx - x, cy + y)
        drawpixel(cx - y, cy + x)
        drawpixel(cx - x, cy - y)
        drawpixel(cx - y, cy - x)
        drawpixel(cx + x, cy - y)
        drawpixel(cx + y, cy - x)

        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1


def drawShooter():
    global shooter_x,sradius,sr,sg,sb
    center_x = shooter_x
    center_y = 20
    radius = sradius
    glColor3f(sr, sg, sb)
    MPCDraw(center_x, center_y, radius)


class Bullet:
    def __init__(self, x):
        self.x = x
        self.y = 20
        self.radius=3.5

    def draw(self):
        glColor3f(1.0, 0, 0)
        MPCDraw(self.x, self.y, self.radius)




class Circle:
    def __init__(self):
        self.radius = random.randint(15, 35)
        self.x = random.randint(self.radius, 500 - self.radius)
        self.y = 445
        self.collision = False

    def colchecker(self, another):
        radialdistance = (self.x - another.x) ** 2 + (self.y - another.y) ** 2
        mindistance = (self.radius + another.radius) ** 2
        return radialdistance < mindistance

    def checkcollision(self, circles):
        for other_circle in circles:
            if other_circle != self:
                if self.colchecker(other_circle):
                    self.collision = True
                    break
        else:
            self.collision = False

    def draw(self):
        if  self.collision == False:
            glColor3f(0, 0.5, 1)
            MPCDraw(self.x, self.y, self.radius)








def specialKeyListener(key, x, y):
    global shooter_x, bullets, gameover
    if gameover==False and pause==False:
            if key == GLUT_KEY_LEFT:
                if shooter_x >= 20:
                    shooter_x -= 7
            if key == GLUT_KEY_RIGHT:
                if shooter_x <= 480:
                    shooter_x += 7
            if key == GLUT_KEY_UP:
                b = Bullet(shooter_x)
                bullets.append(b)
    glutPostRedisplay()


def keyboardListener(key, x, y):
    global shooter_x, bullets, gameover,speed
    if gameover==False and pause==False:
        if key == b'a':
            if shooter_x >= 20:
                shooter_x -= 7
        if key == b'd':
            if shooter_x <= 480:
                shooter_x += 7
        if key == b' ':
            b = Bullet(shooter_x)
            bullets.append(b)
        if key == b'h':
            speed+= 1
    glutPostRedisplay()




def mouseListener(button, state, x, y):
    global pause,score, gameover, bullets, circles
    if button == GLUT_LEFT_BUTTON:
        if (state == GLUT_DOWN):
            if y<=50:
                if 0<=x<=60:
                    bullets=[]
                    circles=[]
                    gameover=False
                    print(f"Final Score: {score}")
                    print(f"Restarting...")
                    print(f"Started Over")
                    score=0
                if 230 <= x <= 280:
                    if pause == False:
                        print("Game paused")
                        pause=True
                    else:
                        pause=False
                        print("Game resumed")
                if 460<=x<=490:
                    print(f"Exiting...")
                    print(f"Goodbye! Final Score {score}")
                    glutLeaveMainLoop()
    glutPostRedisplay()




speed = .3
def animate():
    global speed
    global bullets, circles,score,missed,gameover,surfaceshot, pause ,sradius,sr,sg,sb
    if gameover==False and pause==False:
        bullets_to_remove = []
        cir_to_remove = []

        for bullet in bullets:
            for cir in circles:
                distance_squared = (bullet.x - cir.x) ** 2 + (bullet.y - cir.y) ** 2
                if distance_squared <= (bullet.radius + cir.radius) ** 2:
                    bullets_to_remove.append(bullet)
                    cir_to_remove.append(cir)
                    score += 1
                    speed+= 0.1
                    print(f"Score: {score}")
                    break

        for bullet in bullets_to_remove:
            bullets.remove(bullet)
        for cir in cir_to_remove:
            circles.remove(cir)

        for cir in circles:
            cir.y -= speed +0.1
            if cir.y <= 10:
                circles.remove(cir)
                missed += 1
                if missed == 3:
                    print("Game Over, missed 3 times !!")
                    print(f"Final Score: {score}")
                    gameover = True
                if (shooter_x - cir.x) ** 2 + (sradius - cir.y) ** 2 <= (cir.radius + 10) ** 2:
                    sr,sg,sb = 0,0,0
                    print("Game Over!!")
                    print("Shooter got destroyed !")
                    print(f"Final Score: {score}")
                    gameover = True


        for bullet in bullets:
            bullet.y += 1 + (speed*0.7)
            if bullet.y >= 445:
                surfaceshot+=1
                bullets.remove(bullet)
                if surfaceshot==3:
                    print("Top border shot 3 times.")
                    print("Game Over!!")
                    print(f"Final Score: {score}")
                    gameover=True

    glutPostRedisplay()




def display():
    global gameover,bgenspeed
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(1.0)
    drawShooter()
    if gameover==False:
        if pause == False:
            if random.random() < bgenspeed/1000:
                c = Circle()
                c.checkcollision(circles)
                if c.collision == False:
                    circles.append(c)
        for cir in circles:
            cir.draw()
        for bullet in bullets:
            bullet.draw()
        restart()
        pauseonoff()
        exitbutton()
        buttonborder()
    glutSwapBuffers()





shooter_x = random.randint(220, 280)
sradius = 10
bgenspeed = 5
sr,sg,sb = 1,1,1
bullets = []
circles=[]
score=0
missed=0
surfaceshot=0
gameover=False
pause=False


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Bubble Shooter")
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)
glutMouseFunc(mouseListener)
glutDisplayFunc(display)
glutIdleFunc(animate)
init()
glutMainLoop()
