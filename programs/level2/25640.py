# MBTI같은 사람 수 출력

ANSWER_MBTI = input()
member_no = int(input())

answer_list = [mbti for _ in range(member_no) if (mbti := input()) == ANSWER_MBTI]
print(len(answer_list))