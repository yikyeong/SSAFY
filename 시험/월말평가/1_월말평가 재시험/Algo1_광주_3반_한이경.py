T = int(input())
for tc in range(1,T+1):
    N = int(input())
    first_end = list(map(int, input().split()))
    land = [list(map(int, input().split()))for _ in range(N)]
    land_add = 0
    cnt = 0
    result_sum = 0

    # 평탄화 할 영역 구하기
    for i in range (first_end[0], first_end[2]+1):
        for j in range(first_end[1], first_end[3]+1):
            land_add += land[i][j]                  # 평탄화 할 영역의 높이 합
            cnt += 1                                # 평탄화 할 영역의 칸 수
    avg = land_add // cnt                           # 평균값

    # 평균값으로 평탄화 해주기
    for i in range (first_end[0], first_end[2]+1):
        for j in range(first_end[1], first_end[3]+1):
            if avg != land[i][j] :
                if avg > land[i][j] :               # 평균값이 영역의 높이보다 크다면
                    result_sum += avg - land[i][j]
                elif avg < land[i][j] :             # 영역의 높이가 평균값보다 크다면
                    result_sum += land[i][j] - avg

    print(f"#{tc} {result_sum}")