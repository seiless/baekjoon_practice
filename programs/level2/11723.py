input_isbn = input()
sum_isbn = 0
for i in range(0,12):
    if input_isbn[i] == "*":
        temp_num = 0
    else:
        temp_num = int(input_isbn[i])
    if i % 2 == 0:
        sum_isbn += temp_num
    else:
        sum_isbn += temp_num * 3
for i in range(0,10):
    if (10 - (sum_isbn + i) % 10)==int(input_isbn[-1]):
        print(i)
        break