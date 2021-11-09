from math import *
import matplotlib.pyplot as plt

theta = pi/6
r0 = [1,0]
circ_range = 2*pi/theta
r1 = tan(theta)

for i in range(1,6):
    x = r1*sin((i-1)*theta)
    y = r1*cos((i-1)*theta)
    r0[0] = r0[0]+x
    r0[1] = r0[1]+y
    print(r0)



