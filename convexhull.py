import math
"""
   Convex Hull Assignment: COSC262 (2017)
   Student Name: Thomas Kearsley
   Usercode: tke29
"""

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

    return points



def theta(pointA,pointB):
    dx = pointB[0] - pointA[0]
    dy = pointB[1] - pointA[1]
    if abs(dx) < 1.e-6 and abs(dy) < 1.e-6:
        t = 0
    else:
        t = 1.0 * dy/(abs(dx) + abs(dy))
    if dx < 0:
        t = 2 - t
    elif dy < 0:
        t = 4 + t
    #Needed this
    if t == 0:
        return 360.00
    return t*90

def theta_graham(pointA,pointB):
    dx = pointB[0] - pointA[0]
    dy = pointB[1] - pointA[1]
    if abs(dx) < 1.e-6 and abs(dy) < 1.e-6:
        t = 0
    else:
        t = 1.0 * dy/(abs(dx) + abs(dy))
    if dx < 0:
        t = 2 - t
    elif dy < 0:
        t = 4 + t
    return t*90    
    

def lineFn(ptA, ptB, ptC):
    """Given three points, the function finds the value which could be used to determine which sides the third point lies"""
    val1 = (ptB[0]-ptA[0])*(ptC[1]-ptA[1])
    val2 = (ptB[1]-ptA[1])*(ptC[0]-ptA[0])
    ans = val1 - val2
    return ans 

def isCCW(ptA, ptB, ptC):
    """Return True if the third point is on the left side of the line from ptA to ptB and False otherwise"""
    ans = lineFn(ptA, ptB, ptC) > 1.e-6
    return ans

def grahamscan(pts_array):
    """Returns the convex hull vertices computed using the
         Graham-scan algorithm as a list of 'h' tuples
         [(u0,v0), (u1,v1), ...]  
        
    """
    
    pts_array.sort(key=lambda x: x[1]) #sorts points by lowest y-val
    p0 = pts_array[0]
    
    angles = []
    for each in pts_array:
        angle = theta_graham(p0,each)
        angles.append((angle,each))
    angles.sort(key=lambda x: x[0])
    stack = []
    for i in range(0,3):
        stack.append(angles[i][1])
    angles = angles[3:]
    for i in range(0,len(angles)):
        potential_point = angles[i][1]
        while not isCCW(stack[-2],stack[-1],angles[i][1]):
            stack.pop() #keeps popping until is counter-clockwise
        stack.append(angles[i][1]) # appends point when is counterclockwise
    return stack
    
def cross(origin, ptA, ptB):
    return (ptA[0] - origin[0]) * (ptB[1] - origin[1]) - (ptA[1] - origin[1]) * (ptB[0] - origin[0])
    
def giftwrap(listPts):
    """Returns the convex hull vertices computed using the
          giftwrap algorithm as a list of 'h' tuples
          [(u0,v0), (u1,v1), ...]    
    """
    y = 99**99
    #FINDING MIN Y-VAL POINT:
    for i in range(0,len(listPts)):
        if listPts[i][1] < y:
            y = listPts[i][1]
            lowPt = listPts[i]
            k = i
    listPts.append(lowPt) #pts[n] = Pk
    n = len(listPts) -1
    i = 0
    v = 0
    solution = []
    while k != n:
        listPts[i],listPts[k] = listPts[k],listPts[i]
        minAngle = 361
        solution.append(listPts[i])
        for j in range(i+1,n+1):
            angle = theta(listPts[i],listPts[j])
            if(angle < minAngle and angle > v and listPts[j] != listPts[i]):
                minAngle = angle
                k = j
        i = i+1 
        v = minAngle
    return solution


def amethod(listPts):
    '''METHOD CHOSEN IS MONOTONE CHAINING'''
    #Sorts points via x-axis co-ord
    points = sorted(listPts)

    #building upper hull
    lower_hull = []
    for point in points:
        while len(lower_hull) >= 2 and cross(lower_hull[-2], lower_hull[-1], point) <= 0:
            lower_hull.pop()
        lower_hull.append(point)

    # Building upper hull
    upper_hull = []
    for point in reversed(points):
        while len(upper_hull) >= 2 and cross(upper_hull[-2], upper_hull[-1], point) <= 0:
            upper_hull.pop()
        upper_hull.append(point)

    # Concatenation of the lower and upper hulls gives the convex hull.
    # Last point of each list is omitted because it is repeated at the beginning of the other list. 
    hull = upper_hull[:-1] + lower_hull[:-1]
    #Descending x-values
    return hull


