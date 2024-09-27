T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]        # 비교할 배열
    pattern = [list(map(int,input().split())) for _ in range(3)]    # 패턴 배열
    cnt = 0
    for i in range(N-2):
        for j in range(N-2):
            which_one = [[0]*3 for _ in range(3)]                   # 3칸씩 잘라서 비교할 수 있는 빈 배열 만들기
            for x in range(3):
                for y in range(3):
                    which_one[x][y] = arr[i+x][j+y]                 # 빈 배열에 arr의 값 담기
            if which_one == pattern :                               # 3칸씩 자른 배열과 패턴 배열이 같으면 +1
                cnt += 1
    print(f"#{tc} {cnt}")