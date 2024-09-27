import sys
sys.stdin = open("input_folder/스도쿠_input.txt","r")

def check_sudoku():
    for i in range(9):
        check_r = [0] * 10                          # 가로 확인 빈 배열
        check_c = [0] * 10                          # 세로 확인 빈 배열
        for j in range(9):
            check_r[sudoku[i][j]] += 1              # 스도쿠에 있는 숫자를 인덱스 번호에 넣어 몇 개 있는지 확인
            check_c[sudoku[j][i]] += 1
        for t in range(1,10):                       # 가로, 세로 배열을 확인
            if check_r[t] == 0 or check_r[t] > 1:   # 1~9 인덱스에 1씩 들어있어야 한다.
                return 0                            # 0개 또는 1개가 넘으면 잘못된 스도쿠 이므로 0을 return
            if check_c[t] == 0 or check_r[t] > 1:
                return 0

    # 작은 사각형 9칸을 확인
    for x in range(0,9,3):                          # sudoku 가로
        for y in range(0,9,3):                      # sudoku 세로
            check_9 = [0] * 10                      # y 범위가 바뀌면 그 옆 9칸 탐색
            for i in range(3):                      # 작은 사각형 가로
                for j in range(3):                  # 작은 사각형 세로
                    check_9[sudoku[x+i][y+j]] += 1
                    if check_9[sudoku[x+i][y+j]] > 1:
                        return 0
    return 1                                        # return 0을 만나지 않았다면 다 true이므로 1을 return

T = int(input())
for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    print(f"#{tc} {check_sudoku()}")