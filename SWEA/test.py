from collections import defaultdict

# 상(0), 하(1), 좌(2), 우(3)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    atoms = [list(map(int, input().split())) for _ in range(N)]

    # 좌표 2배 확장 (0.5단위 충돌 표현)
    for atom in atoms:
        atom[0] *= 2  # x
        atom[1] *= 2  # y

    total_energy = 0
    for _ in range(4001):  # 최대 4000 step이면 충분
        if not atoms:
            break

        pos_map = defaultdict(list)
        new_atoms = []

        # 이동
        for x, y, d, k in atoms:
            nx = x + dx[d]
            ny = y + dy[d]
            # 범위를 벗어나면 소멸
            if not (-2000 <= nx <= 2000 and -2000 <= ny <= 2000):
                continue
            pos_map[(nx, ny)].append(k)
            new_atoms.append([nx, ny, d, k])

        # 충돌 감지 및 에너지 합산
        exploded_pos = set()
        for pos, energies in pos_map.items():
            if len(energies) >= 2:
                total_energy += sum(energies)
                exploded_pos.add(pos)

        # 충돌한 원자 제거
        atoms = [atom for atom in new_atoms if (atom[0], atom[1]) not in exploded_pos]

    print(f"#{tc} {total_energy}")
