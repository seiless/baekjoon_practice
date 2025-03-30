import re
N = int(input())

def calc_sum(X):
    return int((X*(X+1))/2)

for _ in range(N):
    input_answer = re.findall(r'O+', input())
    score_sum = [calc_sum(len(seq)) for seq in input_answer]
    print(sum(score_sum))