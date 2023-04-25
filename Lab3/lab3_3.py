#!/usr/bin/env python3
from cmath import cos, sin
from math import pi
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *

import numpy
import random



N = 20
tab = numpy.zeros((N,N,3))
tabu = numpy.zeros((N))
tabv = numpy.zeros((N))
k = 0.0
add = 1.0/(N-1)

for i in range(N):
    tabu[i] = k
    tabv[i] = k
    k+=add

for u in range (N):
    for v in range (N):
        u1 = tabu[u]
        v1 = tabv[v]
        x = ((-90)*(pow(u1,5)) + 225*(pow(u1,4)) - 270*(pow(u1,3)) + 180*(pow(u1,2)) - 45*u1) * (cos(pi*v1))
        y = (160*(pow(u1,4)) - 320*(pow(u1,3)) + 160*(pow(u1,2))-5)
        z = ((-90)*(pow(u1,5)) + 225*(pow(u1,4)) - 270*(pow(u1,3)) + 180*(pow(u1,2)) - 45*u1) * (sin(pi*v1))
        tab[u][v][0] = x
        tab[u][v][1] = y
        tab[u][v][2] = z
#print(tab)






def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
   


def shutdown():
    pass


def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)

    glEnd()

def spin(angle):
    glRotatef(angle,1.0,0.0,0.0)
    glRotatef(angle,0.0,1.0,0.0)
    glRotatef(angle,0.0,0.0,1.0)

def render(time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    spin(time * 180/3.1415)
    axes()
    random.seed(1000)
    glBegin(GL_TRIANGLES)
    for i in range(N-1):
       for j in range(N-1):
            
            glColor(random.random(),random.random(),random.random())
            glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])
            glColor(random.random(),random.random(),random.random())
            glVertex3f(tab[i+1][j][0], tab[i+1][j][1], tab[i+1][j][2])
            glColor(random.random(),random.random(),random.random())
            glVertex3f(tab[i][j+1][0], tab[i][j+1][1], tab[i][j+1][2])

            glColor(random.random(),random.random(),random.random())
            glVertex3f(tab[i+1][j+1][0], tab[i+1][j+1][1], tab[i+1][j+1][2])
            glColor(random.random(),random.random(),random.random())
            glVertex3f(tab[i+1][j][0], tab[i+1][j][1], tab[i+1][j][2])
            glColor(random.random(),random.random(),random.random())
            glVertex3f(tab[i][j+1][0], tab[i][j+1][1], tab[i][j+1][2])
            
    glEnd()


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
        glOrtho(-7.5, 7.5, -7.5 / aspect_ratio, 7.5 / aspect_ratio, 7.5, -7.5)
    else:
        glOrtho(-7.5 * aspect_ratio, 7.5 * aspect_ratio, -7.5, 7.5, 7.5, -7.5)

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