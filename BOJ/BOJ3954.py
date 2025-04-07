T = int(input())
for _ in range(T):
    M, C, I = map(int, input().split())
    graph = [0] * M
    codes = list(input())
    alpha = list(input())

    # 괄호 매칭 저장
    par = {}
    stack = []
    for idx, code in enumerate(codes):
        if code == '[':
            stack.append(idx)
        elif code == ']':
            open_idx = stack.pop()
            par[open_idx] = idx
            par[idx] = open_idx

    pointer = 0
    i = 0
    alp = 0
    repeat = 0

    # 실제 실행
    visited = [0] * C
    jump_counts = [0] * C  # ] → [ 점프 카운트
    last_i = 0

    while i < C and repeat < 50000000:
        visited[i] += 1
        if codes[i] == '+':
            graph[pointer] = (graph[pointer] + 1) % 256
        elif codes[i] == '-':
            graph[pointer] = (graph[pointer] - 1) % 256
        elif codes[i] == '<':
            pointer = (pointer - 1 + M) % M
        elif codes[i] == '>':
            pointer = (pointer + 1) % M
        elif codes[i] == '[':
            if graph[pointer] == 0:
                i = par[i]
                continue
        elif codes[i] == ']':
            if graph[pointer] != 0:
                jump_counts[i] += 1
                i = par[i]
                continue
        elif codes[i] == ',':
            if alp >= I:
                graph[pointer] = 255
            else:
                graph[pointer] = ord(alpha[alp])
                alp += 1
        i += 1
        repeat += 1
        last_i = i  # 마지막 명령어 위치 기록

    if repeat >= 50000000:
        # 무한루프 발생 → 점프 횟수가 존재한 루프 중 가장 바깥 루프 출력
        loop_start = loop_end = 0
        max_len = -1
        stack = []
        for idx in range(C):
            if codes[idx] == '[':
                stack.append(idx)
            elif codes[idx] == ']':
                open_idx = stack.pop()
                s, e = open_idx, idx
                jump_sum = sum(jump_counts[s:e+1])
                if jump_sum > 0:
                    if (e - s) > max_len:
                        max_len = e - s
                        loop_start, loop_end = s, e
        print(f"Loops {loop_start} {loop_end}")
    else:
        print("Terminates")
