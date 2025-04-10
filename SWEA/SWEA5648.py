'''
SWEA5648
시뮬레이션은 그냥 돌리는게 낫다.


# 구조
1. 범위를 2배로 늘린다.
for 4001
    1. 원자를 이동 시킨다.
    2. 좌표를 넣고, dict에도 넣고
    3.


'''
from collections import defaultdict

dy = [1,-1,0,0]
dx = [0,0,-1,1]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    atoms = [list(map(int,input().split())) for _ in range(N)]
    answer = 0
    for atom in atoms:
        atom[0] *= 2
        atom[1] *= 2

    for i in range(4001):
        cross_pos = defaultdict(list)
        new_atom = []
        for x, y, d, a in atoms:
            nx = x + dx[d]
            ny = y + dy[d]
            new_atom.append([nx, ny, d, a])
            cross_pos[(nx, ny)].append(a)

        remove_set = set()
        for pos, values in cross_pos.items():
            if len(values) >= 2:
                answer += sum(values)
                remove_set.add(pos)

        atoms = [atom for atom in new_atom if (atom[0],atom[1]) not in remove_set]

    print(f'#{tc} {answer}')









