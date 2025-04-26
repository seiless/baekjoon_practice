# 입력
# 첫째 줄에 N(1 ≤ N ≤ 1,000,000,000)이 주어진다.

# 출력
# 입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다.

input_num = int(input())

def calc_sum(N):
    return 6*int((N*(N+1))/2) + 1
count = 0
while input_num > calc_sum(count):
    count = count + 1
print(count + 1)