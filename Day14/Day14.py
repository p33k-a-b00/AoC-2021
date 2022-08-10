import numpy
import re
import collections

#>>> s = 'a word and another word'
#>>> c = collections.Counter(s)

def parseInput():
    output = []
    with open('input.txt') as f:   
        for line in f:
            line = (line.strip().split(' -> '))
            output.append(line)
    template = output.pop(0)
    output.pop(0)
    return [template[0], output]

def pairInsert(template,input):
    #print (template)
    output = template
    length = len(output)
    #print(input) 
    while length > 1:
        #print(template[length-2]+template[length-1])
        for insert in input:
            if insert[0] == template[length-2]+template[length-1]:
                #print (insert[1])
                output = output[:length-1]+insert[1]+output[length-1:]
                #print(output)
        length = length - 1
    return output

    


input = parseInput()
steps = 40
template = input[0]

while steps > 0:
    template = pairInsert(template,input[1])
    steps = steps - 1 
    print(len(template))

c = collections.Counter(template)
print (c.most_common()[0][1]-c.most_common()[-1][1])