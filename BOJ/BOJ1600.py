'''
#입력데이터
K : 말 이동 횟수
W, H: 가로 길이, 세로 길이
graph
말 델타 / 사방 델타
말 visited 3차원

#구조
visited = [0]*(K+1) W H

bfs():

    q.append(i,j,h) h = hores를 했냐 안 했냐

        델타(사방)

        델타(말)
            델타 말에서 말을 -1해야 함


'''
from collections import deque
K = int(input())
W, H = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(H)]

dr = [0,1,0,-1]
dc = [1,0,-1,0]

hr = [-1,-2,-2,-1,1,2,2,1]
hc = [-2,-1,1,2,2,1,-1,-2]

visited = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]

def bfs(h):
    step = 0
    q = deque()
    q.append((0,0,h))
    visited[0][0][h] = 1
    while q:
        len_q = len(q)
        for _ in range(len_q):
            cr, cc, hs = q.popleft()
            if cr == H-1 and cc == W-1:
                return step

            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]

                if 0 <= nr < H and 0 <= nc < W and graph[nr][nc] == 0 and visited[nr][nc][hs] == 0:
                    q.append((nr,nc,hs))
                    visited[nr][nc][hs] = 1

            for n in range(8):
                nr = cr + hr[n]
                nc = cc + hc[n]

                if hs > 0 and 0 <= nr < H and 0 <= nc < W and graph[nr][nc] == 0 and visited[nr][nc][hs-1] == 0:
                    q.append((nr,nc,hs-1))
                    visited[nr][nc][hs-1] = 1
        step += 1
    return -1


print(bfs(K))
