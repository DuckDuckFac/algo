'''
DFS
'''
def dfs(idx,end,cnt):
    global mx
    mx = max(mx,cnt)
    for k in range(idx+1,N):
        if end <= meeting[k][0]:
            dfs(k,meeting[k][1],cnt+1)

N = int(input())
meeting = []
check = 0
mx = 1
for _ in range(N):
    meeting.append(list(map(int,input().split())))

meeting.sort()
meeting.sort(key=lambda x:x[1])

for i in range(N):
    dfs(i,meeting[i][1],1)

print(mx)