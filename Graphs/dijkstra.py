from _collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def Solve(self,A,B,C):
        graph = defaultdict(list)
        for i, j, k in B:
            graph[i].append((j, k))
            graph[j].append((i, k))

        vis = [False for _ in range(A)]
        dis = [float('inf') for _ in range(A)]
        dis[C] = 0
        pq = []
        heappush(pq, (0, C))

        while pq:
            dist, node = heappop(pq)
            vis[node] = True
            for v, w in graph[node]:
                new_dis = dist + w
                if new_dis < dis[v]:
                    dis[v] = new_dis
                    heappush(pq, (new_dis, v))

        for i in range(A):
            if dis[i] == float('inf'):
                dis[i] = -1

        return dis

A=6
B =[[0, 4, 9],
    [3, 4, 6],
    [1, 2, 1],
    [2, 5, 1],
    [2, 4, 5],
    [0, 3, 7],
    [0, 1, 1],
    [4, 5, 7],
    [0, 5, 1]]
C=4
D=Solution()
print(D.Solve(A,B,C))
