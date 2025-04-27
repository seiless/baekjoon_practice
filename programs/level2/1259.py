while True:
    case = input().strip()
    if case == '0':
        break
    if case == case[::-1]:
        print('yes')
    else:
        print('no')