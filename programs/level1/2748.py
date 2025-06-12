N = int(input())

dps = [0] * (N + 1)
dps[1] = 1
for i in range(2, N + 1):
    dps[i] = dps[i - 1] + dps[i - 2]

print(dps[N])