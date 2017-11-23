def readDataPts(filename, N):
    """Reads the first N lines of data from the input file
          and returns a list of N tuples
          [(x0,y0), (x1, y1), ...]
    """
    count = 0
    points = []
    listPts = open(filename,"r")
    lines = listPts.readlines()
    for line in lines:
        if count < N:
            point_list = line.split()
            count += 1
            for i in range(0,len(point_list)-1):
                points.append((float(point_list[i]),float(point_list[i+1])))
    points.sort(key=lambda x: x[1])
    return points




inf = float("inf")

def dist(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5

def angle(p, point):        
    d = (point[0]-p[0])
    n = (point[1]-p[1])

    if n == 0:        
        return inf

    return d/n

def cross(a,b,c):      
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

def get_hull(points, n, p, pindex):    
    if not p:
        p = [inf,inf]
        for x in xrange(n):
            point = points[x]
            if [point[1],point[0]] < [p[1],p[0]]:
                p = point
                pindex = x    

    l = len(points)
    if l == 1:        
        return [points[0]]       

    points = points[:pindex] + points[pindex+1:]
    l = len(points)

    for point in points:                
        point.append(angle(p, point))
        point.append(dist(p,point))    

    points.sort(key = lambda point: (-point[2], point[3]))

    hull = [p,points[0]]

    if points[0][2] == points[-1][2]:
        hull[1] = points[-1]
    else:
        x = 1  
        while x < l:
            point = points[x]              
            score = cross(hull[-2], hull[-1], point)
            if score > 0:
                hull.append(point)          
            elif score == 0 and len(hull) == 2:
                hull.pop()
                hull.append(point)
            else:
                hull.pop()        
                x -= 1
            x += 1

    return hull


listPts = readDataPts('Set_A.dat', 50)
print(listPts)
print(get_hull(listPts,(599.4, 400.8),50,0))