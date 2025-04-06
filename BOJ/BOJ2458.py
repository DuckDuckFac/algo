'''
BOJ2458
키 순서

# 입력 데이터
N, M : 학생 수, 비교 횟수
M번 비교

# 구조
1. dfs를 통해서 나보다 큰 방향, 나보다 작은 방향 만들기
2. 두 개 더한 값 N-1이면 출력

'''
def dfs_up(num):
    global cnt
    if up_graph[num]:
        for up in up_graph[num]:
            if not visited[up]:
                visited[up] = 1
                cnt += 1
                dfs_up(up)
    return

def dfs_down(num):
    global cnt
    if down_graph[num]:
        for down in down_graph[num]:
            if not visited[down]:
                visited[down] = 1
                cnt += 1
                dfs_down(down)

    return






N, M = map(int,input().split())
up_graph = [[] for _ in range(N+1)]
down_graph = [[] for _ in range(N+1)]
result = 0
for _ in range(M):
    x, y = map(int,input().split())
    up_graph[x].append(y)
    down_graph[y].append(x)

# print(up_graph)
# print(down_graph)


for i in range(1,N+1):
    cnt = 0
    visited = [0] * (N + 1)
    dfs_up(i)
    visited = [0] * (N + 1)
    dfs_down(i)
    if cnt == N-1:
        result += 1

print(result)
