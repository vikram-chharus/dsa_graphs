graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'F', 'E'],
    'D' : ['A', 'G', 'E'],
    'E' : ['A', 'B', 'C', 'D', 'F', 'G'],
    'F' : ['C', 'E', 'G']
}
visited = {}
q = []
level = {}
parent = {}
def bfs(src, dest):
    q.append(src)
    visited[src] = True
    level[src] = 0
    parent[src] = 0
    while q:
        cur_v = q.pop(0)
        for node in graph[cur_v]:
            if node not in visited:
                q.append(node)
                visited[node] = True
                level[node] = level[cur_v] + 1
                parent[node] = cur_v
            if dest in level: 
                path = []
                x = node
                p = parent[node]
                while x:
                    path.append(x)
                    x = p
                    if x:
                        p = parent[x]
                path.reverse()
                return [level[dest], path]
    
    return level[dest]

print(bfs('A', 'F'))