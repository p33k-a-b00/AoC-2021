#Part 1################################################################################
import numpy
inputt = []
numbers = []
boards = [[]]
size = 0

def buildInput():
    inputt = []
    with open('input.txt') as f:   
        for line in f:
            if line.strip() != '':
                inputt.append(line.strip())
    return inputt

def buildBoards(array):
    array.pop(0)
    size = len(array[0].split())
    numberOfBoards = (len(array) // size )
    board = 0
    i = 0
    j = 0
    
    output = numpy.zeros( (numberOfBoards, size, size) )

    for line in array:
        if i == 5:
            board += 1
            i = 0
        for l in line.split():
            if j != 5:
                output[board][i][j] = l
                j += 1
        i += 1
        j = 0
    return output

def markAndCheck(numbers, boards):
    for number in numbers:
        for board in boards:
            match = numpy.where(board == int(number))
            board[match] += 0.1
            
            columnCheck = numpy.sum(board, axis=0)
            for column in columnCheck:
                if (column%1) == 0.5:
                    return [board,number]
            rowCheck = numpy.sum(board, axis=1)
            for row in rowCheck:
                if (row%1) == 0.5:
                    return [board,number]

def scoreBoard(board):
    sum = 0
    for row in board[0]:
        for val in row:
            if val.is_integer():
                sum += val 
    print(int(board[1])*sum) 
    

inputt = buildInput()
numbers = inputt[0].split(',')

boards = buildBoards(inputt)

winner = markAndCheck(numbers,boards)
print(winner)
scoreBoard(winner)

#Part 2################################################################################

def backwardsMarkAndCheck(numbers, boards):
    for number in numbers:
        for board in boards:
            match = numpy.where(board == int(number))
            board[match] += 0.1

    for number in reversed(numbers):
        for board in boards:
            match = numpy.where(board == float(number)+0.1)
            board[match] -= 0.1

            c = False
            r = False
            columnCheck = numpy.sum(board, axis=0)
            for column in columnCheck:
                if round((column%1),1) == 0.5:
                    c = True
            rowCheck = numpy.sum(board, axis=1)
            for row in rowCheck:
                if round((row%1),1) == 0.5:
                    r = True
            if not c and not r:
                board[match] += 0.1
                return [board,number]

loser = backwardsMarkAndCheck(numbers, boards)
print(loser)
scoreBoard(loser)
