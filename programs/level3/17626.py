import sys
import math

# 입력 빠르게 받기
N = int(sys.stdin.readline())

# 초기화
dp = [0] + [float('inf')] * N
squares = [i * i for i in range(1, int(math.isqrt(N)) + 1)]

# DP 계산
for i in range(1, N + 1):
    for square in squares:
        if square > i:
            break
        dp[i] = min(dp[i], dp[i - square] + 1)

print(dp[N])