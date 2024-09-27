import sys
sys.stdin = open("txt_folder/Ladder1_input.txt","r")

# for i in range(1,11):
#     tc = int(input())
#     ladder_list = [list(map(int, input().split())) for _ in range(100)]
#
#     for i in range(100):
#         if ladder_list[99][i] == 2:
#             nj = i                      # 출구의 열(시작하는 곳의 열)
#
#     ni = 99                         # 출구 행(시작하는 곳의 행)
#     while (ni > 0):                 # ni가 0이랑 같으면 한 번 더 돌아서 범위를 벗어나게 된다. -> 위에 줄까지 탐색하려함
#         if nj < 99 and ladder_list[ni][nj+1] == 1 :         # 현재 열이 99보다 작아야 우로 갈 수 있어서 99보다 작아야하고, 우로 한 칸 갔을 때 값이 1이라면
#             while nj < 99 and ladder_list[ni][nj+1] == 1 :  # 우로 갔을 때 1이 나올 때까지
#                 nj += 1                                     # 우로 한 칸 가라
#         elif nj > 0 and ladder_list[ni][nj-1] == 1:
#             while nj > 0 and ladder_list[ni][nj-1] == 1:
#                 nj -= 1
#         ni -= 1                                             # 두 조건 다 만족하지 못했을 땐 좌,우로 가는게 아닌 위로 올라가야 하므로 ni -1
#
#     print(f"#{tc} {nj}")