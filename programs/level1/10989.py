import string
input_word = input()
lowercase_letters = string.ascii_lowercase

alphabet_dict = {}

for letters in lowercase_letters:
    alphabet_dict[letters] = input_word.find(letters)

print(*alphabet_dict.values())