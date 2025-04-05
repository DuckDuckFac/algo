'''
치킨 배달
#입력 데이터
N, M : N 마을 크기 , M 치킨집의 개수
graph[N][N]


#구조
dfs로 치킨 집 바꿔 놓으면서 M개 만큼 놓으면서 최솟값 구하기

for N
    치킨집 좌표 구하기

def dfs():


'''
import itertools
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

chicken_pos = []
house_pos = []

min_dis = float('inf')
def dfs(house,chicken):
    sum = 0
    for k, n in house:
        mn = float('inf')
        for x, y in chicken:
            min_c_h = abs(x-k) + abs(y-n)
            mn = min(min_c_h,mn)
        sum += mn

    return sum

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house_pos.append((i,j))
        if graph[i][j] == 2:
            chicken_pos.append((i,j))



for chicken_store in itertools.combinations(chicken_pos,M):
    min_dis = min(min_dis,dfs(house_pos,chicken_store))

print(min_dis)

