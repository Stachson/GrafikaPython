import sys
from tkinter import S

from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass

def fractal(x, y, a, b, s):
    rectangle(x, y, a, b, 1.0, 1.0) #pierwszy kwadrat
    iteration(x, y, a, b, s)



def iteration(x, y, a, b, s):
    if (s == 0):
        return

    newA = a/3; 

    for i in range (3):
        for j in range (3):
            newX = x + j * newA
            newY = y + i * newA
            rectangleContour(newX, newY, a, b, (1/3))
            iteration(newX, newY, newA, newA, s-1)
            
    x_center = x + newA
    y_center = y + newA
    rectangle(x_center, y_center, a, b, 0.0, (1/3))




def rectangleContour(x, y, a, b , d):

    glBegin(GL_LINE_LOOP)
    glColor3f(0.0, 0, 0)
    glVertex2f(x, y)
    glVertex2f(x, y + b * d)
    glVertex2f(x + a * d, y + b * d)
    glVertex2f(x + a * d, y)
    glEnd()


def rectangle(x, y, a, b, c, d):

    if(c == 1.0):
        glColor3f(1.0, 0.0, 0.0)
    else:
        glColor3f(1.0, 1.0, 1.0)

    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(x, y + b * d)
    glVertex2f(x + a * d, y)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(x, y + b * d)
    glVertex2f(x + a * d, y)
    glVertex2f(x + a * d, y + b * d)
    glEnd()

def render(time):
    glClear(GL_COLOR_BUFFER_BIT)
    fractal(0, 0, 60, 60, 4)
    glFlush()


def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-100.0, 100.0, -100.0 / aspect_ratio, 100.0 / aspect_ratio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspect_ratio, 100.0 * aspect_ratio, -100.0, 100.0,
                1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit():
        sys.exit(-1)



    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()