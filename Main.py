#Tyme Suda and Matthew Wilson

from visual import *

def collision_detection_sphere(sphere_table):
    #Detects collisions bettwen diffrent spheres
    for i in range(0,len(sphere_table)):
        for n in range(0,len(sphere_table)):
            if n!=i:
                if abs(sphere_table[i].pos-sphere_table[n].pos)<(sphere_table[i].radius*2):
                    linear_momentum(sphere_table[i],sphere_table[n])

def linear_momentum(object1,object2):
    #Assumes elastic collision
    #All masses are the same
    #Also all collsions are at closest point i.e. Vel vector points streight through both objects
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
            if abs(wall_table[w].pos.x-sphere_table[s].pos.x)<(sphere_table[s].radius+wall_table[w].size.x)
                sphere_table[s].velocity.x=-sphere_table[s].velocity.x
            if abs(wall_table[w].pos.y-sphere_table[s].pos.y)<(sphere_table[s].radius+wall_table[w].size.y)
                sphere_table[s].velocity.y=-sphere_table[s].velocity.y