def main():
    listPtsA = readDataPts('Set_A.dat', 1000) 
    print(giftwrap(listPtsA))
    '''
    listPtsA = readDataPts('Set_A.dat', 30000) 
    listPtsB = readDataPts('Set_B.dat', 30000)  #File name, numPts given as example only
    #Gift Wrapping
    print("--- GIFTWRAPPING ALGORITHM TESTS ---")
    print()
    print('--- Set_A.dat ---')
    print(giftwrap(listPtsA))
    print()
    print('--- Set_B.dat ---')
    print(giftwrap(listPtsB))
    print()
    #Graham Scan
    print("--- GRAHAM SCAN ALGORITHM TESTS ---")
    print()
    print('--- Set_A.dat ---')
    print(grahamscan(listPtsA))
    print()
    print('--- Set_B.dat ---')
    print(grahamscan(listPtsB))
    print()
    #Monotone Chaining
    print("--- MONOTONE ALGORITHM TEST ---")
    print()
    print('--- Set_A.dat ---')
    print()
    print("Note: Lists are not in the same order so are sorted.")
    b = sorted([(950.0, 50.0), (950.0, 950.0), (50.0, 950.0), (50.0, 50.0)])
    a = sorted(amethod(listPtsA))
    print("Sorted lists are Equal?",a==b)
    print()
    print('--- Set_B.dat ---')
    b = sorted([(500.0, 50.0), (520.0, 50.4), (539.9, 51.8), (559.8, 54.0), (579.6, 57.1), (599.2, 61.1), (618.6, 65.9), (637.8, 71.6), (656.7, 78.1), (675.2, 85.5), (693.5, 93.7), (711.3, 102.7), (728.8, 112.5), (745.8, 123.0), (762.3, 134.3), (778.3, 146.4), (793.7, 159.1), (808.6, 172.4), (822.8, 186.5), (836.4, 201.1), (849.4, 216.4), (861.6, 232.2), (873.2, 248.5), (884.0, 265.3), (894.0, 282.6), (903.3, 300.4), (911.8, 318.5), (919.4, 336.9), (926.2, 355.7), (932.2, 374.8), (937.4, 394.1), (941.6, 413.7), (945.0, 433.4), (947.6, 453.2), (949.2, 473.2), (949.9, 493.1), (949.8, 513.1), (948.8, 533.1), (946.9, 553.0), (944.1, 572.8), (940.4, 592.5), (935.9, 612.0), (930.4, 631.2), (924.2, 650.2), (917.1, 668.9), (909.2, 687.3), (900.5, 705.3), (890.9, 722.9), (880.7, 740.0), (869.6, 756.7), (857.8, 772.8), (845.4, 788.5), (832.2, 803.5), (818.4, 818.0), (804.0, 831.8), (788.9, 845.0), (773.3, 857.5), (757.1, 869.3), (740.5, 880.4), (723.3, 890.7), (705.8, 900.2), (687.8, 908.9), (669.4, 916.9), (650.7, 924.0), (631.8, 930.3), (612.5, 935.7), (593.0, 940.3), (573.4, 944.0), (553.6, 946.8), (533.7, 948.7), (513.7, 949.8), (493.7, 950.0), (473.7, 949.2), (453.8, 947.6), (434.0, 945.1), (414.2, 941.8), (394.7, 937.5), (375.4, 932.4), (356.3, 926.4), (337.5, 919.6), (319.0, 912.0), (300.9, 903.5), (283.1, 894.3), (265.8, 884.3), (249.0, 873.5), (232.6, 862.0), (216.8, 849.7), (201.6, 836.8), (186.9, 823.2), (172.8, 809.0), (159.4, 794.1), (146.7, 778.7), (134.7, 762.7), (123.4, 746.3), (112.8, 729.3), (103.0, 711.8), (94.0, 694.0), (85.7, 675.8), (78.3, 657.2), (71.8, 638.3), (66.1, 619.1), (61.2, 599.7), (57.2, 580.1), (54.1, 560.4), (51.8, 540.5), (50.5, 520.6), (50.0, 500.6), (50.4, 480.6), (51.7, 460.6), (53.9, 440.7), (57.0, 421.0), (60.9, 401.4), (65.8, 382.0), (71.4, 362.8), (77.9, 343.9), (85.3, 325.3), (93.5, 307.0), (102.4, 289.2), (112.2, 271.7), (122.7, 254.7), (134.0, 238.2), (146.0, 222.2), (158.7, 206.7), (172.1, 191.9), (186.1, 177.6), (200.7, 164.0), (215.9, 151.0), (231.7, 138.7), (248.0, 127.2), (264.9, 116.3), (282.1, 106.3), (299.8, 97.0), (317.9, 88.5), (336.4, 80.8), (355.2, 73.9), (374.3, 67.9), (393.6, 62.8), (413.1, 58.5), (432.8, 55.0), (452.7, 52.5), (472.6, 50.8)])
    print("Note: Lists are not in the same order so are sorted.")
    a = sorted(amethod(listPtsB))
    print("Sorted lists are Equal?",a==b)
    '''
if __name__  ==  "__main__":
    main()
  