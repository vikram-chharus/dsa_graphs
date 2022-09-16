grid=[
    [3, 2, 1, 0],
    [2, 1, 2, 3],
    [1, 2, 3, 4],
    [1, 2, 2, 1]
]
visited = len(grid)*[len(grid)*[0]]
level = len(grid)*[len(grid)*[float('inf')]]
print(level)
movements = [
    [0,1], [0, -1], [1,0],[-1,0],
    # [1,1], [-1, -1], [1,-1], [-1, 1]
]
def getMAX():
    maxx = float('-inf')
    for i in grid:
        for j in i:
            maxx = max(maxx, j)
    return maxx
def isValid(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid)
def bfs():
    maxx = getMAX()
    q = []
    l = len(grid)
    for i in range(0,len(grid)):
        for j in range(0,len(grid)):
            if maxx == grid[i][j]:
                q.append([i, j])
                level[i][j] = 0
                visited[i][j] = 1
    
    while q:
        cur_v = q.pop(0)
        max_level = float('-inf')
        for movement in movements:
            cx = movement[0] + cur_v[0]
            cy = movement[1] + cur_v[1]
            if not isValid(cx, cy):
                continue
            q.append([cx,cy])
            visited[cx][cy] = 1
            level[cx][cy] = level[cur_v[0]][cur_v[1]] + 1
            max_level = max(max_level, level[cx][cy])

        return max_level

print(bfs())