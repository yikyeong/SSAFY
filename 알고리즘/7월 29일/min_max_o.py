import sys
sys.stdin = open("txt_folder/min_max.txt","r")

T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    arr = list(map(int,input().split()))

    max_arr = arr[0]
    min_arr = arr[0]
    for i in arr :
        if i > max_arr:
            max_arr = i
        if i < min_arr :
            min_arr = i
    answer = max_arr - min_arr
    print(f"#{tc} {answer}")