import sys
sys.stdin = open("input_folder/돌뒤집기_input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())                 # N: 첫 줄에 돌의 수, M: 뒤집기 횟수
    first_stone = list(map(int,input().split()))    # N개 돌의 초기상태
    for m in range(M):
        i, j = map(int, input().split())            # i번째 돌, 마주보는 j개의 돌 뒤집기
        position = i-1
        for k in range(1,j+1):
            if position-k >= 0 and position+k <= N-1:
                if first_stone[position-k] == first_stone[position+k]:
                    if first_stone[position-k] == 0:
                        first_stone[position - k] = first_stone[position + k] = 1
                    elif first_stone[position-k] == 1:
                        first_stone[position - k] = first_stone[position + k] = 0
    print(f"#{tc}",*first_stone)