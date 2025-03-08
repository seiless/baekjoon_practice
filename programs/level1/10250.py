import sys

keys = [
    "Height",
    "Weight",
    "Number"
]

lines = sys.stdin.read().splitlines()
N = int(lines[0])
values = lines[1:N+1]

print(values)