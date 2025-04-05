'''
BOJ 2636 치즈

#입력 데이터
N, M = R, C
graph[N][M]
delta


#구조
안 쪽 공기임을 어떻게 알지

'''

dr = [0,1,0,-1]
dc = [1,0,-1,0]

N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
time = 0
cheese = 0

