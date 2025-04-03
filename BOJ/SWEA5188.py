T = int(input())
for tc in range(1,T+1):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    sum_graph = [[0]*N for _ in range(N)]
    sum_graph[0][0] = graph[0][0]

    for i in range(1,N):
        sum_graph[0][i] = graph[0][i] + sum_graph[0][i-1]
        sum_graph[i][0] = graph[i][0] + sum_graph[i-1][0]

    for i in range(1,N):
        for j in range(1,N):
            sum_graph[i][j] = min(sum_graph[i-1][j], sum_graph[i][j-1]) + graph[i][j]

    print(f'#{tc} {sum_graph[N-1][N-1]}')