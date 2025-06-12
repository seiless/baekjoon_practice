# 주어진 숫자 A와 B를 입력받아서
# (A + B) x (A - B)의 결과를 출력하는 프로그램
# A와 B를 입력받기
A, B = map(int, input().split())

def calculate_expression(A, B):
    return (A + B) * (A - B)
# 결과 계산
print(calculate_expression(A, B))