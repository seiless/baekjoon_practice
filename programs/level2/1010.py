test_case = int(input())
test_list = []
for i in range(test_case):
    test_list.append(list(map(int, input().split())))

all_n, all_m = zip(*test_list)

rows = max(all_n)
cols = max(all_m)

matrix = [[0 for _ in range(cols)] for _ in range(rows)]

for row in range(rows):
    for col in range(cols):
        if row == 0:
            matrix[row][col] = col + 1
        elif row == col:
            matrix[row][col] = 1
        elif col > row:
            matrix[row][col] = matrix[row][col - 1] + matrix[row - 1][col - 1]

for test in test_list:
    n, m = test
    print(matrix[n-1][m-1])