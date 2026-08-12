import math

t = int(input())
for _ in range(t):
    x = int(input())
    # Find the minimum number of correct answers needed using ceil
    correct_count = math.ceil(x / 3)
    # The difference between the points from these correct answers and x gives the incorrect answers
    incorrect_count = (correct_count * 3) - x
    print(incorrect_count)