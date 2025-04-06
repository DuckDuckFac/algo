'''
dfs로 판별
감소 하는 수의 마지막은 9876542310 => 1022
dfs로 수를 하나씩 붙여야 함.
백트래킹으로 그 다음 수가 첫 수보다 크면 return(백트래킹)
마지막 수가 0이 되면 그건 끝
2자리 .. 3자리 .. 4자리 ..

'''
def dfs(n):
    global cnt, save

    if len(num) >= 2:
        if num[len(num)-1] >= num[len(num)-2]:
            return

    if len(num) == n:
        cnt += 1
        if cnt == N:
            save = num[:]
            flag = True
            return
        return

    for i in range(10):
        num.append(i)
        dfs(n)
        num.pop()
        if cnt == N:
            return
# 전체 함수가 리턴 되어야 함 근데 그게 안 되고 있음.

N = int(input())
num = []
cnt = -1
flag = False
if N > 1022:
    print(-1)
else:
    for n in range(1,11):
        dfs(n)
        if flag == True:
            break
    for i in range(len(save)):
        print(save[i], end = "")