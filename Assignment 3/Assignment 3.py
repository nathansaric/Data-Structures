# Nathan Saric - 04/14/2021

# Breadth-First Search Algorithm and Prim's Algorithm

import random # used to randomly generate values and choices

# Vertex class used in Graph class containing an initialization function 
# and another function that fulfill the requirements set out in Problems 1.1 through 1.4
class Vertex:

    # Initialization function for Vertex class
    def __init__(self, vertexValue):
        self.value = vertexValue
        self.adjacencies = {}

    # addAdjacency that adds an adjacent vertex to an existing vertex 
    # along with the weight of the edge that connects the two vertices
    def addAdjacency(self, endVertex, weight):
        self.adjacencies[endVertex] = weight

# Graph class containing an initialization function, a string function, an iterator function, 
# and 8 other functions that fulfill the requirements set out in Problems 1.1 through 1.4
class Graph: 

    # Initialization function for Graph class
    def __init__(self, *args):
        self.vertices = {}
        self.totalVertices = 0

        # Note that this function is an overloaded constructor that can accept several arguments
        # If 1 argument is passed, it is assumed that it is a graph that has been hardcoded
        # Otherwise it is assumed that 3 arguments are passed into the function
        if len(args) > 1:
            numVertices = args[0]
            minWeight = args[1]
            maxWeight = args[2]
            inputGraph = None
        else: 
            inputGraph = args[0]

        # Generates a random graph since the inputGraph flag was set to None
        if inputGraph == None:
            self.createRandomGraph(numVertices, minWeight, maxWeight)
            
            # Checks if the randomly generated graph is connected, otherwise randomly generates a new graph
            connected = self.BFS_Algorithm()[3]
            if connected == False:
                self.createRandomGraph(numVertices, minWeight, maxWeight)
        else: # Generates the input graph since the inputGraph flag was not set to None
            self.createInputGraph(inputGraph)

    # Iterator function that allows the objects of type Graph to be iterable
    def __iter__(self):
        return iter(self.vertices.values())

    # String function that formats an interpretable adjacency list representation for a Graph object
    def __str__(self):
        for vertex in self:
            adjacencyList = []
            for adjacentVertex in vertex.adjacencies:
                adjacencyList.append(str(adjacentVertex.value) + ": " + str(vertex.adjacencies[adjacentVertex]))
            print(str(vertex.value) + " is adjacent to: " + str(adjacencyList))
        return ("-" * 100)

    # createRandomGraph function that randomly generates a graph following the method outlined in Problem 1.1
    def createRandomGraph(self, numVertices, minWeight, maxWeight):
        for i in range(numVertices):
            self.insertVertex(i)
        self.insertEdge(0, random.randint(1, numVertices), random.randint(minWeight,maxWeight))

        for i in range(2, numVertices):
            x = random.randint(1, i-1)
            S = []

            for j in range(x):
                S.append(random.randint(1, i-1))

            for s in S:
                w = random.randint(minWeight, maxWeight)
                self.insertEdge(i, s, w)

    # createInputGraph function that generates a graph representation given an adjacency matrix
    def createInputGraph(self, inputGraph):
        for i in range(len(inputGraph)):
            self.insertVertex(i)

            for j in range(len(inputGraph[i])):
                if inputGraph[i][j] != 0 and i in self.vertices and j in self.vertices:
                    self.insertEdge(i, j, inputGraph[i][j])

    # insertVertex function that inserts and returns a new vertex in the Graph 
    def insertVertex(self, vertexValue):
        if vertexValue not in self.vertices:
            self.totalVertices += 1
    
        newVertex = Vertex(vertexValue)
        self.vertices[vertexValue] = newVertex
        return newVertex

    # insertEdge function that inserts an edge with a given weight between two vertices 
    def insertEdge(self, startVertex, endVertex, weight):
        # Checks to see if the start vertex is in the Graph
        if startVertex not in self.vertices:
            self.insertVertex(startVertex)

        # Checks to see if the end vertex is in the Graph
        if endVertex not in self.vertices:
            self.insertVertex(endVertex)

        # Inserts the edge in both directions to ensure the graph is undirected
        self.vertices[startVertex].addAdjacency(self.vertices[endVertex], weight)
        self.vertices[endVertex].addAdjacency(self.vertices[startVertex], weight)

    # adjacencyMatrixConvert function that converts an adjacency list into its corresponding adjacency matrix
    # This function returns an adjacency matrix which is used to simplify the implementation of Prim's Algorithm
    def adjacencyMatrixConvert(self):
        adjacencyMatrix = []
        for i in range(self.totalVertices):
            adjacencyMatrix.append([0] * self.totalVertices)
    
            for adjacentVertex in self.vertices[i].adjacencies:
                adjacencyMatrix[i][int(adjacentVertex.value)] = int(self.vertices[i].adjacencies[adjacentVertex])

        return adjacencyMatrix

    # BFS_Algorithm function that implements a breadth-first search traversal for the Graph as outlined in Problem 1.2
    # This function returns the total weight of the edges included in the spanning tree the algorithm randomly traverses
    # This function also returns the start vertex, the sequence of edges travelled
    # This function is also used to check if the Graph is connected and returns True or False accordingly 
    def BFS_Algorithm(self):
        totalWeight = 0 
        queue, visited, edges = [], [], []  

        # Randomly selects a start vertex for the spanning tree
        startVertex = random.choice(list(self.vertices.keys()))
        queue.append(startVertex)
        while len(queue) > 0:
            x = queue.pop()
            if x not in visited:
                visited.append(x)

            for y in self.vertices[x].adjacencies: 
                if y.value not in visited:
                    visited.append(y.value)
                    queue.append(y.value)
                    totalWeight += self.vertices[x].adjacencies[y]
                    edges.append(self.vertices[x].adjacencies[y])

        # Checks to see if the graph is connected by comparing the length of the traversed vertices with the total number of vertices
        if len(visited) == self.totalVertices:
            return totalWeight, startVertex, edges, True
        else:
            return totalWeight, startVertex, edges, False

    # prim_Algorithm function that implements Prim's Algorithm for the Graph as outlined in Problem 1.3
    # This function returns the minimum weight of the edges included in the minimum spanning tree the algorithm traverses
    # This function also returns the sequence of edges travelled
    def prim_Algorithm(self):
        # Converts the Graph to an adjacency matrix representation 
        adjacencyMatrix = self.adjacencyMatrixConvert()
        numEdges, minimumWeight = 0, 0
        visited, edges = [], []
        for i in range(self.totalVertices):
            visited.append(False)
        visited[0] = True # Start at the first vertex in the Graph

        while (numEdges < self.totalVertices - 1):
            minimumEdge = maxWeight
            x, y = 0, 0

            for i in range(self.totalVertices):
                if visited[i] == True:
                    for j in range(self.totalVertices):
                        if ((visited[j] == False) and (adjacencyMatrix[i][j] != 0)):
                            if minimumEdge > adjacencyMatrix[i][j]:
                                minimumEdge = adjacencyMatrix[i][j]
                                x, y = i, j
            numEdges += 1
            minimumWeight += minimumEdge
            visited[y] = True
            edges.append(adjacencyMatrix[x][y])

        return minimumWeight, edges

    # compareAlgorithms function that compares the breadth-first search algorithm and Prim's algorithm as outlined in Problem 1.4
    # This function returns the difference in weight values produced by each respective algorithm from Problem 1.2 and 1.3 
    def compareAlgorithms(n, k, minWeight, maxWeight):
        results = []
        for i in range(1, k+1):
            newGraph = Graph(n, minWeight, maxWeight)
            B = newGraph.BFS_Algorithm()[0]
            P = newGraph.prim_Algorithm()[0]
            diff = (B - P)/P
            results.append(diff)

        return results

