while(True):
    num = input()
    if num == '0': break
    num_len = len(num)
    target = num_len // 2
    next_target = num_len // 2

    if num_len % 2 != 0:
        next_target = next_target + 1

    if num[0:target] == num[next_target:num_len][::-1]:
        print("yes")
    else:
        print("no")

