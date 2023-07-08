a, b = map(int, input().split())
x = 0
y = 0
target = 45

# 일어난 분이 45분보다 작으면 45분과 일어난분을 뺀 값을 다시 60에서 뺀다
if target > b:
    temp = target - b
    y = 60 - temp
    # 그리고 일어난 시를 -1 뺀다 만약 0시라면 23시로 한다.
    if a == 0:
        x = 23
    else:
        x = a - 1
# 일어난 분이 45분보다 안작으면 그냥 분에서 뺀다.
else:
    y = b - 45
    x = a    
    
print(x, y)


