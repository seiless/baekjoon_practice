test_case_num = int(input())

test_case_dict = {}

for _ in range(test_case_num):
    key, value = input().split()
    test_case_dict[key] = value
    
for key in test_case_dict:
    key_int = int(key)
    print_value = ''
    for char in test_case_dict[key]:
        print_value = print_value + (char*key_int)
    print(print_value)