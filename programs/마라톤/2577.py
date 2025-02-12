import sys
from collections import Counter

answer_num = 1
for e in map(int, sys.stdin):
    answer_num = answer_num * e

def count_digits(n):
    num_str = str(n)
    digit_count = Counter(num_str) 
    full_count = {str(i): 0 for i in range(10)}
    full_count.update(digit_count)
    return {k: int(v) for k, v in full_count.items()}

answer_dict = count_digits(answer_num)

for key in answer_dict.keys():
    print(answer_dict[key])