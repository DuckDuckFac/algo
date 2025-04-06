import heapq
T = int(input())


dr = [0,1,0,-1]
dc = [1,0,-1,0]

def dijkstra(r,c):
    pq = [(graph[0][0],r,c)]
    INF = float('inf')
    dists = [[INF] * N for _ in range(N)]
    dists[0][0] = graph[0][0]

    while pq:
        dist, cr, cc = heapq.heappop(pq)

        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                new_dist = dist + graph[nr][nc]

                if dists[nr][nc] <= new_dist:
                    continue

                dists[nr][nc] = new_dist
                heapq.heappush(pq, (new_dist, nr, nc))
    return dists




for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int,input())) for _ in range(N)]
    result = dijkstra(0,0)


    print(f'#{tc} {result[N-1][N-1]}')