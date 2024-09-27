'''
3
3
1 1 2
1
1
5
3 1 2 1 2
'''
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0

    for i in range(N):
        result ^= arr[i]
    print(f"#{tc} {result}")