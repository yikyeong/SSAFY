import sys
sys.stdin = open("input_folder/의석이의세로로말해요_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    str_list = [list(input())for _ in range(5)]

    m=0
    for i in range(5):
        if m < len(str_list[i]):
            m = len(str_list[i])

    new_list = [["."]*m for _ in range(5)]
    for i in range(5):
        for j in range(len(str_list[i])):
            new_list[i][j] = str_list[i][j]

    ans = ""
    for i in range(m):
        for j in range(5):
            if new_list[j][i] != ".":
                ans += new_list[j][i]

    print(f"#{tc} {ans}")
