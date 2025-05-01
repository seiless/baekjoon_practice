import sys
input_num = int(input())
data = set(map(int, sys.stdin.read().split()))
print('\n'.join(map(str, sorted(data))))