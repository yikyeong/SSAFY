import sys
sys.stdin = open("txt_folder/Flatten_input.txt","r")

for tc in range(1,11):
    N = int(input())
    box = list(map(int,input().split()))

    for i in range(N):                      # 덤프 횟수 만큼
        max_height = box[0]
        low_height = box[0]
        max_index = 0
        low_index = 0
        for i in range(100) :
            if max_height < box[i]:
                max_height = box[i]
                max_index = i               # 최고 높이의 인덱스 찾기
            if low_height > box[i]:
                low_height = box[i]
                low_index = i               # 최저 높이의 인덱스 찾기
        box[max_index] -= 1                 # 최고 높이의 상자에서 -1
        box[low_index] += 1                 # 최저 높이의 상자에서 +1 를 N번 만큼 반복

    # 최종적인 최고, 최저 높이의 상자의 차 구하기기
    max_box = box[0]
    min_box = box[0]
    for i in range(100):
        if max_box < box[i]:
            max_box = box[i]
        if min_box > box[i]:
            min_box = box[i]
    result = max_box - min_box

    print(f"#{tc} {result}")










