'''

# 입력 데이터
L, C : 암호 숫자, 전체 암호 갯수
password = list(map(str, input().split())

조합으로 짜면 됨.
ord를 기준으로 짜면 될듯합니다.

'''
def dfs(cnt,idx):
    global result


    if cnt == L:
        num_vowel = 0
        for k in result:
            if k in vowel:
                num_vowel += 1

        if num_vowel >= 1 and L - num_vowel >= 2:
            print("".join(result))
            return
        return

    for i in range(idx,C):
        result.append(password[i])
        dfs(cnt+1, i+1)
        result.pop()


L, C = map(int,input().split())
password = list(map(str,input().split()))
vowel = set(('a','e','i','o','u'))
result = []

# for i in range(C):
#     print(ord(password[i]))

password.sort()
# print(password)


dfs(0,0)

