import sys

data = sys.stdin.read().splitlines()

N, M = list(map(int,data[0].split()))

not_listened = set(data[1:N+1])
not_seemd = set(data[N+1:N+M+1])
answer_list = sorted(list(not_listened & not_seemd))
print(len(answer_list))
print('\n'.join(answer_list))