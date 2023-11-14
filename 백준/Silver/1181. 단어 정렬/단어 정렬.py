n = int(input())
word_list = [input() for i in range(n)]

set_word_list = list(set(word_list))
set_word_list.sort(key=lambda x: (len(x), x))

for word in set_word_list:
    print(word)
