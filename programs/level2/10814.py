input_num = int(input())
case_dict = {}

for case in range(input_num):
    Age, Name = input().split()
    Age = int(Age)
    if Age not in case_dict:
        case_dict[Age] = []
    case_dict[Age].append(Name)

for key, value in dict(sorted(case_dict.items())).items():
    for name in value:
        print(key,name)