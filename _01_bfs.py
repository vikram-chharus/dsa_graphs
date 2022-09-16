#either the weight of the edges is 0 or 1 then we use 0-1 BFS graph technique 
#Observation: at any instant of time we can have maximun 2 levels in the queue while traversing the graph
#when I have a 0 wt edge I'll process it first than the edge having wt 1
#insert lesser wt edge at the beginning and higher at the end of the queue to process it in seq.
#everytime lower level gets performed before higher 

# import collections
# from random import randint

# x = collections.OrderedDict()
# y  = {}
# x['first'] = 1
# x['second'] = 2
# x['third'] = 3

# y['first'] = 1
# y['second'] = 2
# y['third'] = 3
# y['forth'] = 4
# new_x = x.fromkeys(range(10), range(randint(1,10)))
# print(new_x)
# for i in new_x[0]:
#     print(i)


from collections import deque as dq

ve = [(1, 2), (3, 2), (3, 4), (5, 6), (6, 2), (7, 4), (7, 5)]
    

graph = dict()
level = list()
queue = dq()

for v in ve:
    if v[0] == v[1]:
        continue
    if v[0] not in graph:
        graph[v[0]] = [[v[1], 0]]
    else:
        graph[v[0]].append([v[1], 0])

    if v[1] not in graph:
        graph[v[1]] = [[v[0], 1]]
    else:
        graph[v[1]].append([v[0], 1])
    
for i in range(0, len(graph)+1):
    level.append(float('inf'))

def bfs():
    queue.append(1)
    level[1] = 0
    while queue:
        cur_v = queue.popleft()

        for child in graph[cur_v]:
            child_v = child[0]
            child_wt = child[1]

            if level[cur_v] +child_wt < level[child_v]:
                level[child_v] =  level[cur_v] +child_wt
                if child_wt == 1:
                    queue.append(child_v)
                else:
                    queue.appendleft(child_v)
        
    return -1 if level[len(graph)] == float('inf') else level[len(graph)]

print(bfs())








