answer_list = []
num = 666
input = int(input())
while len(answer_list) < 187:
    if "666" in str(num):
        answer_list.append(str(num))
        num = num + 1
    else:
        num = num + 1
print(answer_list[-1])