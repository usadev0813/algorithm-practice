n = int(input())
num_list = list(map(int, input().split()))

result = 0
for num in num_list:
    flag = 1
    if num > 1:
        for i in range(2, num):
            if num % i == 0: flag = 0
        if flag == 1: result +=1
print(result)