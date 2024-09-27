import sys
sys.stdin = open("txt_folder/특별한정렬_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    number = list(map(int,input().split()))
    sort_number = sorted(number)
    empty_list = [0]*10

    odd = 1
    for i in range(0,5):
        empty_list[odd] = sort_number[i]
        odd+=2
    even = 0
    for j in range(-1,-6,-1):
        empty_list[even] = sort_number[j]
        even+=2

    print(f"#{tc}",end=" ")
    print(*empty_list[0:10])