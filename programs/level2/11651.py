case_num = int(input())

case_list = []
for i in range(case_num):
    case_list.append(list(map(int,input().split())))

sorted_lst = sorted(case_list, key=lambda x: (x[1], x[0]))

for case in sorted_lst:
    print(*case)