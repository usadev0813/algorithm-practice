n = int(input())
scores = list(map(int, input().split()))
max_num = max(scores)

alpha = max_num * 100

sum = 0
for i in range(n):
    sum += scores[i] / max_num * 100
print(sum / n)

