N = int(input())

def split_string_to_int_list(lst):
    return [int(char) for char in lst]

input_num_list = split_string_to_int_list(input())

print(sum(input_num_list))