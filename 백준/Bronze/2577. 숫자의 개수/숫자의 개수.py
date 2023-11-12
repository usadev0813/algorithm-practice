value = 1
for i in range(3):
    value *= int(input())

for j in range(0, 10):
    temp = 0
    for k in range(len(str(value))):
        if j == int(str(value)[k]):
            temp += 1
    print(temp)
