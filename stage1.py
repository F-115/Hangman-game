import random
import time
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from modules.stage1animate import stage1animate
from modules.listeners import keyboardListener
from modules.listeners import mouseListener
from modules.listeners import specialKeyListener
import math
from modules.playPauseX import draw_pause, draw_play, draw_x
from modules.shapes import draw_boat, draw_bucket, draw_chicken2, draw_diamond
from modules.config import config




def display():
    # //clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0);  # //color black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # //load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    # //initialize the matrix
    glLoadIdentity()
    # //now give three info
    # //1. where is the camera (viewer)?
    # //2. where is the camera looking?
    # //3. Which direction is the camera's UP direction?
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    glMatrixMode(GL_MODELVIEW)
    
    draw_x()
    draw_pause()
    draw_play()
    draw_boat()
    draw_bucket()    
    draw_chicken2()
    draw_oval()
    
    if (config.create_new):
        m, n = config.create_new
        glBegin(GL_POINTS)
        glColor3f(0.7, 0.8, 0.6)
        glVertex2f(m, n)
        glEnd()
    if (config.end):
        return
    glutSwapBuffers()


def init():
    # //clear the screen
    glClearColor(0, 0, 0, 0)
    # //load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    # //initialize the matrix
    glLoadIdentity()
    # //give PERSPECTIVE parameters
    gluPerspective(104, 1, 1, 1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    # //near distance
    # //far distance

glutInit()
glutInitWindowSize(config.W_Width, config.W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)  # //Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()

glutDisplayFunc(display) 


 # display callback function
glutIdleFunc(stage1animate)  # what you want to do in the idle time (when no drawing is occuring)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)

glutMainLoop()
    # return something
    # The main loop of OpenGL


