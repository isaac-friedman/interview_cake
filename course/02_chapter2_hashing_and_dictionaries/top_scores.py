from sortedcontainers import SortedList

def top_scores(scores):
    return SortedList(scores)



unsorted_scores = [37, 89, 41, 65, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100

print(top_scores(unsorted_scores))
