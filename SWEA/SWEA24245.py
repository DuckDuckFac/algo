T = int(input())

for tc in range(1,T+1):
    # 1: 가위 2: 바위 3: 보
    hyeongtak, yongji = map(int,input().split())

    # 이기는 경우
    if hyeongtak == 1 and yongji == 3:
        print(f'#{tc} {hyeongtak}')
    elif hyeongtak == 2 and yongji == 1:
        print(f'#{tc} {hyeongtak}')
    elif hyeongtak == 3 and yongji == 2:
        print(f'#{tc} {hyeongtak}')

    # 진 경우
    if hyeongtak == 3 and yongji == 1:
        print(f'#{tc} {2}')
    elif hyeongtak == 2 and yongji == 3:
        print(f'#{tc} {1}')
    elif hyeongtak == 1 and yongji == 2:
        print(f'#{tc} {3}')
    # 비긴 경우

    if hyeongtak == yongji:
        print(f'#{tc} {hyeongtak}')