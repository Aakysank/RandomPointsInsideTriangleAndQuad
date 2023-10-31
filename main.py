import random
import math
def decorator(fnPtr):
    def innerfunc(*args, **kwds):
        shape = 'quadrilateral'
        for key,value in kwds.items():
            if key == 'shape':
                shape = value
                break

        print(f'computing a random point inside a {shape}')

        i = fnPtr(*args, **kwds)

        print(f'Random point inside the {shape} is {next(i)}')
        return i
    return innerfunc

@decorator
def generateRandomPointInsideGivenShape(geomPts, shape='triangle'):
    new_pt = []
    if shape is 'triangle' and len(geomPts) == 3:
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

        for pts in zip(*geomPts):
            new_pt.append(((pts[0]*u) + (pts[1]*v) + (pts[2]*w)))

        yield(new_pt)
        
    elif shape is 'quadrilateral' and len(geomPts) == 4:
        #need to find the barycentric coordinates of the triangle
        #for any point P = uA+vB+wC+tD, where u,v,w,t are barycentric coordinates
        #and A,B,C,D are corners of quadrilateral
        #varying from 0 to 1, and u+v+w+t = 1
        print(geomPts)
        trianglelist = []
        for i in range(4):
            if isPointInsideTriangle(geomPts[i%4], geomPts[(i+1)%4],geomPts[(i+2)%4], geomPts[(i+3)%4]) == True:
                trianglelist.append((geomPts[i%4], geomPts[(i+1)%4], geomPts[(i+2)%4]))
                trianglelist.append((geomPts[(i%4)], geomPts[(i+2)%4], geomPts[(i+3)%4]))
                break

        print(trianglelist)
        if (len(trianglelist)):
            random_tri = random.choice(trianglelist)
            generateRandomPointInsideGivenShape(random_tri, shape='triangle')
        else:
            ldha = random.random()
            mu = random.random()

            u = (1-ldha)*(1-mu)
            v = ldha * (1-mu)
            w = ldha * mu
            t = (1-ldha)*mu

            for pts in zip(*geomPts):
                new_pt.append(((pts[0]*u) + (pts[1]*v) + (pts[2]*w)+ (pts[3]*t)))
                    
            yield(new_pt)

def computeTriangleArea(pt1,pt2,pt3):
    
    vect1 = [pt1[i] - pt2[i] for i in range(3)]
    vect2 = [pt1[i] - pt3[i] for i in range(3)]
    
    cx = (vect1[1] * vect2[2]) - (vect1[2] * vect2[1])
    cy = (vect1[2] * vect2[0]) - (vect1[0] * vect2[2])
    cz = (vect1[0] * vect2[1]) - (vect1[1] * vect2[0])

    return math.sqrt((pow(cx,2))+ (pow(cy,2)) + (pow(cz,2))) * 0.5
    
def isPointInsideTriangle(pt, pt1,pt2,pt3):
    tri_pts = [pt1, pt2, pt3]
    actual_area = computeTriangleArea(tri_pts[0],tri_pts[1],tri_pts[2])
    total_area = 0.0
    for i in range(len(tri_pts)-1):
        total_area += computeTriangleArea(tri_pts[i%len(tri_pts)], tri_pts[i+1%len(tri_pts)],pt)

    if total_area == actual_area:
        print('The point given is inside the triangle')
        return True
    else:
        print('The point given is outside the triangle')
        return False
    

#testing the code
#triangle
triangle_pt1 = [-0.75,0,1]
triangle_pt2 = [0.75,0,0]
triangle_pt3 = [0, 1.5,1.1]

tri_pt_tuple = (triangle_pt1,triangle_pt2,triangle_pt3)
random_pt = generateRandomPointInsideGivenShape(tri_pt_tuple, shape='triangle')


quad_pt1 = [0,0,0]
quad_pt2 = [1,0,0]
quad_pt3 = [1,1,0]
quad_pt4 = [0,1,0]

quad_pt_tuple = (quad_pt1,quad_pt2,quad_pt3,quad_pt4)
random_pt = generateRandomPointInsideGivenShape(quad_pt_tuple, shape='quadrilateral')
