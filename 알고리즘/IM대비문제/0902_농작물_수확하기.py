import sys
sys.stdin = open("input_folder/농작물수확_input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())        # N : 농장의 크기
    farm = [list(map(int, input())) for _ in range(N)]
    d = N//2
    sum_farming = 0
    k=0

    for i in range(N):
        for j in range(d-k,(d+k)+1):
            sum_farming += farm[i][j]
        if i < d:
            k += 1
        if i >= d:
            k -= 1
    print(f"#{tc} {sum_farming}")



