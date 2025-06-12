# 주어진 문자열의 대소문자를 거꾸로 해서 출력
def reverse(s):
    result = []
    for char in s:
        if char.islower():
            result.append(char.upper())
        elif char.isupper():
            result.append(char.lower())
        else:
            result.append(char)
    return ''.join(result)
print(reverse(input()))