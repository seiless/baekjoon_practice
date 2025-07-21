# 宝石の種類Nと運べる総体積V
N, V = map(int,input().split())
gem_list = []
for i in range(N):
    gem_list.append(tuple(map(int,input().split())))
items = []

for value, volume, count in gem_list:
    k = 1
    while count > 0:
        take = min(k, count)
        items.append((value * take, volume * take))
        count -= take
        k *= 2

dp = [0] * (V + 1)

for value, volume in items:
    for j in range(V, volume -1, -1):
        dp[j] = max(dp[j], dp[j - volume] + value)

print(dp[V])