N = int(input())

result = 0
fac_result = 1
for i in range(1, N + 1):
    fac_result *= i # N팩토리얼 값을 구한다

reverse_str_fac_result = list(str(fac_result)) # N팩토리얼 값을 문자열 리스트로 변환한다.

for str_fac_num in reversed(reverse_str_fac_result):
    if str_fac_num == '0': result += 1
    else: break

print(result)