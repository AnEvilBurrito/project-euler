'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

'''

# this is an interesting problem, we can imagine this as a graph pathfinding problem, whereas depth first search, breadth first search,
# dijkstra and A* can all come in handy 

# let's approach this problem with depth first search first, it must compute and compare maximum while performing 
# graph traversal 

# --- importing graph 

import heapq
from fractions import Fraction


triangle = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

# triangle = '''3
# 7 4
# 2 4 6
# 8 5 9 3'''

triangle_split = triangle.split("\n")

t = []
for line in triangle_split: 
    t.append(line.split(" ")) 

# --- build data structure

# label nodes as 1, 2 3, 4 5 6,.... 
def node_number(triangle, row_index, index): 

    try:
        a = triangle[row_index][index] 
    except IndexError: 
        raise IndexError("Out of range triangle index")

    number = 0 
    i = 0 
    while i < row_index:
        number += len(triangle[i]) 
        i += 1

    return number + index + 1 

# print(node_number(t, len(t)-1, len(t[-1])-1))

# construct edge list 

# edge[0] = source, edge[1] = target, edge[2] = weight 
edgeList = []
edgeList.append((0, 1, int(t[0][0])))

j = 0 
while j < len(t)-1:
    i = 0 
    while i < len(t[j]):
        edgeList.append((node_number(t, j, i), node_number(t, j+1, i), int(t[j+1][i])))
        edgeList.append((node_number(t, j, i), node_number(t, j+1, i+1), int(t[j+1][i+1])))
        i += 1 
    j += 1

# print(edgeList)

# constructing adjacency list 

AdjList = []
i = 0
while i <= node_number(t, len(t)-1, len(t[-1])-1):
    # above func retrieves max node  
    AdjList.append([])
    i += 1

for edge in edgeList:
    # source, target, weight 
    AdjList[edge[0]].append((edge[1], edge[2]))

# for adj in AdjList:
#     print(adj)

# --- cost-sensitive search.. 

def uniformCostSearch(adjlist): 

    Visited = [0]
    Fringe = [(0, 0)] # start at node 0 with cumulative cost 0 (cumulative_cost, node)
    # print(heapq.heappop(Fringe))
    while True: 

        heapq._heapify_max(Fringe)
        print(Fringe)

        if len(Fringe) == 0:
            # no solutions exist if fringe becomes empty 
            return None 

        cumulativeCost, node = heapq._heappop_max(Fringe)
        print(cumulativeCost, node)
        if len(adjlist[node]) == 0: 
            # if there are no further nodes, we have reached the leaf and therefore the 
            # solution. node[0] = the cum cost, which is the max sum 
            return cumulativeCost
        
        Visited.append(node)
        
        for child, weight in adjlist[node]:
            newCumulCost = cumulativeCost + weight   
            nodeFringe = [y for (x,y) in Fringe]
            if child not in Visited and child not in nodeFringe: 
                heapq.heappush(Fringe, (newCumulCost, child)) 
            elif child in nodeFringe: 
                if newCumulCost < Fringe[nodeFringe.index(child)][0]: 
                    del Fringe[nodeFringe.index(child)]
                    heapq.heappush(Fringe, (newCumulCost, child))
            


# print(uniformCostSearch(AdjList)) 

# I think since uniform cost search is a shortest-path finding algorithm, it does not work for this 
# problem, which requires the longest path... 


def breadthFirstSearch(adjlist): 
    # let's try finding the cumulative cost of every node then... 
    Discovered = []
    Visited = []
    maxPathSum = [0] * len(adjlist)

    Discovered.append((0, 0)) # append node 0 to discovered, in the format of (node, totalWeight) 

    while len(Discovered) != 0: 
        # print(Discovered)
        node, nodeWeight = Discovered.pop(0)
        nodeDiscovered = [x[0] for x in Discovered]
        for child, childWeight in adjlist[node]: 
            newWeight = nodeWeight + childWeight 
            if child not in Visited and child not in nodeDiscovered: 
                Discovered.append((child, newWeight)) 
            elif child in nodeDiscovered:
                if newWeight > Discovered[nodeDiscovered.index(child)][1]:
                    del Discovered[nodeDiscovered.index(child)]
                    Discovered.append((child, newWeight)) 
        
        Visited.append(node)
        maxPathSum[node] = nodeWeight
    
    return maxPathSum

allPathSum = breadthFirstSearch(AdjList)

# i = 0 
# while i < len(allPathSum): 
#     print(i, allPathSum[i])
#     i += 1 

print(max(allPathSum))


'''
Time complexity: ... 
Space complexity: 
Code length:  
readability: 

comment: also check out directed acrylic graphs (DAGs) for this problem 

'''
