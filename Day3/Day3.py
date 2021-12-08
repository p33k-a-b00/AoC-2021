#Part 1################################################################################
gamma = ""
epsilon = ""
powerConsumption = 0
tracker = [0,0,0,0,0,0,0,0,0,0,0,0]
totalLines = 0
halfOfLines = 0
inputArray = []

with open('input.txt') as f:   
    for line in f:
        index = 0
        line = line.strip()
        inputArray.append(line)
        for c in line:
            if c == '1':
                tracker[index] += 1
                index += 1
            else:
                index += 1
        totalLines += 1
halfOfLines = totalLines/2
for x in tracker:
    if x > halfOfLines:
        gamma += "1"
    else:
        gamma += "0"

epsilon = int(gamma,2) ^ int('111111111111',2)
powerConsumption = int(gamma,2) * epsilon
print(powerConsumption) 

#Part 2################################################################################

def findGamma(array,rating):
    size = len(array)
    length = len(array[0])
    tracker = [0] * length
    gamma = ""
    ratingDic = {'o2':'1', 'co2':'0'}

    for element in array:
        index = 0
        for bit in element:
            if bit == '1':
                tracker[index] += 1
                index += 1
            else:
                index += 1
    for position in tracker:
        if position > size/2:
            gamma += "1"
        elif position == size/2:
            gamma += "1"
        else:
            gamma += "0"
    return gamma

gamma = findGamma(inputArray,'o2')  
inputArray2 = inputArray.copy()
index = 0
tracker = [0] * len(inputArray[0])

while len(inputArray) > 1:
    for element in list(inputArray):
        if element[index] != gamma[index]:
            inputArray.remove(element)
    
    gamma = findGamma(inputArray,'o2')
    index += 1

gamma = findGamma(inputArray2,'co2')
index = 0
tracker = [0] * len(inputArray2[0])

while len(inputArray2) > 1:
    for element in list(inputArray2):
        if element[index] == gamma[index]:
            inputArray2.remove(element)

    gamma = findGamma(inputArray2,'co2')
    index += 1

print(int(inputArray[0],2)*int(inputArray2[0],2))

