'''

칼로리가 최소일때, 더해야 한다.

'''
T = int(input())
for tc in range(1,T+1):
    N, max_cal = map(int,input().split())
    ingre = []
    for i in range(N):
        ingre.append(list(map(int,input().split())))
    mx = float('-inf')

    def dfs(taste,cal,idx):
        global mx
        if cal <= max_cal:
            mx = max(mx,taste)
        else:
            return

        for i in range(idx, N):
            t,c = ingre[i]
            if cal + c <= max_cal:
                dfs(taste+t, cal+c, idx+1)


    dfs(0,0, 0)
    print(f'#{tc} {mx}')
