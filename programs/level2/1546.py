test_num = int(input())
test_score = list(map(int, input().split()))
max_score = max(test_score)
new_score = []
for score in test_score:
    temp_score = (score/max_score) * 100
    new_score.append(temp_score)
print(sum(new_score)/test_num)