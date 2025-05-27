T = int(input())

test_case = []
for i in range(T):
    test_case.append(int(input()))

max_value = max(test_case) + 1

dp_0 = [0] * max_value
dp_1 = [0] * max_value

for i in range(max_value):
    if i == 0:
        dp_0[i] = 1
    elif i == 1:
        dp_1[i] = 1
    else:
        dp_0[i] = dp_0[i-1] + dp_0[i-2]
        dp_1[i] = dp_1[i-1] + dp_1[i-2]
for case in test_case:
    print(dp_0[case], dp_1[case])
