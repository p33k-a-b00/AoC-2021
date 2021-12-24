def parseInput():
    output = []
    chunks = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
    }
    closeChunks = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
    }
    chunkKeys = {
    "(": 0,
    "[": 1,
    "{": 2,
    "<": 3
    }
    chunkCloseKeys = {
    ")": 0,
    "]": 1,
    "}": 2,
    ">": 3
    }
    points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
    }

    incomp = []
    cor = []
    score = 0
    score2 = 0
    with open('input.txt') as f:   
        for line in f:
            modLine = list(line.strip())
            chunkTracker = [0,0,0,0]
            lastOpened = []
            complete = []
            corrupt = False
            incomplete = False
            chunkFound = False
            print(modLine)
            i = 0
            score2 = 0
            while chunkFound == False and incomplete == False and corrupt == False:
                if modLine[i] in chunkKeys:
                    lastOpened.append(modLine[i])
                    chunkTracker[chunkKeys[modLine[i]]] += 1
                elif chunkKeys[lastOpened[-1]] != chunkCloseKeys[modLine[i]]:
                    corrupt = True
                    score += points[modLine[i]]
                else:    
                    chunkTracker[chunkCloseKeys[modLine[i]]] -= 1
                    lastOpened.pop() 
                if corrupt == False:    
                    if sum(chunkTracker) > 0 and i == len(modLine)-1:
                        incomplete = True
                        for x in lastOpened[::-1]:
                            complete.append(chunks[x])
                        for x in complete:
                            temp = score2
                            score2 = temp * 5 + closeChunks[x]
                        output.append(score2)
                    elif sum(chunkTracker) > 0 and chunkTracker[chunkKeys[modLine[0]]] == 0:
                        corrupt = True
                        score += points[modLine[i]]
                    elif chunkTracker[chunkKeys[modLine[0]]] == 0:
                        out = ""
                        modLine = modLine[i+1:]
                        i = -1
                    for x in chunkTracker:
                        if x < 0:
                            corrupt = True
                            score += points[modLine[i]]

                i += 1
            print(chunkFound,incomplete,corrupt)
            if incomplete:
                incomp.append(line.strip())
            if corrupt:
                cor.append(line.strip())
    output.sort()
    return output[int(len(output)/2)]

print(parseInput())