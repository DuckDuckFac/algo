'''
BOJ11559 Puyo Puyo

# 입력 데이터
graph[R][C] : R = 12, C = 6 고정
delta

# 구조
BFS로 특정 알파벳을 돌았을 때, 4개 이상이면 연쇄

'''
def combo():

N = 12
M = 6
graph = [list(input()) for _ in range(N)]

dr = [0,1,0,-1]
dc = [1,0,-1,0]

flag = True # 연쇄가 있으면,

while flag == True:
    for i in range(N):
        for j in range(M):
            if graph[i][j] != '.' and visited[i][j] == 0:



