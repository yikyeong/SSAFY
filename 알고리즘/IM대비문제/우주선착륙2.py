dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    stop = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N):
        for j in range(M):
            cnt = 0
            for d in range(8):
                r = i + dr[d]
                c = j + dc[d]
                if r >= 0 and c >= 0 and r < N and c < M:
                    if stop[i][j] > stop[r][c]:
                        cnt += 1
            if cnt >= 4:
                result += 1

    print(f"#{tc} {result}")