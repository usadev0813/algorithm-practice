result = []
for i in range(10):
    result.append(int(input()) % 42)
set_list = set(result)
print(len(set_list))