import sys
import math
def split_and_calc_pythagoras(lst):
    sorted_list = sorted(lst,reverse = True)
    X = sorted_list[0]
    Y,Z = sorted_list[1],sorted_list[2]
    answer = "right" if X**2 == Y**2 + Z**2 else "wrong"
    return answer

for e in sys.stdin:
    if e != '0 0 0':
        input_list = list(map(int,e.split()))
        print(split_and_calc_pythagoras(input_list))