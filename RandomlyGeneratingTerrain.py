import math
import random
import time
from processing import *

width = 400 #width of the window
height = 400 #height of the window
w = 1000 #width of the terrain
h = 800 #height of the terrain
scale = 20
rows = int(h/scale)
cols = int(w/scale)
flyingLocation = 0




### this will store each point ###
terrain = []  
for i in range(cols):
    terrain.append([])
    for j in range(rows):
        terrain[i].append(0)






### create an empty black window ###
def setup():
  size(400, 400, P3D)
  flyingLocation = 0
  
  
  
### draw the animation ###
def draw():
    background(0)
    stroke(0)
    fill(0,160,0)
    
    global flyingLocation
    flyingLocation -= 0.10
    yoff = flyingLocation
    
    ### For each point, raise or lower it by a random amount ###
    for y in range(rows):
        xoff =0
        for x in range(cols):
            terrain[x][y] = map(noise(xoff,yoff),0,1,-100,100)  ##(-75,75) is the range of the random numbers
            xoff+=0.1
        yoff+=0.1
    
    #adjust camera angle
    translate(width/2,height/2-100)
    rotateX(math.pi/3)
    translate(-w/2,-h/2)
  
    for y in range(rows-1):
        beginShape(TRIANGLE_STRIP)
        for x in range(cols):
            vertex(x*scale,y*scale,terrain[x][y])
            vertex(x*scale,(y+1)*scale,terrain[x][y+1])
        endShape()
    time.sleep(0.025)
  
  

      
run()