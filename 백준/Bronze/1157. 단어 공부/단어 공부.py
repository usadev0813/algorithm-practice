value = input().lower()

set_list = set(value)
dic = {}

for i in range(len(set_list)):
    t = set_list.pop()
    dic[t] = value.count(t)

duplica_word = [k for k,v in dic.items() if max(dic.values()) == v]
if len(duplica_word) > 1:
    print("?")
else:
    print(duplica_word[0].upper())