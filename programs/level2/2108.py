import sys
from collections import Counter

case_all = [int(line.strip()) for line in sys.stdin]
case_num = case_all[0]
case_list = case_all[1:]
median_num = int(case_num/2)

def get_mode(data):
    counter = Counter(data)
    max_count = max(counter.values())
    modes = sorted([k for k, v in counter.items() if v == max_count])
    if len(modes) >= 2:
        return modes[1]
    else:
        return modes[0]

sorted_list = sorted(case_list)
print(round(sum(case_list)/case_num))
print(sorted_list[median_num])
print(get_mode(case_list))
print(sorted_list[case_num-1] - sorted_list[0])