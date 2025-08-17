TEST_CASE = int(input())

CASE_LIST = [0] * TEST_CASE

for i in range(TEST_CASE):
    CASE_PRICE = int(input())
    OPTION_CASE = int(input())
    CASE_LIST[i] = CASE_LIST[i] + CASE_PRICE
    if OPTION_CASE != 0:
        for j in range(OPTION_CASE):
            OPTION_NUM, OPTION_PRICE = list(map(int, input().split()))
            CASE_LIST[i] = CASE_LIST[i] + (OPTION_NUM * OPTION_PRICE)
for PRICE in CASE_LIST:
    print(PRICE)
