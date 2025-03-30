test_case_num = int(input())

test_case_list = []

for _ in range(test_case_num):
    test_case_list.append(input().split())

for case in test_case_list:
    repeat_num = int(case[0])
    repeat_char = case[1]
    print_char = ''
    for char in repeat_char:
        print_char = print_char + repeat_num * char
    print(print_char)
