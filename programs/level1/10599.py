import sys

data = sys.stdin.read().splitlines()
cases = [list(map(int, s.split())) for s in data[0:]]

for case in cases:
    if case == [0, 0, 0, 0]:
        break
    else:
        case1 = max(case[2], case[3]) - min(case[0], case[1])
        case2 = min(case[2], case[3]) - max(case[0], case[1])
        print(min(case1, case2), max(case1, case2))
