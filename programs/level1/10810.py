import sys

data = sys.stdin.read().splitlines()
queries = [list(map(int, s.split())) for s in data[1:]]
N, M = list(map(int, data[0].split()))

answer_list = [0] * N

for query in queries:
    start_point = query[0] - 1
    end_point = query[1]
    new_input = query[2]
    answer_list[start_point:end_point] = [new_input] * (end_point - start_point)
print(" ".join(map(str, answer_list)))
