import sys

cases = sys.stdin.read().splitlines()
num_test_case = int(cases[0])
for case in cases[1:]:
    miss_number, char = case.split()
    miss_number = int(miss_number) - 1
    print(char[:miss_number] + char[miss_number + 1 :])
