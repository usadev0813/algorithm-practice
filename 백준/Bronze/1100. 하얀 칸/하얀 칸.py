result = 0
arr = []
for i in range(8):
    arr += [list(input())]

for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            if (i+j) % 2 == 0 and arr[i][j] == "F":
                result += 1
        else:
            if (i+j) % 2 == 0 and arr[i][j] == "F":
                result += 1
print(result)