# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

N = int(input())

input_numbers = list(map(int, input().split()))

def make_sieve_under_n(n):
    sieve = [True] * 1001
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(1000**0.5) + 1):
        if sieve[i]:
            for j in range(i*i,1001,i):
                sieve[j] = False

    return sieve[n]

answer = 0
for num in input_numbers:
    if make_sieve_under_n(num):
        answer = answer + 1
print(answer)