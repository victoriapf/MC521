from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):

        visited.add(v)

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)
        return visited


t = int(input())
for x in range(0, t):
    K, N, M = map(int, input().split())
    g = Graph()
    origin = [0] * K
    destiny = [0] * K
    for i in range(0, K):
        origin[i] = int(input())
    for j in range(0, M):
        u, v = map(int, input().split())
        g.addEdge(u, v)
    inter = g.DFS(origin[0])
    for a in range(1, K):
        inter = set(inter.intersection(g.DFS(origin[a])))
    s = 'Case ' + str(x+1)+': ' + str(len(inter))
    print(s)
