'''
BOJ17142 연구소 3

# 입력 데이터
N, M : N*N, M개의 바이러스 개수
graph[N][N]
virus_pos = 2의 위치

# 구조
입력
for N
    for N
        2의 위치 append
        그 위치 1로 바꾸기

def 조합
    if M
    deepcopy
    for virus_pos
        2로 바꿔주고
    bfs를 들어간다.

    for
    2의 위치에 대한 조합

def bfs
    bfs를 도는 로직

    끝나고 0체크 있으면 -1 없으면 최솟값 출력

'''
from copy import deepcopy
from collections import deque

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def bfs(arr,virus):
    global min_time
    q = deque()
    visited = [[0] * N for _ in range(N)]
    for x,y in virus:
        q.append((x,y))
        visited[x][y] = 1
    time = -1
    while q:
        cr, cc = q.popleft()
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            # 만약 다음것이 비활성 바이러스 * 이거나 이미 활성화 된 바이러스라면
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                if arr[nr][nc] == 0 or arr[nr][nc] == 3:
                    visited[nr][nc] = visited[cr][cc] + 1
                    arr[nr][nc] = 2
                    q.append((nr,nc))
        time += 1

    # 이 곳의 논리는 모든 조합이 바이러스를 퍼트릴 수 없을 때 -1
    # 그것이 아니라면 min_time을 추출
    # print(time)
    # for i in range(N):
    #     print(arr[i])
    for i in range(N):
        if arr[i].count(0):
            return
    min_time = min(min_time,time)

def comb(cnt,idx):
    if cnt == M:
        lab = deepcopy(graph)
        for x,y in spread:
            lab[x][y] = 2
        bfs(lab,spread)
        return

    for i in range(idx,virus_len):
        spread.append(virus_pos[i])
        comb(cnt+1,i+1)
        spread.pop()


N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
virus_pos = []
spread = []
min_time = float('inf')
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus_pos.append((i,j))
            graph[i][j] = 3
virus_len = len(virus_pos)

comb(0,0)
if min_time == float('inf'):
    print(-1)
else:
    print(min_time)
