import sys

sys.stdin = open("txt_folder/연속한1의개수_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input()))
    max_len = 0
    cnt = 0
    for i in range(N):
        if num_list[i] == 1:
            cnt += 1
            if cnt > max_len:
                max_len = cnt
        else :
            cnt = 0
    print(f"#{tc} {max_len}")