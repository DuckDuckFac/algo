'''
감소하는 수

#입력
N : N번째 감소하는 수

# 구조
자릿수를 비교하면서 모두 감소하면 +1
2라면 2개 (1,0)
3이라면 3개 (2,1,0)
N이라면 N개

while i != N:

숫자가 몇자리 인지 파악 후 K까지 돌리기
3자리 인 경우
i//10^len(i)-1
i%10



'''
N = int(input())
i = 10   # 비교 할 숫자
K = 10   # 순서
# 9876543210
if N <= 10:
    i = N
else:
    while K != N:
        if i > 9876543210:
            i = -1
            break
        num = i
        comp = 0
        for j in range(len(str(i))-1,0,-1):
            comp = num // (10 ** j)
            num %= (10 ** j)
            if comp <= (num // (10**(j-1))):
                break
        else:
            K += 1

        i += 1



print(i)