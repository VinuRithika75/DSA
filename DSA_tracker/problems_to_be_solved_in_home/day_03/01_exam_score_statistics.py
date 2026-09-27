
import math

n = int(input())

scores = list(map(float, input().split()))


print("Scores:")

for i in range(n):
    print(int(scores[i]) if scores[i].is_integer() else scores[i], end=" ")

    if (i + 1) % 4 == 0:
        print()


total = 0

for i in range(n):
    total = total + scores[i]

average = total / n

lowest = scores[0]

for i in range(1, n):
    if scores[i] < lowest:
        lowest = scores[i]


highest = scores[0]

for i in range(1, n):
    if scores[i] > highest:
        highest = scores[i]

print()
print("Average: %.2f" % average)
print("Lowest Score:", int(lowest) if lowest.is_integer() else lowest)
print("Highest Score:", int(highest) if highest.is_integer() else highest)


print()
print("Score  Deviation")

for i in range(n):
    deviation = scores[i] - average
    print("%g     %.2f" % (scores[i], deviation))


sum_squared_deviation = 0

for i in range(n):
    deviation = scores[i] - average
    sum_squared_deviation = sum_squared_deviation + deviation * deviation

standard_deviation = math.sqrt(sum_squared_deviation / n)

print()
print("Standard Deviation: %.2f" % standard_deviation)

count = 0

lower_limit = average - standard_deviation
upper_limit = average + standard_deviation

for i in range(n):
    if lower_limit <= scores[i] <= upper_limit:
        count = count + 1

print("Scores within one standard deviation:", count)