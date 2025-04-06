'''
BOJ 14503 로봇청소가
#입력 데이터
N. M : N*M
r c d 로봇 청소기의 좌표 방향
graph = 방의 배열 N줄

delta
[-1,0,1,0]
[0,1,0,-1]

[
청소처리 visited = [[0]*M] for _ in range(N)]
#구조


while을 돌면서 조건문 수행하며 이동

    visited[r][c]=1
    if graph[r][c] == 0:


    for i in range(4):
        nr, nc 모두 visited 처리 되어있으면
        new_dr=d+2%4
        if 벽이면
        break

        nr, nc 중 visited 처리 되어있지 않은 애가 있으면
        반시계 회전
        전진
'''
from copy import deepcopy

N, M = map(int,input().split())
r, c, d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = deepcopy(graph)
clean = 0
dr = [-1,0,1,0]
dc = [0,1,0,-1]



while True:
    check = 0
    if visited[r][c] == 0:
        visited[r][c] = 1
        clean += 1

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if visited[nr][nc] == 1:
            check += 1

    if check == 4: # 청소 되지 않은 빈칸이 없는 경우
        new_dir = (d+2)%4
        nr = r + dr[new_dir]
        nc = c + dc[new_dir]
        if graph[nr][nc] == 1: #벽인 경우
            break
        r = nr
        c = nc

    else:
        for n in range(4):
            d = (d+3)%4
            nr = r + dr[d]
            nc = c + dc[d]
            if visited[nr][nc] == 0:
                r = nr
                c = nc
                break


print(clean)