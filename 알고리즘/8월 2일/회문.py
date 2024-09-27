import sys
sys.stdin = open("회문_input.txt","r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())     # N: 글자판의 크기, M: 회문의 길이
    str_list = [input() for _ in range(N)]
    answer = ""

    # 가로 회문 확인
    for i in range(N):
        for j in range(N-M+1):
            for t in range(M//2):
                if str_list[i][j+t] != str_list[i][j+M-1-t]:
                    break 
            else :
                answer = "".join(str_list[i][j:j+M])

                # if str_list[j+t][i] != str_list[(j+M-1)-t][i]:
                #     break
                # else:
                #     answer = "".join(str_list[j:j+M][i])
    print(f"#{tc} {answer}")


    
        