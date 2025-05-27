data = sys.stdin.read().splitlines()

N, M = list(map(int,data[0].split()))

site_dict = {}
for i in range(N):
    input_site,password = input().split()
    site_dict[input_site] = password
for j in range(M):
    input_site = input()
    print(site_dict[input_site])