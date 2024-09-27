import sys
sys.stdin = open("스위치_조작_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())                        # N : 스위치 개수
    A = list(map(int, input().split()))     # A : 조작 전 상태
    B = list(map(int, input().split()))     # B : 조작 후 상태
    cnt = 0
    while A != B:
        for i in range(N):
            if A[i] != B[i]:
                cnt += 1
                for j in range(i,N):
                    if B[j] == 0:
                        B[j] = 1
                    elif B[j] == 1:
                        B[j] = 0
    print(f"#{tc} {cnt}")
