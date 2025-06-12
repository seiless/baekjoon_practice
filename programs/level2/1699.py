N = int(input())
import math

dp = [i for i in range(N+1)]

for i in range(1,N+1):
    for j in range(1, int(math.sqrt(i)) + 1):
        square = j * j
        dp[i] = min(dp[i], dp[i - square] + 1)
print(dp[N])
