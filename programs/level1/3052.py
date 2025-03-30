import sys

numbers = [int(line.strip())%42 for line in sys.stdin if line.strip()]
print(len(set(numbers)))