import random
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#generator function that returns any number of points inside a triangle.
def generatePointsInsideQuad(pt1,pt2,pt3,pt4):
    new_pt = []

    #need to find the barycentric coordinates of the triangle
    #for any point P = uA+vB+wC+tD, where u,v,w,t are barycentric coordinates
    #and A,B,C,D are corners of quadrilateral
    #varying from 0 to 1, and u+v+w = 1

    #fixing v and w as random points (varies from 0 to 1
    #v = random.random()
    #w = random.random()

    #u = 1-v-w

    ldha = random.random()
    mu = random.random()

    u = (1-ldha)*(1-mu)
    v = ldha * (1-mu)
    w = ldha * mu
    t = (1-ldha)*mu

    for pts in zip(pt1,pt2,pt3, pt4):
        new_pt.append(((pts[0]*u) + (pts[1]*v) + (pts[2]*w)+ (pts[3]*t)))
            
    yield(new_pt)


        
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

pt1 = [0,0,0]
pt2 = [1,0,0]
pt3 = [0,1,0]
pt4 = [1,1,0]

x = []
y = []
z = []

index = 0
for pts in zip(pt1,pt2,pt3,pt4):
    if index == 0:
        x.append(pts[0])
        x.append(pts[1])
        x.append(pts[2])
        x.append(pts[3])
    elif index == 1:
        y.append(pts[0])
        y.append(pts[1])
        y.append(pts[2])
        y.append(pts[3])
    elif index == 2:
        z.append(pts[0])
        z.append(pts[1])
        z.append(pts[2])
        z.append(pts[3])

    index+=1


ax.plot(x + [x[0]], y + [y[0]], z + [z[0]], marker='o', color='b', alpha=0.2)

counter = 0
for i in generatePointsInsideQuad(pt1,pt2,pt3,pt4):
    ax.scatter(*i, c='green', marker='x')
    counter+=1

print("Num points inside quadrilateral", counter)
    
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title('3D Triangle')

plt.show()





