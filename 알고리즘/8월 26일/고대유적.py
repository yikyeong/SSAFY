import sys
sys.stdin = open("고대유적_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split()))for _ in range(N)]

    max_len = 0
    for i in range(N):
        r_cnt = 0
        for j in range(M):
            if arr[i][j]==1:
                r_cnt += 1
                if r_cnt > max_len:
                    max_len = r_cnt
            else :
                r_cnt = 0

    for i in range(M):
        c_cnt = 0
        for j in range(N):
            if arr[j][i]==1:
                c_cnt += 1
                if c_cnt > max_len:
                    max_len = c_cnt
            else :
                c_cnt = 0
    if max_len < 2:
        max_len = 0

    print(f"#{tc} {max_len}")