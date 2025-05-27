N = int(input())

dp = [0] * (N + 1)

def get_candidates(i, dp):
    candidates = [dp[i - 1]]
    if i % 2 == 0:
        candidates.append(dp[i // 2])
    if i % 3 == 0:
        candidates.append(dp[i // 3])
    return candidates

for i in range(2, N + 1):
    dp[i] = min(get_candidates(i, dp)) + 1

print(dp[N])

