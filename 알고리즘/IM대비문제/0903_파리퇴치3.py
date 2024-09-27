import sys

sys.stdin = open("input_folder/파리퇴치3_input.txt", "r")

#     상  우 하  좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
#      상우 하우 하좌 상좌
dx = [-1, 1, 1, -1]
dy = [1, 1, -1, -1]
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N : 배열의 크기, M : 기준을 포함한 세기
    fly_list = [list(map(int, input().split())) for _ in range(N)]
    max_fly = 0

    for i in range(N):
        for j in range(N):
            sum_fly = 0
            sum_fly += fly_list[i][j]
            for k in range(1,M):
                for d in range(4):
                    r = i+(k*dr[d])
                    c = j+(k*dc[d])
                    if 0<=r<N and 0<=c<N :
                        sum_fly += fly_list[r][c]
            if sum_fly > max_fly :
                max_fly = sum_fly
            
            sum_fly_dia = 0
            sum_fly_dia += fly_list[i][j]
            for k in range(1,M):
                for d in range(4):
                    x = i+(k*dx[d])
                    y = j+(k*dy[d])
                    if 0<=x<N and 0<=y<N :
                        sum_fly_dia += fly_list[x][y]
            if sum_fly_dia > max_fly :
                max_fly = sum_fly_dia
                
    print(f"#{tc} {max_fly}")