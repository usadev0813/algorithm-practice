x, y = map(int, input().split())
x_list = []
y_list = []

for i in range(x * 2):
    temp = list(map(int, input().split()))
    if x > i:
        x_list.append(temp)
    else:
        y_list.append(temp)

for i in range(x):
    for j in range(y):
        temp_x = x_list[i][j]
        temp_y = y_list[i][j]
        print(temp_x + temp_y, end=" ")
    print()










