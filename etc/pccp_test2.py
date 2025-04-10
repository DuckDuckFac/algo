from collections import deque,defaultdict
dr = [0,1,0,-1]
dc = [1,0,-1,0]

def bfs(r,c):
    global zone_num
    q = deque()
    q.append((r, c))
    visited[r][c] = zone_num
    oil_scale = 1

    while q:
        cr, cc = q.popleft()
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and land[nr][nc] == 1:
                visited[nr][nc] = zone_num
                q.append((nr, nc))
                oil_scale += 1

    oil_zone[zone_num] = oil_scale
    zone_num += 1



N, M = map(int,input().split())
land = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
oil_zone = defaultdict(int)
oil_zone[0] = 0
zone_num = 1
max_oil = 0

for i in range(N):
    for j in range(M):
        if land[i][j] == 1 and visited[i][j]==0:
            bfs(i,j)

for i in range(N):
    print(visited[i])
print(oil_zone)
for i in range(M):
    check_oil = set()
    sum_oil = 0
    for j in range(N):
        if visited[j][i]:
            check_oil.add(visited[j][i])
    for oil in check_oil:
        sum_oil += oil_zone[oil]
    max_oil = max(max_oil, sum_oil)

print(max_oil)
