# Naive O(n^2) where n is the number of edges implementation of
# Prim's Algorithm for finding the minimum spanning tree
# We expect an array of Edges, where each position is one edge 
# numbered 0 through n-1, and the list contains all outgoing edges 
# together with their weights
#
# We assume the graph is connected
#
# We just use the first node (0) as starting point

class PrimAlgorithmNaive():
    def findMinimumSpanningTree(self, adjaciencyMatrix):
        startNode = 0
        seenNodes = [startNode]
        edgesMinimumSpanTree = {}
        
        while len(seenNodes) < len(adjaciencyMatrix):
            smallestEdge = None
            # for each edge in the matrix (graph) we must consider
            # edges that start in seen nodes and end outside the seen nodes
            # and preserve the one with the smallest cost
            # this is the greedy part of the algorithm
            for node in adjaciencyMatrix:
                for edge in node:
                    if edge.source in seenNodes and edge.destination not in seenNodes:
                        if smallestEdge is None or edge.weight < smallestEdge.weight:
                            smallestEdge = edge
 
            # no more edges to consider apparently, so let's get out of here
            if smallestEdge is None:
                return edgesMinimumSpanTree
            
            # if we have an edge, add it and set its destination
            # in seen nodes
            if smallestEdge.source not in edgesMinimumSpanTree:
                edgesMinimumSpanTree[smallestEdge.source] = []
            edgesMinimumSpanTree[smallestEdge.source].append(smallestEdge)
            seenNodes.append(smallestEdge.destination)
            
        return edgesMinimumSpanTree