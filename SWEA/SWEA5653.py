'''
650*650

# 입력 데이터
T : tc
N, M, K : 세포 N,M 배양시간
for N
for M
graph[650][650]
active[650][650]

# 구조

'''
from collections import deque
T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int,input().split())
    q = deque()
    cell = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if cell[i][j] > 0:
                q.append((i,j))
    while q:
    result = 0









    print(f'#{tc} {result}')