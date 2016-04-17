#Tyme Suda and Matthew Wilson

from visual import *
import random

dt=0.1
rate=100

#Code defined variables
spheres=[]
walls=[]

def collision_detection_sphere(sphere_table):
    #Detects collisions bettwen diffrent spheres
    for i in range(0,len(sphere_table)):
        for n in range(0,len(sphere_table)):
            if n!=i:
                if abs(sphere_table[i].pos-sphere_table[n].pos)<(sphere_table[i].radius*2):
                    linear_momentum(sphere_table[i],sphere_table[n])

def linear_momentum(object1,object2):
    #Assumes elastic collision and masses are the same
    #Also all collsions are at closest point i.e. Vel vector points straight through both objects. Might ajust later but will take a lot more programing
    a=object1.velocity.x
    b=object2.velocity.x
    c=object1.velocity.y
    d=object2.velocity.y
    object2.velocity.x=a
    object1.velocity.x=b
    object2.velocity.y=c
    object1.velocity.y=d

def collision_detection_wall(wall_table,sphere_table):
    for w in range(0,len(wall_table)):
        for s in range(0,len(sphere_table)):
            if abs(wall_table[w].pos.x-sphere_table[s].pos.x)<(sphere_table[s].radius+wall_table[w].size.x):
                sphere_table[s].velocity.x=-sphere_table[s].velocity.x
            if abs(wall_table[w].pos.y-sphere_table[s].pos.y)<(sphere_table[s].radius+wall_table[w].size.y):
                sphere_table[s].velocity.y=-sphere_table[s].velocity.y

def physics_step(sphere_table,dt):
    #First update velocity, then pos
    #Assumes other physics checks have already been done i.e. collision checks
    for i in range(0,len(sphere_table)):
        sphere_table[i].pos+=sphere_table.velocity*dt

def create_sphere(num_of_spheres,width,length):
    for i in range(0,num_of_spheres):
        a=randomfloat(width)
        b=randomfloat(length)
        spheres.append(sphere(pos=(a,b,0)))


def randomfloat(width):
    #reutrns random flote bettwen width and -width
    if random.randint(0,1)==1:
        return random.random()*width
    else:
        return -random.random()*width

create_sphere(3,2,2)
print spheres
