# 입력받은 그대로 출력하는 프로그램
import sys 
# 몇줄이나 입력받을지 모르기때문에 일단 sys.stdin.readline()을 사용
for line in sys.stdin:
    # 입력받은 줄을 그대로 출력
    print(line, end='')  # end=''를 사용하여 줄바꿈을 방지