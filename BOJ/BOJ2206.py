'''
벽 부수고 이동하기
#입력 데이터
N, M
graph[N][M]
delta
visited = [0]*2 벽을 부셨나, 안 부셨나

#구조
최단 거리 :
bfs():

    for
    벽이 1인 경우
    벽을 쓴 경우

'''
from collections import deque
N, M = map(int,input().split())
graph = [list(map(int,input())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def bfs():
    q = deque()
    q.append((0,0,1))
    visited[0][0][1] = 1
    step = 0
    while q:
        len_q = len(q)
        for _ in range(len_q):
            cr, cc, wall = q.popleft()
            if cr == N-1 and cc == M-1:
                return step + 1
            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]

                if 0 <= nr < N and 0 <= nc < M:
                    if graph[nr][nc] == 0 and visited[nr][nc][wall] == 0:
                        visited[nr][nc][wall] = 1
                        q.append((nr,nc,wall))

                    if wall == 1 and graph[nr][nc] == 1 and visited[nr][nc][wall-1] == 0:
                        visited[nr][nc][wall-1] = 1
                        q.append((nr,nc,0))
        step += 1
    return -1

print(bfs())