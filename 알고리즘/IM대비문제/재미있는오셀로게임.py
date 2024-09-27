import sys
sys.stdin = open("input_folder/재미있는오셀로게임_input.txt","r")

dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())      # N: 보드 한 변의 길이, M: 돌을 놓는 횟수
    arr = [list(map(int, input().split())) for _ in range(M)]   # 1: 흑돌(B), 2: 백돌(W)   
    empty_list = [[0]*N for _ in range(N)] 
    n=N//2
    empty_list[n-1][n-1],empty_list[n][n] = 2, 2
    empty_list[n][n-1],empty_list[n-1][n] = 1, 1 
    
    for i in range(len(arr)):
        empty_list[arr[i][1]-1][arr[i][0]-1] = arr[i][2]
        for d in range(8):
            nr = (arr[i][1]-1)+dr[d]
            nc = (arr[i][0]-1)+dc[d]
            if 0 <= nr < N and 0 <= nc < N and empty_list[nr][nc]!=0:
                while empty_list[arr[i][1]-1][arr[i][0]-1] != empty_list[nr][nc]:
                    find_nr = 0
                    find_nc = 0
                    if empty_list[arr[i][1]-1][arr[i][0]-1] != empty_list[nr][nc]:
                                find_nr = nr
                                find_nc = nc
                                nr += dr[d]
                                nc += dc[d]
                    else:
                        break
            print(find_nc)
            