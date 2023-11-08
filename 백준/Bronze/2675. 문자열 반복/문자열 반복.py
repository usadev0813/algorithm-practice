count = int(input())

for j in range(count):
    number, value = input().split()
    result = ""
    for k in range(len(value)):
        result += value[k] * int(number)
    print(result)