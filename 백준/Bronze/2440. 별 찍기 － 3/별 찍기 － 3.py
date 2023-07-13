a = int(input())
for i in range(a, 0, -1):
    temp = ""
    for j in range(i):
        temp = temp + '*'
    print(temp)
