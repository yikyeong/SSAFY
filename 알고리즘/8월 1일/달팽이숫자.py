import sys

sys.stdin = open("txt_folder/달팽이숫자_input.txt", "r")

T = int(input())
# 우 하 좌 상
dr = [0, 1, 0, -1]      # 행
dc = [1, 0, -1, 0]      # 열
for tc in range(1, T + 1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    d = 0               # 델타 인덱스
    r, c = 0, 0         # 현재 행, 현재 열
    for i in range(1, N * N + 1):
        snail[r][c] = i
        # 맨 처음엔 우로 이동하는 델타 방향
        # 아래 조건에 성립하지 않는다면 델타 한 칸 이동
        # r + dr[d] -> 다음 행, c + dc[d] -> 다음 열
        # 다음 열 or 행이 범위에서 벗어난다면 or 이미 숫자가 채워져있다면
        if r + dr[d] >= N or r + dr[d] < 0 or c + dc[d] >= N or c + dc[d] < 0 or snail[r + dr[d]][c + dc[d]] != 0:
            d += 1                          # 델타 인덱스 이동
        d %= 4                              # 델타 인덱스 범위가 벗어날 경우를 생각해서 %4
        r,c = r + dr[d], c + dc[d]          # 현재 r,c를 델타 탐색한 값으로 초기화
    print(f"#{tc}")
    for i in snail:
        print(*i)
