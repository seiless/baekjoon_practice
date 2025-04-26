from itertools import combinations

cards_num, max_score = map(int, input().split())
cards = list(map(int, input().split()))

combi_results = combinations(cards,3)
result = [sum(pair) for pair in combi_results]

if max_score in result:
    print(max_score)
else:
    temp_result = [x for x in result if x <= max_score]
    if temp_result:
        print(max(temp_result))