#to find the shortest path from multiple nodes to a node 

graph ={
    1:[3,5],
    5:[1,6],
    3:[1,5,4,6,2],
    4:[3,4],
    2:[3, 6],
    6:[4,5,3,2]
}

def getMaximum():
    maxx = float('-inf')
    for i in graph:
        for val in graph[i]:
            maxx = max(maxx, val)
    return maxx
def bfs(v1, v2, end):

    q = [[v1, v1], [v2, v2]]
    visited = (len(graph)+1)*[float('inf')]
    visited[v1] = 0
    visited[v2] = 0

    while q:
        cur_v = q.pop(0)
        parent_node = cur_v
        for node in graph[cur_v[0]]:
            if node in graph and visited[node] == float('inf'):
                q.append([node, cur_v[1]])
                visited[node] = visited[cur_v[0]] + 1
            if 0 < end <len(visited) and visited[end] != float('inf'):
                return {"Minimum time:":visited[node], "Node:":cur_v[1]}
    return "No possible path"
print(bfs(1, 2, 7))