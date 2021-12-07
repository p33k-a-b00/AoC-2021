#Part 1################################################################################
""" current = 0 
counter = 0 
with open('input.txt') as f:   
    for line in f:
        prev = current
        current = int(line.strip())
        #print("prev: %s current: %s " %(prev,current))
        if prev != 0:
            if current > prev:
                counter += 1
        #print (counter)        
print(counter) """
#Part 2################################################################################
import numpy
array = []
w = [0,1,2]
window = numpy.array(w)
with open('input.txt') as f:   
    for line in f:
        array.append(int(line.strip()))
counter = 0 
while(window[2]<2000):
    prev = array[window[0]] + array[window[1]] + array[window[2]]
    window = window + 1
    if window[2]<2000:
        current = array[window[0]] + array[window[1]] + array[window[2]]  
        if current > prev:
            counter += 1
print(counter)
