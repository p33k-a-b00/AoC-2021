#Part 1################################################################################
import numpy

#horizontal , depth
p = [0,0]
position = numpy.array(p)
direction = {'forward':1,'down':1, 'up':-1}
with open('input.txt') as f:   
    for line in f:
        line = line.strip().split(' ')
        if line[0] == 'forward':
            p[0] += direction[line[0]] * int(line[1])
        else:
            p[1] += direction[line[0]] * int(line[1]) 
print(p)
#Part 2################################################################################
#horizontal , depth, aim
p = [0,0,0]
position = numpy.array(p)
direction = {'down':1, 'up':-1}
with open('input.txt') as f:   
    for line in f:
        line = line.strip().split(' ')
        if line[0] == 'forward':
            p[0] += int(line[1])
            p[1] += p[2] * int(line[1])
        else:
            p[2] += direction[line[0]] * int(line[1]) 
print(p)
