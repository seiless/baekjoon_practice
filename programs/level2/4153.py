import sys
import math
def split_and_calc_pythagoras(lst):
    sorted_list = sorted(lst,reverse = True)
    X,Y,Z = sorted_list[0],sorted_list[1],sorted_list[2]
    if X >= Y + Z:
        answer = "wrong"
    else:
        answer = "right" if X**2 == Y**2 + Z**2 else "wrong"
    return answer

for line in sys.stdin:
    a, b, c = map(int, line.strip().split())
    if a == 0 and b == 0 and c == 0:
        break
    print(split_and_calc_pythagoras([a, b, c]))