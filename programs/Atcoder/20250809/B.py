input_str = input()
len_str = len(input_str)
# len_strの値が3未満なら、そもそも0


def calc_filling_factor(x, t):
    return (x - 2) / (t - 2)


def find_t(str):
    return str.count("t")


if len_str < 3:
    print(0)
# len_strが十分な値の時だけ、動的計画法?
else:
    answer_list = []
    for i in range(len_str):
        temp_str = input_str[i:]
        for j in range(len(temp_str)):
            temp_str_for_answer = temp_str[: j + 1]
            if (
                temp_str[0] == "t"
                and temp_str[j] == "t"
                and len(temp_str_for_answer) >= 3
            ):
                answer_list.append(
                    calc_filling_factor(
                        find_t(temp_str_for_answer), len(temp_str_for_answer)
                    )
                )
    if answer_list == []:
        answer_list.append(0)
    print(max(answer_list))
