import os

def new_intersection(line1, line2):
    dist = 0
    if line1[1][2] != line2[1][2]:
        if line1[1][2] == 2:
            if line2[0][1] in range(min(line1[0][1], line1[1][1]), max(line1[0][1], line1[1][1])):
                if line1[0][0] in range(min(line2[0][0], line2[1][0]), max(line2[0][0], line2[1][0])):
                    dist = line1[0][3] + line2[0][3] + abs(line1[0][0] - line2[0][0]) + abs(line2[0][1] - line1[0][1])
        else:
            if line1[0][1] in range(min(line2[0][1], line2[1][1]), max(line2[0][1], line2[1][1])):
                if line2[0][0] in range(min(line1[0][0], line1[1][0]), max(line1[0][0], line1[1][0])):
                    dist = line1[0][3] + line2[0][3] + abs(line2[0][0] - line1[0][0]) + abs(line1[0][1] - line2[0][1])
    return dist

def getPoints():
    working_directory = os.path.dirname(__file__)
    input_file_path = working_directory + '/day3input.txt'
    with open(input_file_path) as fp:
        line1 = fp.readline().rstrip('\n').split(",")
        line2 = fp.readline().split(",")
        return line2points(line1), line2points(line2)

def line2points(directions):
    # point = x, y, orientation, steps

    points = [(0,0,0,0)]
    start = (0,0,0,0)
    for val in directions:
        step = int(val[1:])
        if val[0] == "U":
            start = (start[0] + step, start[1], 1, start[3] + step)
        elif val[0] == "D":
            start = (start[0] - step, start[1], 1, start[3] + step)
        elif val[0] == "R":
            start = (start[0], start[1] + step, 2, start[3] + step)
        elif val[0] == "L":
            start = (start[0], start[1] - step, 2, start[3] + step)
        points.append(start)
    return points

dist = 0
segment1, segment2 = getPoints()
for i in range(0, len(segment1) - 1):
    for j in range(0, len(segment2) - 1):
        dist = new_intersection((segment1[i], segment1[i+1]), (segment2[j], segment2[j+1]))
        if dist != 0:
            break
    if dist != 0:
            print(dist)
            break
