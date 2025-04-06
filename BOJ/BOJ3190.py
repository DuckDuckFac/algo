'''
BOJ 3190 뱀

# 입력 데이터
N : 보드의 크기 N*N
K : 사과의 갯수
for < K : 사과의 위치(-1,-1 해야 함)
L : 방향 변환 횟수
for < L : 이동 칸, 회전 방향
delta (우 하 좌 상)
dir = 0

# 구조

for < L 만큼 돌면서
    while 이동 칸:
        1. 머리 이동
            a) 벽 or 내 몸에 부딪히면 break
                flag
            b) 아닌 경우
                ㄱ) 사과를 만난 경우 : 머리 이동 후 꼬리를 움직이지 않음
                ㄴ) 사과를 못 만난 경우 : 머리 이후 꼬리 이동.
    이후 방향 전환 후 다음 입력 기다림.
    반시계 : +3 , 시계 : +1
'''
dr = [0,1,0,-1]
dc = [1,0,-1,0] # 우 하 좌 상
N = int(input())
K = int(input())
graph = [[0]*N for _ in range(N)]
graph[0][0] = 2 # 뱀
snake_len = 1 # 뱀 길이
snake = [[0,0]]
dir = 0
time = 0
flag = False # 부딪혔냐의 flag
for _ in range(K):
    x, y = map(int,input().split())
    graph[x-1][y-1] = 1 # 사과 : 1

L = int(input())
for _ in range(L):
    move, turn = input().split()
    M = 0
    hr, hc = snake[0] # snake의 머리
    nr, nc = hr + dr[dir], hc + dc[dir]
    if nr < 0 or nr >= N or nc < 0 or nc >= N or ([nr,nc] in snake):
        flag = True
        break

    if graph[nr][nc] == 1: # 사과를 만난 경우
        snake_len += 1
        snake.append([0,0])
        for i in range(snake_len-1,0,-1):
            snake[i][0], snake[i][1] = snake[i-1][0],snake[i-1][1]
        snake[0][0] += dr[dir]
        snake[0][1] += dc[dir]
        graph[snake[0][0]][snake[0][1]] = 2
    else: # 사과를 안 만난 경우
        graph[snake[snake_len-1][0]][snake[snake_len-1][1]] = 0
        for i in range(snake_len-1,0,-1):
            snake[i][0], snake[i][1] = snake[i - 1][0], snake[i - 1][1]
        snake[0][0] += dr[dir]
        snake[0][1] += dc[dir]
        graph[snake[0][0]][snake[0][1]] = 2
    M += 1
    time += 1
    if flag:
        print(time)
        break
    if turn == 'L':
        dir = (dir+3)%4
    elif turn == 'D':
        dir = (dir+1)%4







