import sys
from collections import deque
num_queries = int(sys.stdin.readline())
storage = deque()
for _ in range(num_queries):
    line = sys.stdin.readline().split()

    if line[0] == "1" and line[0] == "2":
        continue
    query_type = line[0]

    if query_type == "1":
        count = int(line[1])
        value = int(line[2])
        storage.append([value,count])

    elif query_type == "2":
        pop_count = int(line[1])
        current_sum = 0
        while pop_count > 0 and storage:
            front_block_value, front_block_count = storage[0]
            if front_block_count <= pop_count:
                current_sum += front_block_value * front_block_count
                pop_count -= front_block_count
                storage.popleft()
            else:
                current_sum += pop_count * front_block_value
                storage[0][1] -= pop_count
                pop_count = 0
        print(current_sum)