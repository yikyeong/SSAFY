import sys
sys.stdin = open("txt_folder/Sum_input.txt","r")

for tc in range(1,11):
    tc_in = int(input())
    num_list = [list(map(int,input().split()))for _ in range(100)]
    max_sum = 0

    left_dia_sum = 0
    right_dia_sum = 0
    for i in range(100):
        r_sum = 0                       # 가로 합
        c_sum = 0                       # 세로 합
        for j in range(100):
            r_sum += num_list[i][j]     # 가로 합의 최댓값
            if r_sum > max_sum:
                max_sum = r_sum

            c_sum += num_list[j][i]     # 세로 합의 최댓값
            if c_sum > max_sum:
                max_sum = c_sum

            if i == j:                  # 왼쪽 대각선의 최댓값
                left_dia_sum += num_list[i][j]

            if 99 - i == j :            # 오른쪽 대각선의 최댓값
                right_dia_sum += num_list[i][j]

    if left_dia_sum > max_sum:
        max_sum = left_dia_sum

    if right_dia_sum > max_sum:
        max_sum = right_dia_sum

    print(f"#{tc_in} {max_sum}")
