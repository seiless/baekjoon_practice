N = int(input())

dps = [0] * (N + 1)
dps[1] = 1
dps[2] = 2

for i in range(3,N + 1):
    dps[i] = (dps[i - 1] + dps[i - 2])%15746

print(dps[N])
