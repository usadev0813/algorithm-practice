N = int(input())

result = 0
fac_result = 1
for i in range(1, N + 1):
    fac_result *= i # N팩토리얼 값을 구한다

for str_fac_num in reversed(str(fac_result)):
    if str_fac_num == '0': result += 1
    else: break

print(result)