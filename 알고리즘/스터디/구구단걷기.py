import sys
sys.stdin = open("구구단걷기_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    min_gugudan = []
    num = 0
    for i in range(1,(N//2)+1):
        if N % i == 0:
            num = N//i
            min_gugudan.append([i,num])
    print(min_gugudan)
    
    
    # print(f"#{tc} {ans}")