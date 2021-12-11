#Part 1################################################################################
import numpy
def cleanInput():
    output = []
    with open('input.txt') as f:   
        for line in f:
            line = (line.strip().split('->'))
            start = line[0].split(',')
            end = line[1].split(',')
            output.append([start, end])
    return output
            
                

def buildMap(inputt):
    size = 1000
    output = numpy.zeros( (size, size))

    for vent in inputt:
        xReversed = False
        yReversed = False
        if int(vent[0][0]) < int(vent[1][0]):
            x = list(numpy.arange(int(vent[0][0]),int(vent[1][0])+1))
        else: 
            xReversed = True 
            x = list(numpy.arange(int(vent[1][0]),int(vent[0][0])+1))
        if x == []:
            x.append(int(vent[0][0]))
        
        if int(vent[0][1]) < int(vent[1][1]):
            y = list(numpy.arange(int(vent[0][1]),int(vent[1][1])+1))
        else:
            yReversed = True
            y = list(numpy.arange(int(vent[1][1]),int(vent[0][1])+1))
        if y == []:
            y.append(int(vent[0][1]))
        
        if len(x)>1 and not len(y)>1:
            for point in x:
                #print(str(x) + "," + str(point))
                output[point][y[0]] += 1
        if len(y)>1 and not len(x)>1:
            for point in y:
                #print(str(x) + "," + str(point))
                output[x[0]][point] += 1
#Part 2################################################################################
        if len(y)>1 and len(x)>1:
            if xReversed: 
                x = x[::-1]
            if yReversed:
                y = y[::-1]
            for point in range(len(x)):
                    output[x[point]][y[point]] += 1
                
              
    return(output)

inputt = cleanInput()
field = buildMap(inputt)

match = numpy.argwhere(field > 1)
print(numpy.rot90(numpy.transpose(numpy.rot90(field))))
print(len(match))

