import numpy as np
import math
def distance(v1,v2):
    #wektory puste to dystans jest nieskonczony
    if len(v1) == 0 or len(v2) == 0:
        return 'wektory puste'
    sum = 0
    for i in range(len(v1)):
        sum += ((v2[i]-v1[i])**2)
    return math.sqrt(sum)

v1 = [0,1,0]
v2 = [0,2,0]
print(distance(v1,v2))