# 数列を定めるために使う整数K
import itertools
K = int(input())
sublist_generator = ([X] * M for M, X in (map(int, input().split()) for _ in range (K)))
case = list(itertools.chain.from_iterable(sublist_generator))
# 文字列を作成
length_str = int(len(case)/2)
answer = sum(abs(case[i] - case[i + length_str]) for i in range(length_str))
print(answer)
