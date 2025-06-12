# 행렬의 크기 N과 M
N,M = map(int, input().split())
# 행렬 A의 크기 N x M
A = [list(map(int, input().split())) for _ in range(N)]
# 행렬 B의 크기 N x M
B = [list(map(int, input().split())) for _ in range(N)]

# 행렬 A와 B의 합을 구하기
C = [[0] * M for _ in range(N)]
# 행렬 A와 B의 합 C를 출력하기
for i in range(N):
    for j in range(M):
        C[i][j] = A[i][j] + B[i][j]
# 결과 출력
for row in C:
    print(' '.join(map(str, row)))