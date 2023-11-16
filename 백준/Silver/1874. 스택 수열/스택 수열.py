n = int(input())
orig_list = [int(input()) for i in range(n)]

sort_list = sorted(orig_list)
stack = []
pop_list = []
push_pop_history = []
count = 0
total_count = 0

while True:
    if total_count == len(sort_list) * 2:
        for pust_pop in push_pop_history:
            print(pust_pop)
        break

    if len(stack) == 0:
        stack.append(sort_list[count])
        push_pop_history.append("+")
        total_count += 1
        count += 1
    else:
        if orig_list[0] == stack[-1]:
            pop_list.append(stack.pop())
            push_pop_history.append("-")
            orig_list.remove(orig_list[0])
            total_count += 1
        else:
            if count == len(sort_list):
                print("NO")
                break
            stack.append(sort_list[count])
            push_pop_history.append("+")
            total_count += 1
            count += 1



