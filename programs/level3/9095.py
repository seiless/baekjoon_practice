N = int(input())

test_case = []
for i in range(N):
    test_case.append(int(input()))

max_value = max(3, max(test_case) + 1)
dp = [0] * max_value
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3,max_value):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
for test in test_case:
    print(dp[test])