dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]
tbl = [0, 2, 1, 4, 3]

T = int(input())

for tc in range(1, T+1):
    n, m, k =map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(k)]

    for _ in range(m):
        # 1칸 이동처리, 경계면에 도달했을 때 //2, 방향 반대
        for i in range(len(data)):
            #[0] : i, [1] : j, [2] : n, [3] : dir
            data[i][0] = data[i][0] + dr[data[i][3]]
            data[i][1] = data[i][1] + dc[data[i][3]]
            if data[i][0] ==0 or data[i][0] == n-1 or data[i][1] == 0 or data[i][1] == n-1:
                data[i][2] //= 2
                data[i][3] = tbl[data[i][3]]

            data.sort(key=lambda x : (x[0],x[1],x[2]), reverse=True)

            #같은 좌표 합치기
            i = 1
            while i <len(data):
                if data[i-1][0:2] == data[i][0:2]:
                    data[i-1][2] += data[i][2]
                    data.pop(i)
                else:
                    i+=1

    ans = 0
    for lst in data:
        ans += lst[2]

    print(f'#{tc} {ans}')