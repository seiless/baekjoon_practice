case_num = int(input())
case_list = []
for i in range(case_num):
    floor_num = int(input())
    room_num = int(input())
    case_list.append([floor_num, room_num])

from itertools import accumulate

def recursive_cumsum(base_list, n):
    result = base_list
    for _ in range(n):
        result = list(accumulate(result))
    return result


# 정수가 주어졌을때 그 정수길이만큼의 리스트를 작성하는 함수
def get_list(int_val):
    return [i+1 for i in range(int_val)]

for case in case_list:
    base_list = get_list(case[1])
    result_list = recursive_cumsum(base_list, case[0])
    print(result_list[-1])