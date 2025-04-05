'''
델타 한 방향이 끝까지 간다는 개념
'''
from collections import deque


def bfs():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'R':
                red_pos = (i, j)
            if graph[i][j] == 'B':
                blue_pos = (i, j)
    q = deque()
    q.append(red_pos)
    q.append(blue_pos)
    while q:
        



N, M = map(int,input().split())
graph = [list(input()) for _ in range(N)]




bfs()