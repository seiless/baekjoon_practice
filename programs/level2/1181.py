word_num = int(input())
word_list = list(set([input() for _ in range(word_num)]))
word_list.sort(key=lambda x: (len(x), x))
print('\n'.join(map(str, word_list)))