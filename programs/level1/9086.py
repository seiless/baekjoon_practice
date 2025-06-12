# 주어진 문자열의 첫 글자, 마지막 글자 출력하는 프로그램
# 맨 앞줄엔 테스트 케이스의 숫자 N을 input

test_case = int(input())
for i in range(test_case):
    # 문자열 S를 input
    S = input()
    # 첫 글자와 마지막 글자를 출력 이때 붙여서 출력
    print(S[0]+S[-1])