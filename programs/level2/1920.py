given_num = int(input())
num_set = set(list(map(int,input().split())))
find_num = int(input())
find_list = list(map(int,input().split()))

exist_num = num_set & set(find_list)
for i in find_list:
    print(1 if i in exist_num else 0)