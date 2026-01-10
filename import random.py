import random
test_scores = [random.randint(50, 100) for _ in range(1000)]
total_score = sum(test_scores)
number_of_scores = len(test_scores)
average_score = total_score / number_of_scores
print(f"Total number of scores: {number_of_scores}")
print(f"Sum of all scores: {total_score}")
print(f"The calculated average score is: {average_score}")
