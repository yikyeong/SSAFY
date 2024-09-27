import sys
sys.stdin = open("input_folder/스도쿠_input.txt","r")

def check_sudoku(sudoku):
    for i in range(9):
        check_list_i = [0] * 10
        check_list_j = [0] * 10
        for j in range(9):
            check_list_i[sudoku[i][j]] += 1
            check_list_j[sudoku[j][i]] += 1
        for k in range(1,10):
            if check_list_i[k] > 1 or check_list_j[k] > 1:
                return 0

    for q in range(0,9,3):
        for w in range(0,9,3):
            check_box = [0] * 10
            for r in range(3):
                for c in range(3):
                    check_box[sudoku[q+r][w+c]] += 1
        for k in range(10):
            if check_box[k] > 1:
                return 0
    return 1
T = int(input())
for tc in range(1,T+1):
    sudoku = [list(map(int,input().split())) for _ in range(9)]
    print(f"#{tc}",check_sudoku(sudoku))

