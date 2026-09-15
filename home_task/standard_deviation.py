import math

n = int(input("Enter the number of scores: "))

scores = list(map(int, input("Input Sample: ").split()))

print("Scores:")
for i in range(n):
    print(scores[i], end=" ")
    if (i + 1) % 4 == 0:
        print()

total = sum(scores)
average = total / n

print(f"\nAverage: {average:.2f}")

lowest = scores[0]

for score in scores:
    if score < lowest:
        lowest = score

print(f"Lowest Score: {lowest}")

highest = scores[0]

for score in scores:
    if score > highest:
        highest = score

print(f"Highest Score: {highest}")

print("\nScore  Deviation")

deviations = []

for score in scores:
    deviation = score - average
    deviations.append(deviation)
    print(f"{score:<6}{deviation:>7.2f}")

sum_squared_deviations = 0

for deviation in deviations:
    sum_squared_deviations += deviation ** 2

standard_deviation = math.sqrt(sum_squared_deviations / n)

print(f"\nStandard Deviation: {standard_deviation:.2f}")


count = 0

lower_limit = average - standard_deviation
upper_limit = average + standard_deviation

for score in scores:
    if lower_limit <= score <= upper_limit:
        count += 1

print(f"\nScores within one standard deviation: {count}")
