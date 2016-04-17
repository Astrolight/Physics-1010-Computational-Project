#Tyme Suda and Matthew Wilson

import matplotlib.pyplot as plt
from visual import *
import random

Number_of_iterations_per_sec=500
dt=0.01
time_to_stop=100

width=10
height=10
num_of_spheres=5

#Code defined variables
iteration=0
spheres=[]
walls=[]
time=[]
lastcollision=0

#Sphere 1 data
sv1x=[]
sp1x=[]
sv1y=[]
sp1y=[]
sv1z=[]
sp1z=[]

#Sphere 2 data
sv2x=[]
sp2x=[]
sv2y=[]
sp2y=[]
sv2z=[]
sp2z=[]

#Functions
#Physics
def collision_detection_sphere(sphere_table):
    #Detects collisions bettwen diffrent spheres
    lastcollision=0
    for i in range(0,len(sphere_table)):
        for n in range(0,len(sphere_table)):
            if n!=i:
                if abs(sphere_table[i].pos-sphere_table[n].pos)<(sphere_table[i].radius*2):
                    if abs(lastcollision-time[len(time)-1])<dt*10:
                        break
                    else:
                        linear_momentum(sphere_table[i],sphere_table[n])
                        lastcollision=time[len(time)-1]

def collision_detection_wall(wall_table,sphere_table):
    for w in range(0,len(wall_table)):
        for s in range(0,len(sphere_table)):
            if abs(wall_table[w].pos.x-sphere_table[s].pos.x)<(sphere_table[s].radius*0.5+wall_table[w].size.x):
                sphere_table[s].velocity.x=-sphere_table[s].velocity.x
            if abs(wall_table[w].pos.y-sphere_table[s].pos.y)<(sphere_table[s].radius*0.5+wall_table[w].size.y):
                sphere_table[s].velocity.y=-sphere_table[s].velocity.y

def physics_step(object_table):
    #First update velocity, then pos
    #Assumes other physics checks have already been done i.e. collision checks
    for i in range(0,len(object_table)):
        object_table[i].pos+=object_table[i].velocity*dt

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

#Creation of Objects
def create_sphere(ns,w,h):
    maxvel=avg([w,h])
    for i in range(0,ns):
        x=randomfloat(w-1.5)
        y=randomfloat(h-1.5)
        vx=randomfloat(maxvel)
        vy=randomfloat(maxvel)
        spheres.append(sphere(pos=(x,y,0),velocity=vector(vx,vy,0)))

def create_walls(w,h):
    #Creates board with a center of the origin that encompasus the area
    v=1
    walls.append(box(pos=((w),0,0), size=(v,h*2,v)))
    walls.append(box(pos=((-w),0,0), size=(v,h*2,v)))
    walls.append(box(pos=(0,h,0), size=(w*2,v,v)))
    walls.append(box(pos=(0,-h,0), size=(w*2,v,v)))

#Graphing
def getdata(sphere_table):
    #Only collects data for first 2 spheres
    if time!=[]:
        time.append(dt+time[len(time)-1])
    else:
        time.append(0)
    #Sphere 1 data collection
    sp1x.append(sphere_table[0].pos.x)
    sp1y.append(sphere_table[0].pos.y)
    sp1z.append(sphere_table[0].pos.z)
    sv1x.append(sphere_table[0].velocity.x)
    sv1y.append(sphere_table[0].velocity.y)
    sv1z.append(sphere_table[0].velocity.z)
    #Sphere 2 data collection
    sp2x.append(sphere_table[1].pos.x)
    sp2y.append(sphere_table[1].pos.x)
    sp2z.append(sphere_table[1].pos.x)
    sv2x.append(sphere_table[1].velocity.x)
    sv2y.append(sphere_table[1].velocity.x)
    sv2z.append(sphere_table[1].velocity.x)

def graph():
    plt.subplot(2,2,1)
    plt.title("Sphere 1 Pos and Vel in X")
    plt.plot(time,sp1x,color=color.blue,label="S1 Pos(m)")
    plt.plot(time,sv1x,color=color.red,label="S1 Vel(m)")
    plt.legend()
    plt.xlabel('time (s)')
    plt.subplot(2,2,3)
    plt.title("Sphere 1 Pos and Vel in Y")
    plt.plot(time,sp1y,color=color.blue,label="S1 Pos(m)")
    plt.plot(time,sv1y,color=color.red,label="S1 Vel(m)")
    plt.xlabel('time (s)')
    plt.legend()
    plt.subplot(2,2,2)
    plt.title("Sphere 2 Pos and Vel in X")
    plt.plot(time,sp2x,color=color.blue,label="S2 Pos(m)")
    plt.plot(time,sv2x,color=color.red,label="S2 Vel(m)")
    plt.xlabel('time (s)')
    plt.legend()
    plt.subplot(2,2,4)
    plt.title("Sphere 2 Pos and Vel in Y")
    plt.plot(time,sp2y,color=color.blue,label="S2 Pos(m)")
    plt.plot(time,sv2y,color=color.red,label="S2 Vel(m)")
    plt.xlabel('time (s)')
    plt.legend()
    plt.show()

#Math
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

def vectormag(vector):
    l=sqrt(vector[0]**2+vector[1]**2+vector[2]**2)
    return l

#Main Code
#Setup
create_walls(width,height)
create_sphere(num_of_spheres,width,height)
getdata(spheres)
#print("Code will take "+str(time_to_stop/dt/Number_of_iterations_per_sec)+" sec to run.")
while iteration<time_to_stop:
    rate(Number_of_iterations_per_sec)
    iteration+=dt
    collision_detection_sphere(spheres)
    collision_detection_wall(walls,spheres)
    physics_step(spheres)
    getdata(spheres)
graph()
