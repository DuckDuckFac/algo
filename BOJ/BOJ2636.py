'''
BOJ 2636 치즈

#입력 데이터
N, M = R, C
graph[N][M]
delta


#구조
안 쪽 공기임을 어떻게 알까
공기 부분을 2로 설정해서 돌면, 될듯?

While True를 돌면서
1. BFS로 바깥 공기와 내부 공기를 구분
2. 녹는 부분 구분
3. 녹이기


'''
from collections import deque
from copy import deepcopy


def air(graph_air):
    q = deque()
    q.append((0,0))
    graph_air[0][0] = 2
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    while q:
        cr, cc = q.popleft()
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                if graph_air[nr][nc] == 0 or graph_air[nr][nc] == 2:
                    graph_air[nr][nc] = 2
                    visited[nr][nc] = 1
                    q.append((nr,nc))
    return

def melt_cheese(r,c):
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < M and copy_graph[nr][nc] == 2:
            copy_graph[r][c] = 3
            return
    return

dr = [0,1,0,-1]
dc = [1,0,-1,0]

N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
time = 0
cheese = 0
copy_graph = []
while True:
    for i in range(N):
        if graph[i].count(1):
            break
    else:
        print(time)
        print(cheese)
        break

    copy_graph = deepcopy(graph)
    air(copy_graph)

    cheese = 0
    for i in range(N):
        for j in range(M):
            if copy_graph[i][j] == 1:
                melt_cheese(i,j)
                if graph[i][j] == 1 and copy_graph[i][j] == 3:
                    cheese += 1
                    graph[i][j] = 0

    time += 1



