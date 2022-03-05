'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), 
a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not 
possible to try every route to solve this problem, as there are 299 altogether! If you could 
check one trillion (1012) routes every second it would take over twenty billion years to check them all. 
There is an efficient algorithm to solve it. ;o)
'''

with open("p067_triangle.txt", encoding='utf-8') as f:
    triangle = f.read()
    triangle_split = triangle.split("\n")

    t = []
    for line in triangle_split:
        t.append(line.split(" "))

t = t[:-1]
# print(t)

# triangle = '''3
# 7 4
# 2 4 6
# 8 5 9 3'''

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
        edgeList.append(
            (node_number(t, j, i), node_number(t, j+1, i), int(t[j+1][i])))
        edgeList.append(
            (node_number(t, j, i), node_number(t, j+1, i+1), int(t[j+1][i+1])))
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

# we apply BFS again from problem 18

def breadthFirstSearch(adjlist):
    # let's try finding the cumulative cost of every node then...
    Discovered = []
    Visited = []
    maxPathSum = [0] * len(adjlist)

    # append node 0 to discovered, in the format of (node, totalWeight)
    Discovered.append((0, 0))

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
