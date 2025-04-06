import math
import heapq

def prim(start_node):
    pq = [(0,start_node)]
    MST = [0] * V
    min_weight = 0

    while pq:
        weight, node = heapq.heappop(pq)

        if MST[node]:
            continue

        MST[node] = 1
        min_weight += weight

        for next_node in range(V):
            if star[next_node] == 0:
                continue

            if MST[next_node]:
                continue

            heapq.heappush(pq, (adj[node][next_node], next_node))

    return min_weight



V = int(input())
star = []
for _ in range(V):
    a,b = list(map(float,input().split()))
    star.append((a,b))

adj = [[0]*V for _ in range(V)]

for i in range(V):
    for j in range(V):
        if i == j:
            continue
        adj[i][j] = math.sqrt((abs(star[i][0] - star[j][0]) ** 2 + abs(star[i][1] - star[j][1]) ** 2))
        adj[j][i] = math.sqrt((abs(star[i][0] - star[j][0]) ** 2 + abs(star[i][1] - star[j][1]) ** 2))


print(round(prim(0),2))