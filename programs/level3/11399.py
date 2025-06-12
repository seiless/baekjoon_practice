N = int(input())
# 사람별로 돈을 인출하는데 걸리는 시간
money_time = list(map(int, input().split()))

# 각 사람이 인출하는데 필요한 시간의 합을 최소로 하는 방법
# 돈을 인출하는데 걸리는 시간이 적은 사람부터 순서대로 인출하게 정렬
money_time.sort()

# 각 사람이 인출하는데 걸리는 합을 구하기
each_total_time = 0
total_time = [0] * N
for i in range(N):
    each_total_time += money_time[i]
    total_time[i] = each_total_time
print(sum(total_time))