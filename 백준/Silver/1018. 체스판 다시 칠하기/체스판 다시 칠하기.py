N, M = map(int, input().split())
board = list()
for i in range(N):
    board.append(input())
repair = list()

# 체스판 시작 범위 설정
# 만약 가로로 브루트 포스할 때 N이 10일때 10-7하면 3이다. 고로 8x8 체스가 가로로 3번만 움직이게끔 하기 위함
for i in range(N-7):
    # 마찬가지로 세로로 브루트 포스할 때 시작 범위 설정
    for j in range(M-7):
        first_W = 0
        first_B = 0
        # 8x8범위의 체스판으로 검증을 시작한다 검증할 것은 화이트로 체스판이 시작할때 or 블랙으로 시작할때의
        # 해당하는 칸이 옳은 색상의 칸인지를 판별하면된다. 만약 화이트로 체스판이 시작된다면 짝수칸이 모두 화이트여야 한다.
        # 그렇지 않다면 해당하는 칸은 잘못된 칸이기 때문에 first_w를 +1 시킨다 블랙일때도 마찬가지
        for k in range(i,i+8):
            for l in range(j,j + 8):
                # 체스 시작이 화이트일때와 블랙일때 모두 구한다 만약 화이트로 시작을 한다고 쳤을때 짝수는 모두 화이트여야한다.
                # 그런데 만약 화이트(W)가 아니라면 그 칸은 잘못된 색상이기에 first_W +1 시킨다
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        first_W = first_W + 1
                    if board[k][l] != 'B':
                        first_B = first_B + 1
                # 체스 시작이 화이트일때 홀수칸은 블랙이여야만 한다 근데 B가 아니라면 잘못된 칸이므로 first_W +1 시킨다
                else:
                    if board[k][l] != 'B':
                        first_W = first_W + 1
                    if board[k][l] != 'W':
                        first_B = first_B + 1
        repair.append(min(first_W, first_B))
print(min(repair))