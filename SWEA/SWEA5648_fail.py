'''
SWEA5648 원자 소멸 시뮬레이션

# 입력 데이터
T : tc
N : 원자의 수
atom[N] = 0 : x(c), 1 : y(r), 2 : 이동 방향, 3 : K(보유 에너지)
delta

# 구조
while atom:
    atom.sort()



# 생각해봐야 할 것들
1. 두 좌표가 양쪽에서 오는 경우 미리 터트려 둬도 되나? X
    만약 정렬을 하면 되나? 정렬을 하면 될거같긴하다. 그럼 미리 터트려도 되지않나

    A, G 가 터진 경우 B, D 는 만나지 못 함. 그래서 원소들이 크로스 되는 경우에만.
    2가지 경우
    1. 한 점에서 만나는 경우
    2. 두 원자가 한 좌표에서 만나지 않고 스치고 지나가는 경우

2. 모든 원소가 겹치지 않을 것이라는 장담 할 수 있는 경우
    만날 가능성이 없는 애 pop
        ㄱ. 상
            a)하 하보다 y가 상이 더 크면 안됨
            b)좌 좌보다 y가 상이 더 크면 안됨
            c)우 우보다 y가 상이 더 크면 안됨

        ㄴ. 하
            a)상 상보다 y가 하가 더 작으면 안됨. (겹침)
            b)좌 좌보다 y가 하가 더 작으면 안됨.
            c)우 우보다 y가 하가 더 작으면 안됨.

        ㄷ. 좌
            a)우 우보다 x가 좌가 더 작은 경우
        ㄹ. 우
        ==> 하나로 합쳐도 될 것 같은데 상 / 좌 우 하 , 하 / 좌 우 상 , 좌 / 우

    x가 같은 상태에서 뒤 ?
    y가 같은 상태에서 양옆 ?
'''
dr = [-1,1,0,0]
dc = [0,0,-1,1]
T = int(input())
N = int(input())
atom = [list(map(int,input().split())) for _ in range(N)]
result = 0
while atom:
    idx = 0
    atom.sort(key=lambda x: x[0])
    while idx < len(atom):
        j = idx + 1
        if (atom[idx][1] == atom[j][1]) and (atom[idx][2] == 3 and atom[j][2] == 2):
            result += atom[idx][3] + atom[j][3]
            atom.pop(j)
            atom.pop(idx)
            continue
        idx += 1

    idx = 0
    atom.sort(key=lambda x: x[1])
    while idx < len(atom):
        j = idx + 1
        if (atom[idx][0] == atom[j][0]) and (atom[idx][2] == 0 and atom[j][2] == 1):
            result += atom[idx][3] + atom[j][3]
            atom.pop(j)
            atom.pop(idx)
            continue
        idx += 1
    #for else?
    for j in range(len(atom)-1,0,-1):
        for i in range(j-1,-1,-1):
            if atom[j][2] == 0:
                if atom[j][1] < atom[i][1]:
                    break
            elif atom[i][2] == 1:
                if atom[j][1] > atom[i][1]:
                    break
            elif atom[i][2] == 2:
                if atom[j][0] > atom[i][0]:
                    break
            elif atom[i][2] == 3:
                if atom[j][0] < atom[i][0]:
                    break
        else:
            atom.pop(j)

    for k in range(len(atom)):
        atom[k][0] += dc[atom[k][2]]
        atom[k][1] += dr[atom[k][2]]

    same_pos = set() # 같은 좌표의 인덱스
    for i in range(len(atom)-1):
        for j in range(i+1,len(atom)):
            if atom[i][0] == atom[j][0] and atom[i][1] == atom[j][1]:
                same_pos.add(i)
                same_pos.add(j)

    same_pos_lst = [x for x in same_pos]
    same_pos_lst.sort(reverse=True)
    for i in same_pos_lst:
        result += atom[i][3]
        atom.pop(i)