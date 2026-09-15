n = int(input())
c = int(input())

scores = list(map(int, input().split()))

count = 0

for i in range(n):
    if scores[i] >= c:
        count = count + 1

print(count)