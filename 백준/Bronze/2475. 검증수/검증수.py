def func(list):
    result = 0
    for _ in range(len(list)):
        result += list[_] * list[_]
    return result % 10


nums = list(map(int, input().split()))

print(func(nums))
