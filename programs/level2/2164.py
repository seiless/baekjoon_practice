N = int(input())
from collections import deque

card_que = deque()
card_list = [i+1 for i in range(N)]
card_que.extend(card_list)

while len(card_que) > 1:
    card_que.popleft()
    card_que.append(card_que.popleft())
print(card_que[0])