# Test code
if __name__ == '__main__':

    # Adjacency matrix provided in the assignment for testing purposes
    testGraph = [[ 0, 15,  0,  7, 10,  0],
                  [15,  0,  9, 11,  0,  9],
                  [ 0,  9,  0,  0, 12,  7],
                  [ 7, 11,  0,  0,  8, 14],
                  [10,  0, 12,  8,  0,  8],
                  [ 0,  9,  7, 14,  8,  0]]

    # These variables are all able to change for testing purposes
    numVertices = 5
    minWeight = 10
    maxWeight = 100
    n = [20, 40, 60]
    k = 3

    # List of lists used to simplify the testing code
    testSet = [["Input Graph", testGraph], ["Random Graph", numVertices, minWeight, maxWeight]]

    for i in range(len(testSet)):
        print("-" * 100)
        print("Testing %s Generation" % testSet[i][0])

        if testSet[i][0] == "Input Graph":
            newGraph = Graph(testSet[i][1])
        else: #testSet[i][0] == "Random Graph"
            newGraph = Graph(testSet[i][1], testSet[i][2], testSet[i][3])
        print(newGraph)

        print("-" * 100)
        print("Testing Breadth-First Search Algorithm with %s" % testSet[i][0])
        BFS = newGraph.BFS_Algorithm()
        print("Total weight of the %s using breadth-first search algorithm is: %s" % (testSet[i][0], str(BFS[0])))
        print("The random start vertex chosen was: %s and the sequence of travelled edges was: %s" % (str(BFS[1]), str(BFS[2])))
        print("-" * 100)

        print("-" * 100)
        print("Testing Prim's Algorithm with %s" % testSet[i][0])
        PRIM = newGraph.prim_Algorithm()
        print("Minimum weight of the %s using Prim's algorithm is: %s" % (testSet[i][0], str(PRIM[0])))
        print("The sequence of travelled edges was: %s" % str(PRIM[1]))
        print("-" * 100)

    # Displaying the results for Problem 1.4 as percentages
    print("Comparing Breadth-First Search and Prim's Algorithm")
    for i in range(len(n)):
        results = Graph.compareAlgorithms(n[i], k, minWeight, maxWeight)
        nAverageValue = sum(results) / len(results)
        print("The average value of Diff when n = %d and k = %d is %7.4f" % (n[i], k, (nAverageValue * 100)) + "%")
