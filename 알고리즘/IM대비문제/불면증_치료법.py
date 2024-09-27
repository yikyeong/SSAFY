import sys
sys.stdin = open("input_folder/불면증_치료법_input.txt","r")
# T = int(input())
# for tc in range (1,T+1):
#     N = int(input())
#     s=set()
#     while len(s) < 10 :
#         for

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    m = N
    s = set()
    while len(s) < 10:
        for i in str(N):
            s.add(i)
        N += m
    print(f"#{tc} {N - m}")