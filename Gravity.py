import pygame
import numpy as np
from random import random
from math import *

class Object:

    def __init__(self, x, y, r, m, moveable):
        self.x = x
        self.y=y
        self.r=r
        self.color = (0,0,0)
        self.mass = m
        self.vx = 0
        self.vy = 0
        self.moveable = moveable
    def draw(self):
        drawCircle(self.color,(int(self.x),int(self.y)),self.r)
    def move(self):
        if self.moveable:
            self.x += self.vx
            self.y += self.vy
        self.draw()
    def updateVel(self,objects):
        c = 4
        totalGravityX = 0
        totalGravityY = 0
        for o in objects:
            gravity = (0,0)
            dx = o.x -self.x
            dy = o.y - self.y
            dTotal = sqrt(pow(dx,2)+pow(dy,2))
            if dTotal>self.r+o.r:
                dx/=dTotal
                dy/=dTotal
                force= c*o.mass*self.mass/(pow(dTotal,2))
                totalGravityX+=dx*force
                totalGravityY+=dy*force
            elif dTotal>0:
                dx/=dTotal
                dy/=dTotal
                force= -2*c*o.mass*self.mass/(pow(dTotal,2))
                totalGravityX+=dx*force
                totalGravityY+=dy*force
        self.vx+=totalGravityX/self.mass
        self.vy+=totalGravityY/self.mass

    


def drawCircle(color, pos ,radius):
    pygame.draw.circle(screen,color,pos,radius)
    
objects = []

screen=pygame.display.set_mode([800,800])
screen.fill([150, 150, 150])
pygame.display.set_caption('Gravity')

a = Object(400,400,50, 300,False)
b = Object(300,250,25,100,True)
c = Object(100,250,25,100,True)
objects.append(a)
objects.append(b)
objects.append(c)


running = True
while running:
    screen.fill([150, 150, 150])
    for o in objects:
        o.updateVel(objects)
    for o in objects:
        o.move()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               print('space')
       
        if pygame.mouse.get_pressed()[0]:
            try:
                print('down')
            except AttributeError:
                pass
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            objects.append(Object(pos[0],pos[1],20,50,True))
    pygame.display.flip()
