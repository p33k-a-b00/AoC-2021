import numpy as np

def parseInput():
    output = []
    with open('input.txt') as f:   
        for line in f:
            output.append(line.strip())
    return output

def fillOctopuses():
    grid = parseInput()
    length = len(grid[0])
    grids = np.zeros( (len(grid), length))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grids[i][j] = grid[i][j]
    grids[len(grid)-1][length-1] = grid[len(grid)-1][length-1]
    return(grids)

def findTens(grid):
    return np.argwhere(grid == 10)

def energyToZero(grid,tens):
    for ten in tens:
        grid[ten[0]][ten[1]] = 0
    return grid

def addTopLeft(grid,flash,flashes):
    if (flash[0] - 1 > -1) and (flash[1] - 1 > -1) and [flash[0]-1,flash[1]-1] not in flashes:
        grid[flash[0]-1][flash[1]-1] += 1
        if grid[flash[0]-1][flash[1]-1] == 10:
            grid[flash[0]-1][flash[1]-1] = 0
            return [grid,[flash[0]-1,flash[1]-1]]  
    return [grid,0]

def addTop(grid,flash,flashes):
    if (flash[0] - 1 > -1) and [flash[0]-1,flash[1]] not in flashes:
        grid[flash[0]-1][flash[1]] += 1  
        if grid[flash[0]-1][flash[1]] == 10:
            grid[flash[0]-1][flash[1]] = 0
            return [grid,[flash[0]-1,flash[1]]]  
    return [grid,0]

def addTopRight(grid,flash,flashes):
    if (flash[0] - 1 > -1) and (flash[1] + 1 < grid.shape[1]) and [flash[0]-1,flash[1]+1] not in flashes:
        grid[flash[0]-1][flash[1]+1] += 1  
        if grid[flash[0]-1][flash[1]+1] == 10:
            grid[flash[0]-1][flash[1]+1] = 0
            return [grid,[flash[0]-1,flash[1]+1]]  
    return [grid,0]

def addLeft(grid,flash,flashes):
    if (flash[1] - 1 > -1) and [flash[0],flash[1]-1] not in flashes:
        grid[flash[0]][flash[1]-1] += 1  
        if grid[flash[0]][flash[1]-1] == 10:
            grid[flash[0]][flash[1]-1] = 0
            return [grid,[flash[0],flash[1]-1]]  
    return [grid,0]

def addRight(grid,flash,flashes):
    if (flash[1] + 1 < grid.shape[1]) and [flash[0],flash[1]+1] not in flashes:
        grid[flash[0]][flash[1]+1] += 1  
        if grid[flash[0]][flash[1]+1] == 10:
            grid[flash[0]][flash[1]+1] = 0
            return [grid,[flash[0],flash[1]+1]]  
    return [grid,0]

def addBotLeft(grid,flash,flashes):
    if (flash[0] + 1 < grid.shape[0]) and (flash[1] - 1 > -1) and [flash[0]+1,flash[1]-1] not in flashes:
        grid[flash[0]+1][flash[1]-1] += 1
        if grid[flash[0]+1][flash[1]-1] == 10:
            grid[flash[0]+1][flash[1]-1] = 0
            return [grid,[flash[0]+1,flash[1]-1]]  
    return [grid,0]

def addBot(grid,flash,flashes):
    if (flash[0] + 1 < grid.shape[0]) and [flash[0]+1,flash[1]] not in flashes:
        grid[flash[0]+1][flash[1]] += 1  
        if grid[flash[0]+1][flash[1]] == 10:
            grid[flash[0]+1][flash[1]] = 0
            return [grid,[flash[0]+1,flash[1]]]  
    return [grid,0]

def addBotRight(grid,flash,flashes):
    if (flash[0] + 1 < grid.shape[0]) and (flash[1] + 1 < grid.shape[1]) and [flash[0]+1,flash[1]+1] not in flashes:
        grid[flash[0]+1][flash[1]+1] += 1
        if grid[flash[0]+1][flash[1]+1] == 10:
            grid[flash[0]+1][flash[1]+1] = 0
            return [grid,[flash[0]+1,flash[1]+1]]  
    return [grid,0]

def flashAdds(grid,flashes):
    print(flashes)
    flashcount = 0
    for flash in flashes:
        print(flash)
        temp = addTopLeft(grid,flash,flashes)
        grid = temp[0]
        if temp[1] != 0:
            flashes.append(temp[1])
            flashcount += 1
        
        print(flashes)

        temp = addTop(grid,flash,flashes)
        grid = temp[0]
        if temp[1] != 0:
            flashes.append(temp[1])
            flashcount += 1
        
        print(flashes)

        temp = addTopRight(grid,flash,flashes)
        grid = temp[0]
        if temp[1] != 0:
            flashes.append(temp[1])
            flashcount += 1

        print(flashes)

        temp = addLeft(grid,flash,flashes)
        grid = temp[0]
        if temp[1] != 0:
            flashes.append(temp[1])
            flashcount += 1

        print(flashes)

        temp = addRight(grid,flash,flashes)
        grid = temp[0]
        if temp[1] != 0:
            flashes.append(temp[1])
            flashcount += 1

        print(flashes)

        temp = addBotLeft(grid,flash,flashes)
        grid = temp[0]
        if temp[1] != 0:
            flashes.append(temp[1])
            flashcount += 1

        print(flashes)

        temp = addBot(grid,flash,flashes)
        grid = temp[0]
        if temp[1] != 0:
            flashes.append(temp[1])
            flashcount += 1

        print(flashes)

        temp = addBotRight(grid,flash,flashes)
        grid = temp[0]
        if temp[1] != 0:
            flashes.append(temp[1])
            flashcount += 1


    return [grid,flashcount]    

def newStep(grid):
    grid = grid + 1 
    grid = energyToZero(grid,findTens(grid))
    flashes = np.argwhere(grid == 0).tolist()
    flashcount = len(flashes)
    print(grid)
    temp = flashAdds(grid,flashes)
    grid = temp[0]
    flashcount += temp[1]
    print(grid)
    return [grid,flashcount]

grid = fillOctopuses()
steps = 0
flashcount = 0
while len(np.argwhere(grid == 0).tolist()) != grid.shape[0]*grid.shape[1]:
    temp = newStep(grid)
    grid = temp[0]
    flashcount += temp[1]
    steps += 1 
print(steps)