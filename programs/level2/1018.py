Height, Weight = list(map(int,input().split()))
chess_size = 8
chess_map = [input() for _ in range(Height)]
fix_values = []
fix_values_replace = []
for height in range(Height - chess_size + 1):
    for weight in range(Weight - chess_size + 1):
        first_value = chess_map[height][weight]
        count_fix = 0
        for i in range(height, height+8):
            for j in range(weight, weight+8):
                other_value = chess_map[i][j]
                if (i + j) % 2 == 0:
                    if first_value != other_value:
                        count_fix += 1
                else:
                    if first_value == other_value:
                        count_fix += 1
        fix_values.append(count_fix)
for val in fix_values:
    fix_values_replace.append(64 - val)

print(min(min(fix_values), min(fix_values_replace)))




