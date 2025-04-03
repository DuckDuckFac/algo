import math
import heapq
T = int(input())

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
            if island_graph[node][next_node] == 0:
                continue

            if MST[next_node]:
                continue

            heapq.heappush(pq, (island_graph[next_node][node], next_node))

    return min_weight

for tc in range(1,T+1):
    V = int(input())
    island_x = list(map(int,input().split()))
    island_y = list(map(int,input().split()))
    island_graph = [[0]*V for _ in range(V)]
    K = float(input())
    for i in range(V):
        for j in range(V):
            if i == j:
                continue
            island_graph[i][j] = (abs(island_x[i]-island_x[j])**2) + abs((island_y[i]-island_y[j])**2)
            island_graph[j][i] = (abs(island_x[i]-island_x[j])**2) + abs((island_y[i]-island_y[j])**2)

    result = prim(0)
    print(f'#{tc} {round(K*result)}')
