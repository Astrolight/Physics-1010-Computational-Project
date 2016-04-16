#Tyme Suda and Matthew Wilson

from visual import *

def collision_detection(object_table):
    for i in range(0,len(object_table)):
        for n in range(0,len(object_table)):
            if n!=i:
                if abs(object_table[i].pos-object_table[n].pos)<(object_table[i].radius*2):
                    linear_momentum(object_table[i],object_table[n])

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
