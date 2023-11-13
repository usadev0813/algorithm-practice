for _ in range(int(input())):
    h, w, n = map(int, input().split())

    floor = n % h #층
    room_line = (n // h) + 1 #라인

    if floor == 0:
        floor = h
        room_line -= 1
    print(floor * 100 + room_line)