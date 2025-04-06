'''
전깃줄
#입력데이터

#구조
1,8 그 사이에 있으면 뺸다??

'''
import bisect

N = int(input())
elec = []
for _ in range(N):
    x, y = map(int,input().split())
    elec.append([x,y])

elec.sort()
print(elec)

B = []
for i in range(N):
    B.append(elec[i][1])
print(B)

lis = []
for j in range(N):
    num = B[j]
    pos = bisect.bisect_left(lis,num)
    if pos == len(lis):
        lis.append(num)
    else:
        lis[pos] = num


dp = [0]* (N+1)
for i in range(1, N):
    mx = 0
    for j in range(1,i):
        if B[i] > B[j]:
            mx = max(mx,dp[j])
    dp[i] = mx+1

print(N-len(lis))