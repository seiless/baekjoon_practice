import sys

data = sys.stdin.read().splitlines()

N, M = list(map(int, data[0].split()))
S = list(data[1])
T = list(data[2])
queries = [list(map(int, s.split())) for s in data[3:]]

for query in queries:
    L = query[0] - 1
    R = query[1]
    for i in range(L,R):
        S[i], T[i] = T[i], S[i]
print("".join(S))
