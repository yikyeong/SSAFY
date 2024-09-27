import sys
sys.stdin = open("input_folder/오목판정_input.txt","r")

def verdict (o_mok,N):

    for i in range(N):
        r_cnt = 0
        c_cnt = 0
        for j in range(N):                  # 가로
            if o_mok[i][j] == "o":
                r_cnt += 1
            else :
                r_cnt = 0
            if o_mok[j][i] == "o":          # 세로
                c_cnt += 1
            else:
                c_cnt = 0
            # if i == j :                     # 왼 -> 오 대각선
            #     if o_mok[i][j] == "o":
            #         dl_cnt += 1
            #     else:
            #         dl_cnt = 0
            if r_cnt == 5 or c_cnt == 5 :
                return "YES"
    for i in range(N):
        for j in range(N):
            dr_cnt = 0
            dl_cnt = 0
            if o_mok[i][j] == "o":          # 오 -> 왼 대각선
                for r in range(5):
                    if i+r >= 0 and i+r < N and j-r >= 0 and j-r < N :
                        if o_mok[i + r][j - r] == "o":
                            dr_cnt += 1
                        else:
                            dr_cnt = 0
                    if i + r >= 0 and i + r < N and j + r >= 0 and j + r < N:
                        if o_mok[i+r][j+r] == "o" :
                            dl_cnt += 1
                        else:
                            dl_cnt = 0
            if dr_cnt == 5 or dl_cnt == 5:
                return "YES"
    return "NO"

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    o_mok = [list(input())for _ in range(N)]
    print(f"#{tc}",verdict(o_mok,N))
