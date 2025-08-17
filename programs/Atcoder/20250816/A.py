char = input()

answer_dict = {"red": "SSS", "blue": "FFF", "green": "MMM"}

if char in answer_dict.keys():
    print(answer_dict[char])
else:
    print("Unknown")
