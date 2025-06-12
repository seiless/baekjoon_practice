input_isbn = list(input())
check_sum = 0
deleted_num = -1
for i in range(0,12):
    if input_isbn[i] == "*":
        deleted_num = i
        input_isbn[i] = "0"
    if i % 2 == 0:
        check_sum += int(input_isbn[i])
    else:
        check_sum += int(input_isbn[i]) * 3
for j in range(10):
    temp_sum = 0
    if deleted_num % 2 == 0:
        temp_sum = check_sum + j
    else:
        temp_sum = check_sum + (j * 3)

    calculated_check_digit = (10 - (temp_sum % 10)) % 10
    
    if calculated_check_digit == int(input_isbn[-1]):
        print(j)
        break

