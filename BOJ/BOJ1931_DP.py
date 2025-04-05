from bisect import bisect_right

N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]

# 회의를 끝나는 시간 기준으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

# 끝나는 시간만 따로 리스트로 저장 (정렬과 동일한 순서)
end_times = [end for start, end in meetings]

# dp[i]: i번째 회의까지 고려했을 때 최대 선택 개수
dp = [0] * N

for i in range(N):
    start_i, end_i = meetings[i]

    # end <= start 조건 만족하는 회의 중 가장 마지막 인덱스
    idx = bisect_right(end_times, start_i) - 1

    # 이전 회의까지 고려한 최댓값
    without_current = dp[i - 1] if i > 0 else 0

    # 현재 회의 포함한 경우
    with_current = (dp[idx] if idx >= 0 else 0) + 1

    dp[i] = max(without_current, with_current)

print(dp[-1])
