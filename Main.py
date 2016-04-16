#Tyme Suda and Matthew Wilson

from visual import *

def collision_detection(object_table):
    for i in range(0,len(object_table)):
        for n in range(0,len(object_table)):
            if n!=i:
                if abs(object_table[i].pos-object_table[n].pos)<(object_table[i].radius*2):
                    linear_momentum(object_table[i],object_table[n])
