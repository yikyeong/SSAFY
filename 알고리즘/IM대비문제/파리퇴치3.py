import sys
sys.stdin = open("input_folder/파리퇴치3_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())             # N: N크기의 배열 M: 중심 칸부터 M칸
    fly = [list(map(int,input().split())) for _ in range (N)]

    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    dx = [-1,1,1,-1]
    dy = [1,1,-1,-1]
    max_sum = 0

    for i in range(N):
        for j in range(N):
            rc_sum = 0
            dia_sum = 0
            rc_sum += fly[i][j]
            dia_sum += fly[i][j]
            for k in range(1,M):
                for d in range(4):
                    ni = i+(dr[d]*k)
                    nj = j+(dc[d]*k)
                    if ni >= 0 and ni < N and nj >= 0 and nj < N:
                        rc_sum += fly[ni][nj]
                    di = i + (dx[d] * k)
                    dj = j + (dy[d] * k)
                    if di >= 0 and di < N and dj >= 0 and dj < N:
                        dia_sum += fly[di][dj]
            if rc_sum > max_sum:
                max_sum = rc_sum
            if dia_sum > max_sum:
                max_sum = dia_sum
    print(f"#{tc} {max_sum}")
