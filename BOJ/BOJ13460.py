'''
BOJ 13460
한 방향이 끝까지 간다는 개념
R,B의 위치에 따라서 공 움직임을 다르게 해야 함.


'''
from collections import deque


N, M = map(int,input().split())
graph = [list(input()) for _ in range(N)]
