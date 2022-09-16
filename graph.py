from email.charset import SHORTEST
from textwrap import shorten


class graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start not in self.graph_dict:
                self.graph_dict[start] = [end]
            else:
                self.graph_dict[start].append(end)
        
    
    def find_all_path(self, start, end, path = []):
        path = path + [start]
        
        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                sub_routes = self.find_all_path(node, end, path)
                for route in sub_routes:
                    paths.append(route)
                
        return paths

    def get_shortest_path(self, start, end, path = []):
        path = path + [start]

        if start not in self.graph_dict:
            return None
        
        if start == end:
            return path

        shortest_path = None
        for city in self.graph_dict:
            if city not in path:
                sp = self.get_shortest_path(city, end, path)
                if sp:
                    if sp is None or len(sp) < len(shortest_path):
                        shortest_path = sp
                
        return shortest_path

    def bfs(self, start):
        visited = {}
        answer = []
        queue = []
        queue.append(start)
        visited[start] = True
        while queue:
            cur_node = queue.pop(0)
            answer.append(cur_node)
            if cur_node in self.graph_dict:
                for connected_node in self.graph_dict[cur_node]:
                    if connected_node not in visited:
                        visited[connected_node] = True
                        queue.append(connected_node)
        return answer


if __name__ == '__main__':
    route = [
        ("Mumbai", "Paris"), 
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
        ("Toronto", "Mumbai")
    ]

    map = graph(route)
    # print(map.find_all_path("Mumbai", "Toronto"))
    print(map.bfs("Mumbai"))