a = input()
b = input()
c = input()

print_output = 0

def return_fizzbuzz(n):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 == 0:
        print("Fizz")
    else:
        print(n)

if a not in ["Fizz", "Buzz", "FizzBuzz"]:
    # 셋 다 아니면 자연수니깐 그냥 숫자 더하기
    print_output = int(a) + 3
elif a == "FizzBuzz":
    # 맨 앞이 FizzBuzz인 경우(1가지밖엔 없음) b에 바로 2더하기
    print_output = int(b) + 2
elif a == "Buzz":
    # 맨 앞이 Buzz인 경우, b는 자연수이거나 Fizz 총 2가지 경우
    if b == "Fizz":
        print_output =int(c) + 1
    else:
        print_output = int(b) + 2
else:
    # 맨 앞이 Fizz인 경우, c가 Buzz인 경우(1가지)와 그 외의(3가지) 경우
    if c == "Buzz":
        print_output = int(b) + 2
    else:
        print_output = int(c) + 1

return_fizzbuzz(print_output)
