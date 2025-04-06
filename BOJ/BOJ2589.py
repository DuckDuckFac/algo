'''
BOJ2589 보물섬

# 입력 데이터
N, M : R,C
graph[N][M]이 문자열로 주어짐

# 구조
q의 값이 최대인 경우를 찾는 것.
모든 L의 좌표에 대해서 해야할 것 같음.
'''
from collections import deque

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def bfs(r,c):
    global mx
    cnt = 0
    q = deque()
    q.append((r,c))
    visited[r][c] = 1
    step = -1
    while q:
        len_q = len(q)
        for _ in range(len_q):
            cr, cc = q.popleft()
            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] == 'L' and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    q.append((nr,nc))
        step += 1
    mx = max(mx,step)

N, M = map(int,input().split())
graph = [input() for _ in range(N)]
mx = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'L':
            visited = [[0]*M for _ in range(N)]
            bfs(i,j)

print(mx)