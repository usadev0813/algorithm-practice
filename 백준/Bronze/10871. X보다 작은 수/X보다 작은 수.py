n, value = map(int, input().split())
temp_list = list(map(int, input().split()))
result = []
for i in range(n):
    if temp_list[i] < value:
        result.append(temp_list[i])

print(*result)