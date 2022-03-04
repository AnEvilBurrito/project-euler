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
edgeList.append((0, 1, t[0][0]))

j = 0 
while j < len(t)-1:
    i = 0 
    while i < len(t[j]):
        edgeList.append((node_number(t, j, i), node_number(t, j+1, i), t[j+1][i]))
        edgeList.append((node_number(t, j, i), node_number(t, j+1, i+1), t[j+1][i+1]))
        i += 1 
    j += 1

print(edgeList)

# constructing adjacency list 

AdjList = []
i = 0
while i <= node_number(t, len(t)-1, len(t[-1])-1):
    # above func retrieves max node  
    AdjList.append([])
    i += 1

for edge in edgeList:
    AdjList[edge[0]].append((edge[1], edge[2]))

for adj in AdjList:
    print(adj)

# --- cost-sensitive search.. 

Visited = []

def DFS(v):
    Visited.append(v)
    print(Visited)
    for u in AdjList[v]: 
        if u[0] not in Visited: 
            DFS(u[0])

'''
Time complexity: ... 
Space complexity: 
Code length:  
readability: 

comment: 

'''
