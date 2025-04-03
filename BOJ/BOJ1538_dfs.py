'''
dfs로 판별
감소 하는 수의 마지막은 9876542310 => 5000개 일 때 5001부터는 -1 출력
dfs로 수를 하나씩 붙여야 함.
백트래킹으로 그 다음 수가 첫 수보다 크면 return(백트래킹)
마지막 수가 0이 되면 그건 끝
2자리 .. 3자리 .. 4자리 ..

'''
def dfs(n):
    global cnt

    if len(num) == n:
        cnt += 1
        return

    if len(num) < 1:
        cnt += 1
        return

    if len(num) >= 2:
        if num[len(num)-1] >= num[len(num)-2]:
            return
    cnt += 1
    for i in range(10):
        num.append(i)
        dfs()
        num.pop(0)


N = int(input())
num = []
cnt = 0
flag = False
for n in range(1,11):
    dfs(n)
    if flag == True:
        break
