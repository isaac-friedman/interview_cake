def top_scores(unsorted_scores):
    HIGHEST_POSSIBLE_SCORE = 100
    score_counts = [0] * (HIGHEST_POSSIBLE_SCORE + 1)

    for score in unsorted_scores:
        score_counts[score] += 1
    sorted_scores = []

    for score in range(len(score_counts)):
        # If the score is unique just append it once
        if score_counts[score] == 1:
            sorted_scores.append(score)
        # Otherwise append it COUNT times
        elif score_counts[score] > 1:
            [sorted_scores.append(score) for i in range(score_counts[score])]
        # Pass if count is 0
        else:
            pass
    return sorted_scores

unsorted_scores = [37, 89, 41, 65, 91, 53]


print(top_scores(unsorted_scores))
