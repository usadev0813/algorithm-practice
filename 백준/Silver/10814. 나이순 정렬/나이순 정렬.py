a = int(input())

member_list = []

for _ in range(a):
    age, name = input().split()
    member_list.append([int(age), name])

for i in sorted(member_list, key=lambda x: x[0]):
    print(i[0], i[1])
