import sys
sys.stdin = open("색칠하기_input.txt","r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    blank_list = [[0]*10 for _ in range(10)]                            # 색을 칠할 10*10 2차원 배열 만들어주기
    paint_list = [list(map(int,input().split()))for _ in range(N)]

    # 빈 리스트에 빨강과 파랑을 누적해서 체크해주고
    for paint in paint_list:                                            # paint_list를 한 줄씩 방문
        for i in range(paint[0],paint[2]+1):
            for j in range(paint[1],paint[3]+1):
                if paint[4] == 1:                                       # paint[4]가 1이면 빨강
                    blank_list[i][j] += paint[4]
                else :                                                  # paint[4]가 2이면 파랑
                    blank_list[i][j] += paint[4]

    # blank_list[r][c]가 3이 된다면 그 칸은 보라색이 된 칸이다.
    purple = 0
    for r in range(10):
        for c in range(10):
            if blank_list[r][c] == 3:
                purple += 1

    print(f"#{tc} {purple}")