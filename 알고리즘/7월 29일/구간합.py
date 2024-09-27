import sys
sys.stdin = open("txt_folder/구간합_input.txt","r")

T = int(input())
for tc in range(1, T+1) :
    N, M = map(int, input().split()) # N: 정수의 개수, M: 구간의 개수
    arr = list(map(int, input().split()))

    max_arr = 0                     # 최대값 설정은 가장 작은 수로
    min_arr = 10000*M               # 최소값 설정은 가장 큰 수로
    # max_arr, min_arr을 배열의 0번째 인덱스 값으로 넣어주어도 된다.
    for i in range(0,N-M+1) :       # 끝까지 for문을 도는 것이 아닌 구간의 개수에서 1 빼주기
        # 규칙을 잘 모르겠을 땐 직접 그려보고 다양한 케이스로 접근해서 찾아보기
        sum_arr = 0
        for j in range(0, M):
            sum_arr += arr[i+j]
        if sum_arr > max_arr :      # if를 따로주는 이유 : 값이 중복이 될 수도 있다.
            max_arr = sum_arr       # -> 중복되어도 괜찮다. 왜냐하면 최종적으로는 값이 달라질 것이기 때문
        if sum_arr < min_arr :
            min_arr = sum_arr
    answer = max_arr - min_arr

    print(f"#{tc} {answer}")