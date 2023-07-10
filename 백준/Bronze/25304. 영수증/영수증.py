total = int(input())
sum = 0;

for _ in range(int(input())):
    x, y = map(int, input().split())
    sum += x * y

print("Yes") if total == sum else print("No")