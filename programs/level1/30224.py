# 7을 포함하지도 나누어 떨어지지도 않으면 0
# 7을 포함하지는 않지만 나누어 떨어지면 1
# 7을 포함하지만 나누어 떨어지지 않으면 2
# 7을 포함하고 나누어 떨어지면 3
get_char = input()

def judge_lucky(x):
    if '7' not in x:
        return 0 if int(x)%7 !=0 else 1
    else:
        return 2 if int(x)%7 !=0 else 3
    
print(judge_lucky(get_char))