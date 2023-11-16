import sys

n = int(input())

numbers = [0] * 10001

for i in range(n):
    input_num = int(sys.stdin.readline().strip())
    numbers[input_num] = numbers[input_num] + 1

for i in range(10001):
    if numbers[i] != 0:
        for j in range(numbers[i]):
            sys.stdout.write(str(i) + '\n')