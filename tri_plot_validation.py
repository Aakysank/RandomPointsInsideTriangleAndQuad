import random
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#generator function that returns any number of points inside a triangle.
def generatePointsInsideTriangle(pt1,pt2,pt3):
    new_pt = []

    #need to find the barycentric coordinates of the triangle
    #for any point P = uA+vB+wC, where u,v,w are barycentric coordinates
    #varying from 0 to 1, and u+v+w = 1

    #fixing v and w as random points (varies from 0 to 1
    v = random.random()
    w = random.random()

    u = 1-v-w


    #if this condition satisfies, that means the point is outside the triangle
    #if the point found is outside the triangle, then scale the v and w by half
    #and recompute u.
    if v >= 0.0 and w >= 0.0 and v+w >= 1.0:
        if v > 0.5:
            v *=0.5
        if w > 0.5:
            w *=0.5

        u = 1-v-w

    for pts in zip(pt1,pt2,pt3):
        new_pt.append(((pts[0]*u) + (pts[1]*v) + (pts[2]*w)))
            
    yield(new_pt)


        
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

pt1 = [-0.75,0,1]
pt2 = [0.75,0,0]
pt3 = [0, 1.5,1.1]

vertices = np.array([pt1, pt2, pt3])

ax.plot_trisurf(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='cyan', linewidth=0.2, edgecolor='black', alpha=0.2)

counter = 0
for i in generatePointsInsideTriangle(pt1,pt2,pt3):
    ax.scatter(*i, c='green', marker='x')
    counter+=1

print("Num points inside triangle", counter)
    
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title('3D Triangle')

plt.show()





