import re
import numpy as np

def parseInput():
    dots = []
    folds = []
    dims = [0,0]
    with open('input.txt') as e:   
        for line in e:
            x = line.strip().split(',')
            if len(x) > 1:
                if int(x[0]) > dims[0]:
                    dims[0] = int(x[0])
                if int(x[1]) > dims[1]:
                    dims[1] = int(x[1])
                dots.append(x)
            if len(x) == 1 and x != ['']:
                r1 = re.findall(r"\w=\d{1,9}",x[0])  
                r2 = r1[0].split('=')
                folds.append(r2)
        print (dims)
        print (folds) 
    return [dots, folds, dims]

def buildManual(input):
    grid = np.zeros((input[2][1]+1, input[2][0]+1))
    
    for dot in input[0]:
        grid[int(dot[1])][int(dot[0])] = 1
    print(grid)
    return(grid)

def foldManual(grid,input):
    
    for fold in input[1]:
        if fold[0] == 'y':
            print(int(fold[1]))
            split = np.array_split(grid, [int(fold[1])], 0)
            #print(split)
            merge = np.add(split[0],np.flipud(np.delete(split[1], 0, 0)))
            print(np.count_nonzero(merge))
            grid = merge
        else:
            print(int(fold[1]))
            split = np.array_split(grid, [int(fold[1])], 1)
            #print(split)
            merge = np.add(split[0],np.fliplr(np.delete(split[1], 0, 1)))
            print(np.count_nonzero(merge))
            grid = merge
    return grid

input = parseInput()
grid = buildManual(input)
print(foldManual(grid, input))

