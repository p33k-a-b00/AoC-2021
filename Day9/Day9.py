import numpy as np

def parseInput():
    output = []
    with open('input.txt') as f:   
        for line in f:
            output.append(line)
    return output

def fillCaves():
    cave = parseInput()
    length = len(cave[0]) - 1
    caves = np.zeros( (len(cave), length))
    for i in range(len(cave)):
        for j in range(len(cave[i]) - 1):
            caves[i][j] = cave[i][j]
    caves[len(cave)-1][length-1] = cave[len(cave)-1][length-1]
    return(caves)

def checkSides(caves,length, width,i,j):
    sides = [False] * 4 

    if i == 0:
        #top
        sides[0] = True
    else:
        sides[0] = False
    if j == 0:
        #left
        sides[1] = True
    else:
        sides[1] = False
    if i == width:
        #bottom
        sides[2] = True
    else:
        sides[2] = False
    if j == length:
        #right
        sides[3] = True
    else:
        sides[3] = False
    
    temp = []
    if sides[0] == False:
        x = i - 1
        while x >= 0:
            if caves[x][j] > caves[x+1][j] and caves[x][j] != 9:
                temp.append((x,j))
                x -= 1
            else: 
                x = -1
    if sides[1] == False:
        y = j - 1
        while y >= 0:
#            print(str(caves[i][y]) + " > " + str(caves[i][y+1]))
            if caves[i][y] > caves[i][y+1] and caves[i][y] != 9:
                temp.append((i,y))
                y -= 1
            else: 
                y = -1
    if sides[2] == False:
        x = i + 1
        while x <= width:
            if caves[x][j] > caves[x-1][j] and caves[x][j] != 9:
                temp.append((x,j))
                x += 1
            else:
                x = width +1
    if sides[3] == False:
        y = j + 1
        while y <= length:
            if caves[i][y] > caves[i][y-1] and caves[i][y] != 9:
                temp.append((i,y))
                y += 1
            else:
                y = length + 1
    return temp
    
def findLowPoints(caves):
    shape = caves.shape
    width = shape[0] - 1
    length = shape[1] - 1
    lows = []
    sides = [False] * 4 
    count = 0
    for i in range(width + 1):
        for j in range(length + 1):
            count = 0
            if i == 0:
                #top
                sides[0] = True
            else:
                sides[0] = False
            if j == 0:
                #left
                sides[1] = True
            else:
                sides[1] = False
            if i == width:
                #bottom
                sides[2] = True
            else:
                sides[2] = False
            if j == length:
                #right
                sides[3] = True
            else:
                sides[3] = False
            if sides[0] == False:
                if caves[i][j] < caves[i-1][j]:
                    count += 1
            if sides[1] == False:
                if caves[i][j] < caves[i][j-1]:
                    count += 1
            if sides[2] == False:
                if caves[i][j] < caves[i+1][j]:
                    count += 1
            if sides[3] == False:
                if caves[i][j] < caves[i][j+1]:
                    count += 1

            temp = []
            if count == sum([not elem for elem in sides]):
                temp.append((i,j))
                if sides[0] == False:
                    x = i - 1
                    while x >= 0:
                        if caves[x][j] < caves[x-1][j] and caves[x][j] != 9:
                            temp.append((x,j))
                            x -= 1
                        else: 
                            x = -1
                if sides[1] == False:
                    y = j - 1
                    while y >= 0:
                        if caves[i][y] < caves[i][y-1] and caves[i][y] != 9:
                            temp.append((i,y))
                            y -= 1
                        else: 
                            y = -1
                if sides[2] == False:
                    x = i + 1
                    while x + 1 <= width:
                        if caves[x][j] < caves[x+1][j] and caves[x][j] != 9:
                            temp.append((x,j))
                            x += 1
                        else:
                            x = width +1
                if sides[3] == False:
                    y = j + 1
                    while y + 1 <= length:
                        if caves[i][y] < caves[i][y+1] and caves[i][j] != 9:
                            temp.append((i,y))
                            y += 1
                        else:
                            y = length + 1
                lastSize = 0
                #print(temp)
                while len(temp) != lastSize:
                    lastSize = len(temp)
                    for point in temp:
                        temp = list(temp) + checkSides(caves,length,width,point[0],point[1])
                        temp = list(set(temp))
                lows.append(len(temp))    

    return (lows)

caves = fillCaves()
lows = sorted(findLowPoints(caves))
print(np.prod((lows[-3:])))