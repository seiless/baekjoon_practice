import math

N,K = map(int, input().split())

def combinations(N,K):
    return math.factorial(N) // (math.factorial(K) * math.factorial(N - K))

print(combinations(N,K))