'''
#입력데이터
T: tc
돌의 수, M의 수
graph[N]

i, j : i번째 돌, j개의 돌에 대해

#구조
ij를 입력받으면서 돌려주면 될듯

'''

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    graph = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())

        for k in range(1,j+1):
            if (i-1-k) < 0 or (i-1+k) >= N:
                break

            if graph[i-1-k] == graph[i-1+k]:
                graph[i-1-k] = 1 - graph[i-1-k]
                graph[i-1+k] = 1 - graph[i-1+k]
    print(f'#{tc}', *graph)
