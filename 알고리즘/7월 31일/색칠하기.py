import sys
sys.stdin = open("txt_folder/색칠하기_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())            # 칠 할 영역의 개수
    arr = [list(map(int,input().split())) for _ in range(N)]
    color_list = [[0] * 10 for _ in range(10)]
    cnt = 0

    # 빈 리스트에 빨강과 파랑을 누적해서 체크해주고
    for k in range(N):                          # 리스트를 한 줄씩 방문
        for i in range(arr[k][0],arr[k][2]+1):
            for j in range(arr[k][1],arr[k][3]+1):
                color_list[i][j] += arr[k][4]   # 색깔 누적 합

    # color_list[i][j]가 3이 된다면 그 칸은 보라색이 된 칸이다.
    for i in range (10):
        for j in range (10):
            if color_list[i][j] == 3:
                cnt+=1

    print(f"#{tc} {cnt}")
