#Tyme Suda and Matthew Wilson

from visual import *
import random

dt=0.1
rate=100

width=10
height=10
num_of_spheres=2

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

def create_sphere(ns,w,h,):
    maxvel=avg([w,h])
    for i in range(0,ns):
        x=randomfloat(w-1.5)
        y=randomfloat(h-1.5)
        vx
        vy
        spheres.append(sphere(pos=(x,y,0)))

def create_walls(w,h):
    #Creates board with a center of the origin that encompasus the area
    v=1
    walls.append(box(pos=((w),0,0), size=(v,h*2,v)))
    walls.append(box(pos=((-w),0,0), size=(v,h*2,v)))
    walls.append(box(pos=(0,h,0), size=(w*2,v,v)))
    walls.append(box(pos=(0,-h,0), size=(w*2,v,v)))

def randomfloat(width):
    #reutrns random flote bettwen width and -width
    if random.randint(0,1)==1:
        return random.random()*width
    else:
        return -random.random()*width

def avg(table_of_values):
    sum=0
    for i in range(0,len(table_of_values)):
        sum=+table_of_values[i]
    return sum/len(table_of_values)

create_sphere(1,1,1)
