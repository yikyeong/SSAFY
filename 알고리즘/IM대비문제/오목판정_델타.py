import sys
sys.stdin = open("input_folder/오목판정_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    o_mok = [list(input()) for _ in range (N)]

    dr = [0,1,1,1]
    dc = [1,1,0,-1]
    answer = "NO"

    for i in range(N):
        for j in range(N):
            if o_mok[i][j]=="o":
                for d in range(4):
                    cnt = 0
                    for k in range(5):
                        ni = i + (dr[d]*k)
                        nj = j + (dc[d]*k)
                        if ni >= 0 and ni < N and nj >= 0 and nj < N and o_mok[ni][nj]=="o":
                            cnt+=1
                            if cnt == 5:
                                answer = "YES"
    print(f"#{tc} {answer}")




