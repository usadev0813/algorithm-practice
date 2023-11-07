a, b = map(int, input().split())
result = 0

str_a = list(str(a))
str_b = list(str(b))

for i in range(len(str_a)):
    for j in range(len(str_b)):
        result += int(str_a[i]) * int(str_b[j])

print(result)

