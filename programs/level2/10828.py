command_num = int(input())

stack_list = []
output_list = []
for command in range(command_num):
    given_command = input().split()
    if given_command[0] == "push":
        stack_list.append(given_command[1])
    elif given_command[0] == "pop":
        if len(stack_list) > 0:
            output_list.append(stack_list[-1])
            stack_list.pop()
        else:
            output_list.append(-1)
    elif given_command[0] == "size":
        output_list.append(len(stack_list))
    elif given_command[0] == "empty":
        output_list.append(1 if len(stack_list) == 0 else 0)
    elif given_command[0] == "top":
        if len(stack_list) > 0:
            output_list.append(stack_list[-1])
        else:
            output_list.append(-1)

print('\n'.join(map(str, output_list)))