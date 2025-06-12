P = int(input())
# S의 길이 M이 주어진다
M = int(input())
# 문자열 S가 주어진다
S = input()

# 기본적인 문자열
Char = 'I'
# input으로 받은 숫자만큼 OI를 반복해서 붙여넣는다.
Char_result = Char + 'OI' * P

# 주어진 문자열 S안에서 Char_result가 몇 번 등장하는지 세기
count = 0
# 문자열 S의 길이 M에서 Char_result의 길이 P*2 + 1만큼의 범위를 앞에서부터
# 슬라이딩 방식으로 탐색하면서 비교하기
for i in range(M - (P * 2 + 1) + 1):
    if S[i:i + P * 2 + 1] == Char_result:
        count += 1
# 결과 출력
print(count)