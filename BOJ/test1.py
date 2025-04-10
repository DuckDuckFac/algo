def brainfuck(M, C, I, code, alpha):
    memory = [0] * M
    pointer = 0
    pc = 0
    input_pointer = 0
    steps = 0
    MAX_STEPS = 50000000
    code_len = len(code)

    # 괄호 짝 찾기
    bracket = {}
    stack = []
    for i in range(code_len):
        if code[i] == '[':
            stack.append(i)
        elif code[i] == ']':
            j = stack.pop()
            bracket[i] = j
            bracket[j] = i

    visited = [0] * code_len
    jump_counts = [0] * code_len

    while pc < code_len and steps < MAX_STEPS:
        visited[pc] += 1
        command = code[pc]
        if command == '+':
            memory[pointer] = (memory[pointer] + 1) % 256
        elif command == '-':
            memory[pointer] = (memory[pointer] - 1) % 256
        elif command == '>':
            pointer = (pointer + 1) % M
        elif command == '<':
            pointer = (pointer - 1 + M) % M
        elif command == '[':
            if memory[pointer] == 0:
                pc = bracket[pc]
        elif command == ']':
            if memory[pointer] != 0:
                jump_counts[pc] += 1
                pc = bracket[pc]
        elif command == ',':
            if input_pointer >= I:
                memory[pointer] = 255
            else:
                memory[pointer] = ord(alpha[input_pointer])
                input_pointer += 1
        pc += 1
        steps += 1

    if steps < MAX_STEPS:
        return "Terminates"
    else:
        # 무한 루프 탐지
        loop_start = loop_end = 0
        max_len = -1
        stack = []
        for idx in range(code_len):
            if code[idx] == '[':
                stack.append(idx)
            elif code[idx] == ']':
                open_idx = stack.pop()
                s, e = open_idx, idx
                if sum(jump_counts[s:e+1]) > 0:
                    if (e - s) > max_len:
                        max_len = e - s
                        loop_start, loop_end = s, e
        return f"Loops {loop_start} {loop_end}"


# BOJ 스타일 입력 처리
T = int(input())
for _ in range(T):
    M, C, I = map(int, input().split())
    code = input()
    alpha = input()
    print(brainfuck(M, C, I, code, alpha))
