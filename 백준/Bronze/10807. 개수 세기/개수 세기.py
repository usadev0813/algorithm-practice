n = int(input())
value = list(map(int, input().split()))
target = int(input())

count = 0

for i in range(n):
    if value[i] == target:
        count += 1
print(count)