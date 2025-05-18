case_num = int(input())
case_dict = {}

for i in range(case_num):
    case_dict[i] = list(map(int,input().split()))
answer_case = [1] * case_num

for case_num, value in case_dict.items():
    for others_num, others_value in case_dict.items():
        if case_num != others_num:
            if value[0] < others_value[0] and value[1] < others_value[1]:
                answer_case[case_num] = answer_case[case_num] + 1
                
            
print(*answer_case)