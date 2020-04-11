#Simple: Find The Distance Between Two Points

#Given two ordered pairs calculate the distance between them. 
#Round to two decimal places. 
#This should be easy to do in 0(1) timing.

from math import hypot

def distance(x1, y1, x2, y2):
    dic = hypot(x1-x2, y1-y2)
    return round(dic,2)

from math import hypot

def distance(x1, y1, x2, y2):
    return round(hypot(x2-x1, y2-y1), 2)
