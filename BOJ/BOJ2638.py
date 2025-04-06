'''
BOJ2638 치즈 업그레이드

# 입력 데이터
N, M : R, C
graph[N][M]
delta
deepcopy
time : 시간
# 구조
while 문을 돌면서
    1. 외부 공기, 내부 공기 구분
    2. 외부 공기가 2 이상이면 녹는 치즈
'''
from collections import deque
from copy import deepcopy

def air(air_graph):
    q = deque()
    visited = [[0] * M for _ in range(N)]
    q.append((0,0))
    visited[0][0] = 1
    air_graph[0][0] = 2
    while q:
        cr, cc = q.popleft()
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and air_graph[nr][nc] == 0:
                air_graph[nr][nc] = 2
                visited[nr][nc] = 1
                q.append((nr,nc))
    return

def melt_cheese(r,c):
    cnt = 0
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < M and copy_graph[nr][nc] == 2:
            cnt += 1
            if cnt >= 2:
                copy_graph[r][c] = 3
                return

dr = [0,1,0,-1]
dc = [1,0,-1,0]
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
time = 0
while True:
    for i in range(1,N-1):
        if graph[i].count(1):
            break
    else:
        print(time)
        break

    copy_graph = deepcopy(graph)

    # 1. 외부 공기 구분
    air(copy_graph)

    # 2. 치즈 녹이고 graph에 적용
    for i in range(N):
        for j in range(M):
            if copy_graph[i][j] == 1:
                melt_cheese(i,j)
                if copy_graph[i][j] == 3 and graph[i][j] == 1:
                    graph[i][j] = 0

    time += 1


