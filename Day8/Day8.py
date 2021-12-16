#Part 1################################################################################
import numpy
def parseInput(inputt):
    output = []
    displays = []
    with open('input.txt') as f:   
        for line in f:
            line = line.split()
            line.remove('|')
            output.append(line[-4:])
            line = line[:-4]
            displays.append(line)
    if inputt == 0:
        return displays
    else:
        return output

def findWires(displays):

    displayTracker = numpy.zeros( (len(displays), 10))
    uniqueNumbers = {2:1, 4:4, 3:7, 7:8}

    for i in range(len(displays)):
        for j in range(len(displays[i])):
            if len(displays[i][j]) in [2,4,3,7]:
                displayTracker[i][j] = uniqueNumbers[len(displays[i][j])]
    print(len(numpy.argwhere(displayTracker > 0)))

#findWires(parseInput()[0])

#Part 2################################################################################
import re
def findWires2(displays):

    displayTracker = [[''] * 10] * len(displays)
    uniqueNumbers = {2:1, 4:4, 3:7, 7:8}
    
    for i in range(len(displays)):
        nums = [''] * 10
        for j in range(len(displays[i])):
            if len(displays[i][j]) in [2,4,3,7]:
                nums[uniqueNumbers[len(displays[i][j])]] = displays[i][j]
        displayTracker[i] = nums
        #print(nums[4].translate(str.maketrans('', '', nums[1])))
    #find 9
    for i in range(len(displays)):
        for j in range(len(displays[i])):
            if len(displays[i][j]) == 6:
                if len(displays[i][j].translate(str.maketrans('', '', displayTracker[i][4]))) == 2:
                    displayTracker[i][9] = displays[i][j]
                
    #find 2
    for i in range(len(displays)):
        for j in range(len(displays[i])):
            if len(displays[i][j]) == 5:
                if len(displays[i][j].translate(str.maketrans('', '', displayTracker[i][9]))) == 1:
                    displayTracker[i][2] = displays[i][j]
    #find 3
    for i in range(len(displays)):
        for j in range(len(displays[i])):
            if len(displays[i][j]) == 5:
                if len(displays[i][j].translate(str.maketrans('', '', displayTracker[i][1]))) == 3:
                    displayTracker[i][3] = displays[i][j]
    #find 5
    for i in range(len(displays)):
        for j in range(len(displays[i])):
            if len(displays[i][j]) == 5:
                if len(displays[i][j].translate(str.maketrans('', '', displayTracker[i][2]))) == 2:
                    displayTracker[i][5] = displays[i][j]
    #find 6
    for i in range(len(displays)):
        for j in range(len(displays[i])):
            if len(displays[i][j]) == 6:
                if len(displays[i][j].translate(str.maketrans('', '', displayTracker[i][1]))) == 5:
                    displayTracker[i][6] = displays[i][j]
    #find 0
    for i in range(len(displays)):
        for j in range(len(displays[i])):
            if len(displays[i][j]) == 6:
                if len(displays[i][j].translate(str.maketrans('', '', displayTracker[i][5]))) == 2:
                    displayTracker[i][0] = displays[i][j]
    return(displayTracker)


def calcOutput(decoded, output):
    ret = []
    for x in range(len(decoded)):
        answers = [0,0,0,0]
        for i in range(len(decoded[x])):
            for j in range(len(output[x])):
                if sorted(decoded[x][i]) == sorted(output[x][j]):
                    answers[j] = i 
        ret.append(''.join(map(str,answers)))
    returnSum = 0
    for r in ret:
        returnSum += int(r)    
    return returnSum

    

displays = (parseInput(0))
output = (parseInput(1))
decoded = findWires2(displays)
print(calcOutput(decoded,output))
