# 서울의 오늘 날짜를 출력하는 프로그램 작성
import time

today = time.strftime("%Y-%m-%d", time.localtime())
print(today)