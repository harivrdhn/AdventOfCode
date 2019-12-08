import os
import math

def distance(a,b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def is_between(a,c,b):
    return distance(a,c) + distance(c,b) == distance(a,b)

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return 0

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    if is_between(line1[0], (x,y), line1[1]) and is_between(line2[0], (x,y), line2[1]):
        print(x,y)
        return abs(x) + abs(y)
    else:
        return 0

def getPoints():
    working_directory = os.path.dirname(__file__)
    input_file_path = working_directory + '/day3input.txt'
    with open(input_file_path) as fp:
        line1 = fp.readline().rstrip('\n').split(",")
        line2 = fp.readline().split(",")
        return line2points(line1), line2points(line2)

def line2points(directions):
    points = [(0,0)]
    start = (0,0)
    for val in directions:
        if val[0] == "U":
            start = (start[0] + int(val[1:]), start[1])
        elif val[0] == "D":
            start = (start[0] - int(val[1:]), start[1])
        elif val[0] == "R":
            start = (start[0], start[1] + int(val[1:]))
        elif val[0] == "L":
            start = (start[0], start[1] - int(val[1:]))
        points.append(start)
    return points

maxDist = 0
segment1, segment2 = getPoints()
for i in range(0, len(segment1) - 1):
    for j in range(0, len(segment2) - 1):
        dist = line_intersection((segment1[i], segment1[i+1]), (segment2[j], segment2[j+1]))
        if dist != 0 and maxDist == 0:
            maxDist = dist
        elif dist != 0:
            maxDist = min(maxDist, dist)

print(maxDist)