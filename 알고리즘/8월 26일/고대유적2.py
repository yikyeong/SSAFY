import sys
sys.stdin = open("고대유적2_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())            # N개의 줄에, M개씩 데이터 제공
    arr = [list(map(int,input().split()))for _ in range(N)]

    structure = 0
    for i in range(N):
        for j in range(M):
            r_long = 0  # 가로
            c_long = 0  # 세로
            if arr[i][j] == 1:
                for k in range(M):
                    if j+k < M:
                        if arr[i][j+k] == 1:        # 가로 길이
                            r_long += 1
                        else :
                            break
                for k in range(N):
                    if i+k < N:
                        if arr[i+k][j] == 1:        # 세로 길이
                            c_long += 1
                        else :
                            break
            if r_long > structure:
                structure = r_long
            if c_long > structure:
                structure = c_long
        if structure < 2:
            structure = 0

    print(f"#{tc} {structure}")