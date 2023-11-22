n = int(input())
human_info = []

for i in range(n):
    weight, height = map(int, input().split())
    human_info.append((weight, height))

for i in human_info:
    rank = 1
    for j in human_info:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")


