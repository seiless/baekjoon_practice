r = 31
M = 1234567891

str_length = int(input())
get_str = input()
ans = 0
for i in range(str_length):
    ans = ans + (ord(get_str[i])-96) * r**i
print((ans)%M)