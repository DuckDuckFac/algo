'''
BOJ14502 연구소
#입력 데이터
N,M
graph[N][M]

delta

# 구조
dfs로 벽을 세우고


bfs로 바이러스 퍼트리기

'''
import itertools
from collections import deque
from copy import deepcopy
dr = [0,1,0,-1]
dc = [1,0,-1,0]

N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
safe_zone = []
virus_pos = []
mx = float('-inf')

def bfs(lab):
    sum = 0
    q = deque()
    for x,y in virus_pos:
        q.append((x,y))

    while q:
        cr,cc = q.popleft()
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if 0 <= nr < N and 0 <= nc < M and lab[nr][nc] ==0:
                lab[nr][nc] = 2
                q.append((nr,nc))

    for n in range(N):
        sum += lab[n].count(0)

    return sum




for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            safe_zone.append((i,j))
        if graph[i][j] == 2:
            virus_pos.append((i,j))

for wall_build in itertools.combinations(safe_zone,3):
    copy_graph = deepcopy(graph)
    for x,y in wall_build:
        copy_graph[x][y] = 1

    mx = max(bfs(copy_graph),mx)

print(mx)

