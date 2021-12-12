#Part 1################################################################################
import numpy
def parseInput():
    with open('input.txt') as f:   
        for line in f:
            crabs = list(map(int,line.split(',')))
    return crabs

def alignmentCheck(crabs):
    Max = max(crabs)+1
    positions = numpy.arange(Max)
    print (positions)
    output = numpy.zeros((len(crabs), Max)) 
    
    for i in range(len(crabs)):
        output[i] = (numpy.absolute(numpy.full(shape=Max,fill_value=crabs[i],dtype=numpy.float64) - positions))
    
    columnCheck = numpy.sum(output, axis=0)
    print("Fuel: " + str(columnCheck[numpy.argmin(columnCheck)]))
    print("Position: " + str(numpy.argmin(columnCheck)))

crabs = parseInput()
alignmentCheck(crabs)
#Part 2################################################################################
def triangular_number(n):
    return n * (n + 1) // 2

def alignmentCheck2(crabs):
    Max = max(crabs)+1
    positions = numpy.arange(Max)
    print (positions)
    output = numpy.zeros((len(crabs), Max)) 
    
    for i in range(len(crabs)):
        output[i] = (numpy.absolute(numpy.full(shape=Max,fill_value=crabs[i],dtype=numpy.float64) - positions))
    triOutput = triangular_number(output)
    columnCheck = numpy.sum(triOutput, axis=0)
    print("Fuel: " + str(columnCheck[numpy.argmin(columnCheck)]))
    print("Position: " + str(numpy.argmin(columnCheck)))

alignmentCheck2(crabs)