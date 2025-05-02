'''
#입력 데이터
T : tc
N, K : 야구 선수, 실력차이
player = list

#구조
for N
    for i,N
        if 뺀게 k보다 작으면
            ans +1

나를 제외 한 모든 사람들과 비교해서 max를 구하기

팀의 최대 값 선수와 최솟값 선수의 차이가 K이어야 함.
하나씩 뽑으면서

인덱스 하나씩 탐색하면서, 첫번째꺼 K뺴고 그 사이에 있는 모든 수 체크
두 번쨰 K빼고 그 사이에 있는 거 모두 체크

3
4 2
6 4 2 3
4 3
1 2 3 4
4 1
1 3 7 5
'''

T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    player = list(map(int,input().split()))

    ans = 0

    for i in range(N):
        team = 0
        for j in range(N):
            if player[i]-K <= player[j] <= player[i]:
                team += 1
        ans = max(team,ans)
    print(f'#{tc} {ans}')