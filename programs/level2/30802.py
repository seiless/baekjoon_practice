# 모든 참여자 수 N
N = int(input())
order_list = list(map(int,input().split()))
# 티셔츠의 묶음 주문 가능한 개수 T와 펜의 묶음 주문 가능한 개수 P
T, P = map(int,input().split())

# 첫 줄에 티셔츠를 T장씩 최소 몇 묶음 주문해야 하는지 출력
# 펜을 P자루씩 최대 몇 묶음 주문할 수 있는지와, 그 때 펜을 한 자루씩 몇 개 주문하는지 출력

# 먼저 묶음 티셔츠는 최소 얼마나 주문이 필요한지 계산하는 함수 만들기

def calc_order_t_set_no(order_list):
    order_cnt = 0
    for order in order_list:
        if order % T == 0:
            order_cnt = order_cnt + order // T
        else:
            order_cnt = order_cnt + order // T + 1
    return order_cnt

print(calc_order_t_set_no(order_list))
print(N // P, N % P)
