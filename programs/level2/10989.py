import sys

case_num = int(sys.stdin.readline().strip())

count = [0] * (10001)

for _ in range(case_num):
    num = int(sys.stdin.readline().strip())
    count[num] += 1

for num in range(1, 10001):
    if count[num] > 0:
        for _ in range(count[num]):
            print(num)