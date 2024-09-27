import sys
sys.stdin = open("txt_folder/이진탐색_input.txt","r")

def find_winner(end,P_):
    l = 1
    c = (l + end) // 2
    cnt = 0
    while c != P_:
        if P_ > c :
            l = c
        elif P_ < c:
            end = c
        else :
            break
        c = (l + end) // 2
        cnt+=1

    return cnt


T = int(input())
for tc in range(1,T+1):
    # P : 전체 쪽 수, Pa : A가 찾을 쪽 번호, Pb: B가 찾을 쪽 번호
    P, Pa, Pb = map(int,input().split())
    winner = ""
    A = find_winner(P,Pa)
    B = find_winner(P,Pb)

    if A > B:
        winner = "B"
    elif A < B:
        winner = "A"
    elif A == B:
        winner = "0"

    print(F"#{tc} {winner}")











    #
    # Al = 1
    # Bl = 1
    # Ar = P
    # Br = P
    # Ac = 0
    # Bc = 0
    # winner = "0"
    #
    # while True:
    #     Ac = (Al + Ar) // 2
    #     if Ac == Pa :
    #         winner = "A"
    #         break
    #     elif Ac <= Pa:
    #         Al = Ac
    #     else:
    #         break
    #
    #     Bc = (Bl + Br) // 2
    #     if Bc == Pb:
    #         winner = "B"
    #         break
    #     elif Bc <= Pb:
    #         Br = Bc
    #     else :
    #         break
    #
    # print(f"#{tc} {winner}")
