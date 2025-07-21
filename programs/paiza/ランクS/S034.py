import math
#整数の長さN コスト計算に必要な整数 a, b
N, A, B = map(int,input().split())
# aは圧縮後の要素数と計算
# bは元のデータとのずれを計算
num_list = list(map(int,input().split()))

dp = [math.inf] * (N + 1)
dp[0] = 0

for i in range(1,N + 1):
    for j in range(i):
        sub_array = num_list[j:i]
        sub_array.sort()
        median = sub_array[(len(sub_array) -1) //2]

        diff_sum = sum(abs(num - median) for num in sub_array)

        segment_cost = (A * 2)+ (B * diff_sum)

        dp[i] = min(dp[i], dp[j] + segment_cost)

print(dp[N])