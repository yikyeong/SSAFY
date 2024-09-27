import sys
sys.stdin = open("txt_folder/부분집합의_합_input.txt","r")

T = int(input())
for tc in range(1, T + 1):
    A = list(range(1, 13))
    N, K = map(int, input().split())      # N: 부분집합 원소의 수, K: 부분집합의 합
    result = 0
    for i in range(1<<12):                # 부분 집합의 경우의 수(2^12)
        count = 0
        add = 0
        for j in range(12):               # 12개의 원소를 하나씩 확인
            if i & (1<<j) :               # i의 j번째 비트가 1이면 해당 원소가 부분집합에 포함됨
                count += 1
                add += A[j]
        # 모든 반복문을 완료한 후 부분집합의 갯수와 합이 입력값과 같다면 결과에 추가
        if count == N and add == K:
                result += 1
    print(f"#{tc} {result}")
            
