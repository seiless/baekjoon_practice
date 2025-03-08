# 분해합 구하기

# 아직 정답 못함
N = int(input())

def calc(N):
    answer_list = []
    if N < 10:
        for i in range(1,10):
            if 2 * i == N:
                answer_list.append(i)
    elif 10 <= N < 99:
        for i in range(0,10):
            for j in range(0,10):
                if 11 * i + 2 * j == N:
                    answer_list.append(i * 10 + j)
    else:
        for i in range(0,10):
            for j in range(0,10):
                for k in range(0,10):
                    if i * 101 + 11 * j + 2 * k == N:
                        answer_list.append(i * 100 + 10 * j + k)
    
    if len(answer_list) == 0:
        print(0)
    else:
        print(min(answer_list))

calc(N)