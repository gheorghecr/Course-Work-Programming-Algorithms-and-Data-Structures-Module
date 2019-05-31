"""6. Adapt the previous graph structure to support weighted connections and
implement Dijkstra’s algorithm."""

class Graph:
    def __init__(self):
        self.graph = {}

    def addEdges(self, source, destination, weight):
        """Adding edges to the graph"""
        if (source in self.graph):
            self.graph[source].update({destination:weight})
        elif (source not in self.graph.keys()):
            self.graph.update({source:{destination:weight}})  

    def dijkstra(self, source, destination):
        """Title: More Graphs
            Author: Hintea, D.
            Date: 2018
            Availability: http://moodle.coventry.ac.uk

            Title: Implementation of dijkstra in python
            Author:Ian Sullivan
            Date: 2017
            Availability: https://www.youtube.com/watch?v=IG1QioWSXRI
        """
        previusNode = {}
        path = []
        minDistance = {}
        bigNumber = 99999999
        noVisitedNodes = self.graph

        #set all nodes to infinity
        for node in self.graph:
            minDistance[node] =bigNumber
        minDistance[source] = 0  #source is no distance from it self

        while noVisitedNodes:
            min = None
            #find the node with the minimum distance from a set to use it
            for node in noVisitedNodes:
                try:
                    if (min == None):
                        min = node
                    elif (minDistance[node] < minDistance[min]):
                        min = node
                except KeyError:
                    print("Node " + str(node) + " not in connected ")

            #this will update the weight for the next childrens of the min found
            #in the for loop before  if necessary and remove the min from the
            #noVisitedNodes
            for child, weight in self.graph[min].items():
                if weight + minDistance[min] < minDistance[child]:
                    minDistance[child] = weight + minDistance[min]
                    previusNode[child] = min  # keeping track on the previus node
            noVisitedNodes.pop(min)

        currentNode  = destination # will start from the back
        while (currentNode is not source):
            path.insert(0,currentNode) # will insert the path at the index 0
            currentNode = previusNode[currentNode]
        path.insert(0,source) #adding to the path the first element (source)

        #if the destination is diferent from big number is beucause it was
        #reached and de weight was updated
        if (minDistance[destination] != bigNumber):
            print("Shortest path: " +  str(path))
            print("Weight: " + str(minDistance[destination]))
        return path, minDistance[destination]


if __name__ == "__main__":

        # the graph, just for my understanding
        #{ 1: {2: 3, 3: 2},
        # 2: {1: 3, 3: 6},
        # 3: {1: 2, 2: 6, 4: 5, 5: 7},
        # 4: {3: 5, 5: 3},
        # 5: {3: 7, 4: 3}}

    graph = Graph()
    graph.addEdges(1,2,3)
    graph.addEdges(1,3,2)
    graph.addEdges(2,1,3)
    graph.addEdges(2,3,6)
    graph.addEdges(3,1,2)
    graph.addEdges(3,2,6)
    graph.addEdges(3,4,5)
    graph.addEdges(3,5,7)
    graph.addEdges(4,3,5)
    graph.addEdges(4,5,3)
    graph.addEdges(5,3,7)
    graph.addEdges(5,4,3)

    path, minDistance = graph.dijkstra(2,5)
