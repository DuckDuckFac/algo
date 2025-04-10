'''
SWEA2382 미생물

# 입력
T : tc
N, M, K : 셀의 개수, 격리 시간, 군집 개수
k = []
time
delta 상하좌우 : 1234
for > K 군집 데이터
    r,c,미생물 수, dir

dir_reverse : 반대 방향

# 구조

while time <= M:
    1. 이동
    for r,c,num,dir k
        dir에 맞춰 이동

    2. 방향 체크
    for i : 0 > N-1
        for j : i+1 > N
            a) k[i][0] == k[j][0] and k[i][1] == k [j][1] # 같은 좌표
                if 미생물 크기 비교
                    큰 쪽으로 합치기. 작은 좌표 다 0처리
                else:
                    큰 쪽으로 합치기. 작은 좌표 다 0처리

    3. 바깥 부분을 밟은 경우
    for i
        if 바깥
            a) 미생물//2
            b) 방향 반대

    time += 1

k에서 미생물 전부 합


1. 좌표 + 미생물로 lambda
2. 합하고 pop

'''
dr = [0,-1,1,0,0]
dc = [0,0,0,-1,1]
T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int,input().split())
    time = 0
    k = [list(map(int,input().split())) for _ in range(K)]
    dir_reverse = {1 : 2, 2 : 1, 3 : 4 , 4 : 3}
    result = 0

    while time < M:
        for i in range(K):
            k[i][0] += dr[k[i][3]]
            k[i][1] += dc[k[i][3]]


        k.sort(key=lambda x:(x[0],x[1],-x[2]))
        for i in range(K-1):
            for j in range(i+1,K):
                if k[i][3] != 0 and (k[i][0] == k[j][0]) and (k[i][1] == k[j][1]):
                    if k[i][2] > k[j][2]:
                        k[i][2] += k[j][2]

                        for re in range(4):
                            k[j][re] = 0
                    else: #k[i][2] <= k[j][2]:
                        k[j][2] += k[i][2]
                        for re in range(4):
                            k[i][re] = 0

        for i in range(K):
            if k[i][0] == 0 or k[i][1] == 0 or k[i][0] == N-1 or k[i][1] == N-1:
                if k[i][3] == 0:
                    continue
                k[i][2] //= 2
                if k[i][2] == 0:
                    for re in range(4):
                        k[i][re] = 0
                else:
                    k[i][3] = dir_reverse[k[i][3]]
        time += 1
        # for i in range(K):
        #     print(k[i])
        # print('--------------')
    for z in range(K):
        result += k[z][2]


    print(f'#{tc} {result}')