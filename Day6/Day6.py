#Part 1################################################################################
def parseInput():
    with open('input.txt') as f:   
        for set in f:
            set = list(map(int,set.split(',')))
    return set

def modelGrowth(fishes,days):
    while days > 0:
        for i in range(len(fishes)):
            if fishes[i] == 0:
                fishes[i] = 6
                fishes.append(8)
            else:    
                fishes[i] = fishes[i] - 1
        days -= 1
    return fishes

fishes = parseInput()
print(fishes)
fishes = modelGrowth(fishes,80)
print(len(fishes))
#Part 2################################################################################
import numpy
def parseInputV2():
    with open('input.txt') as f:   
        output = [0,0,0,0,0,0,0]
        for set in f:
            set = list(map(int,set.split(',')))
            set = numpy.array(set)
        for num in numpy.arange(7):
            for fish in set:
                if num == fish:
                    output[num] += 1
    return output

def modelGrowthV2(fishes,days):
    fishes = numpy.array(fishes, dtype=numpy.float64)
    newfishes = numpy.array([0,0], dtype=numpy.float64)
    while days > 0:
        temp = fishes[0]
        fishes = numpy.roll(fishes,-1)
        fishes[6] += newfishes[0]
        newfishes[0] = newfishes[1]
        newfishes[1] = temp

        days -= 1
    return numpy.sum(fishes) + numpy.sum(newfishes)

fishes = parseInputV2()
print(fishes)
fishes = modelGrowthV2(fishes,256)
print(fishes)