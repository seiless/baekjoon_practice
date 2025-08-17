query_num = int(input())
temp_list = []
for num in range(query_num):
    input_query = list(map(int, input().split()))
    if input_query[0] == 1:
        temp_list.append(input_query[1])
    else:
        print(min(temp_list))
        temp_list.remove(min(temp_list))
