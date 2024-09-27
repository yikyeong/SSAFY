import sys
sys.stdin = open("txt_folder/view.txt","r")

for tc in range(1, 11):
    N = int(input())
    building = list(map(int, input().split()))
    add = 0  # 조망권 개수

    for i in range(2, N - 2):  # 앞, 뒤 2칸씩 건물이 없기 때문에 2부터 n-2까지
        height = building[i]  # 건물 하나를 기준으로 잡고
        for j in range(height, -1, -1):  # 윗 층부터 내려오면서 조망권이 몇 세대인지 파악
            if j > building[i - 1] and j > building[i - 2] and j > building[i + 1] and j > building[i + 2]:
                # 현재 세대를 옆 2칸씩 비교하면서 조망권이 확보되었는지 조건문을 통해 검사
                add += 1  # 조망권이 확보되었다면 add에 추가
            else:
                break  # 만약 건물 하나라도 지금 층보다 높으면 검사 x

    print(f"#{tc} {add}")