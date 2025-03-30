# 1부터 8까지 차례대로 연주한다면 ascending, 
# 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed
input_pitch = list(map(int,input().split(' ')))
if input_pitch == sorted(input_pitch):
    print('ascending')
elif input_pitch == sorted(input_pitch,reverse=True):
    print('descending')
else:
    print('mixed')