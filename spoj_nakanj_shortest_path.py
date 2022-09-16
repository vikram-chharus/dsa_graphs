visited = []
level = []
INF = 1e9+10

movements = [
    [-1, 2], [1, 2],
    [-1, -2], [1, -2],
    [2, -1], [2, 1],
    [-2, -1], [-2, 1],
]

def reset():
    for i in range(0,8):
        visited.append([])
        level.append([])
        for j in range(0,8):
            visited[i].append(False)
            level[i].append(INF)

def getX(s):
    return ord(s[0])- ord('a')

def getY(s):
    return ord(s[1])-ord('1')

def isValid(x, y):
    return x>=0 and y>= 0 and x<8 and y < 8

def bfs(src, dest):
    src_x = getX(src)
    src_y = getY(src)
    des_x = getX(dest)
    des_y = getY(dest)
    queue = list()
    queue.append((src_x, src_y))
    visited[src_x][src_y] = True
    level[src_x][src_y] = 0
    while queue:
        cur_v = queue.pop(0)
        x = cur_v[0]
        y = cur_v[1]
        for movement in movements:
            childX = movement[0] + x
            childY = movement[1] + y
            if not isValid(childX, childY):
                continue
            if not visited[childX][childY]:
                queue.append((childX, childY))
                visited[childX][childY] = True
                level[childX][childY] = level[x][y] + 1
            if level[des_x][des_y] != INF:
                break
    return level[des_x][des_y]

reset()

print(bfs('h8','c3'))