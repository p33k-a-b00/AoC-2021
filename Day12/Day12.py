#Credit to https://www.geeksforgeeks.org/find-paths-given-source-destination/
# Modified to fit problem 
from typing import DefaultDict

def parseInput():
    output = []
    vertices = []
    with open('input.txt') as e:   
        for line in e:
            for x in line.strip().split(','):
                output.append(x.split('-'))
                for y in x.split('-'):
                    if y not in vertices:
                        vertices.append(y)
    return [output, vertices]

class Graph:

    def __init__(self, vert):
        self.verticies = vert
        self.graph = DefaultDict(list)

    def addEdge(self,x,y):
        self.graph[x].append(y)
        self.graph[x].sort()
        self.graph[y].append(x)
        self.graph[y].sort()

    def printAllPathsRecursive(self, c, e, visited, path, partTwo):
        if c[0].islower() and not partTwo:
            visited[self.verticies.index(c)] = 1
        if c[0].islower() and partTwo:
            visited[self.verticies.index(c)] += 1
            if visited[self.verticies.index(c)] == 2:
                self.twice = True
        
        path.append(c)

        if c == e:
            print(path)
            self.count += 1
        else:
            for i in self.graph[c]:
                if visited[self.verticies.index(i)] == 0 and not partTwo:
                    self.printAllPathsRecursive(i,e,visited,path,partTwo)
                if visited[self.verticies.index(i)] <= 1 and partTwo and i != 'start':
                    if visited[self.verticies.index(i)] == 1 and self.twice == False:
                        self.printAllPathsRecursive(i,e,visited,path,partTwo)
                    if visited[self.verticies.index(i)] == 0:
                        self.printAllPathsRecursive(i,e,visited,path,partTwo)


        path.pop()
        if c[0].islower() and not partTwo:
            visited[self.verticies.index(c)]= 0
        if c[0].islower() and partTwo:
            visited[self.verticies.index(c)] -= 1
            if max(visited) < 2:
                self.twice = False    



    def printAllPaths(self, s, e, p2):

        visited = [0]*(len(self.verticies))
        path = []
        partTwo = p2
        self.twice = False

        self.count = 0
        self.printAllPathsRecursive(s,e,visited,path,partTwo)
        print(self.count)

temp = parseInput()

caveSystem = Graph(temp[1])

for x in temp[0]:
    caveSystem.addEdge(x[0],x[1])

caveSystem.printAllPaths('start','end', True)