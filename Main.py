#Tyme Suda and Matthew Wilson

import matplotlib.pyplot as plt
from visual import *
import random

Number_of_iterations_per_sec=500
dt=0.01
time_to_stop=20

width=10
height=10
num_of_spheres=2

#Code defined variables
tries_per_sphere=1000
iteration=0
spheres=[]
walls=[]
time=[]

#Sphere data
svx=[]
spx=[]
svy=[]
spy=[]

#Functions
#Physics
def collision_detection_sphere(sphere_table):
    #Detects collisions bettwen diffrent spheres
    lastcollision=0
    for i in range(0,(len(sphere_table)-1)):
        for n in range(i+1,len(sphere_table)):
            if abs(sphere_table[i].pos-sphere_table[n].pos)<(sphere_table[i].radius*2):
                linear_momentum(sphere_table[i],sphere_table[n])

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
        state,x,y=randompos(spheres,w,h,tries_per_sphere)
        if state==False:
            break
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
def datasetup(sphere_table):
    time.append(0)
    for i in range(0,len(sphere_table)):
        spx.append([sphere_table[i].pos.x])
        spy.append([sphere_table[i].pos.y])
        svx.append([sphere_table[i].velocity.x])
        svy.append([sphere_table[i].velocity.y])


def getdata(sphere_table):
    time.append(dt+time[len(time)-1])
    k=len(time)
    for i in range(0,len(sphere_table)):
        spx[i].append(sphere_table[i].pos.x)
        spy[i].append(sphere_table[i].pos.y)
        svx[i].append(sphere_table[i].velocity.x)
        svy[i].append(sphere_table[i].velocity.y)

def graph(sphere_table):
    plots=len(sphere_table)
    i=1
    for i in range(0,len(sphere_table)):
        plt.subplot(2,plots,(i+1))
        plt.title("Sphere "+str(i+1)+" Pos and Vel in X")
        plt.plot(time,spx[i],color=color.blue,label=("S"+str(i+1)+" Pos(m)"))
        plt.plot(time,svx[i],color=color.red,label=("S"+str(i+1)+" Vel(m)"))
        plt.subplot(2,plots,(plots+i+1))
        plt.title("Sphere "+str(i+1)+" Pos and Vel in Y")
        plt.plot(time,spy[i],color=color.blue,label=("S"+str(i+1)+" Pos(m)"))
        plt.plot(time,svy[i],color=color.red,label=("S"+str(i+1)+" Vel(m)"))
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

def randompos(sphere_table,w,h,number_of_tries):
    #Makes sure 2 spheres do not spawn in one another
    tries=1
    correct=0
    while tries<number_of_tries:
        x=randomfloat(w-1.5)
        y=randomfloat(h-1.5)
        if len(sphere_table)==0:
            return True,x,y
        else:
            for i in range(0,len(sphere_table)):
                if abs(vector(x,y)-sphere_table[i].pos)>2:
                    correct+=1
                else:
                    tries+=1
            if correct>=(len(sphere_table)):
                return True,x,y
            else:
                correct=0
    return False,0,0

#Main Code
#Setup
create_walls(width,height)
create_sphere(num_of_spheres,width,height)
datasetup(spheres)
#print("Code will take "+str(time_to_stop/dt/Number_of_iterations_per_sec)+" sec to run.")
while iteration<time_to_stop:
    rate(Number_of_iterations_per_sec)
    iteration+=dt
    collision_detection_sphere(spheres)
    collision_detection_wall(walls,spheres)
    physics_step(spheres)
    getdata(spheres)
graph(spheres)
