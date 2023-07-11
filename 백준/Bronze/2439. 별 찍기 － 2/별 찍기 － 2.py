a = int(input())

for i in range(1, a + 1):
    temp = ""
    for j in range(i):
        temp = temp + "*"
    print(f'{temp:>{a}}')