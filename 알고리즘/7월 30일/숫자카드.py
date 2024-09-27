import sys
sys.stdin = open("txt_folder/숫자카드_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())                # 카드 장 수
    card = list(map(int,input()))
    cnt_card = [0]*10               # 카드의 갯수를 셀 빈 배열

    for i in range(N):
        cnt_card[card[i]] +=1       # 카드 갯수 세기

    max = 0                         # 최대 카드 몇 장?
    idx = 0                         # 최대 갯수의 카드를 저장한 카드 번호
    for j in range(len(cnt_card)):
        if cnt_card[j] >= max :     # 갯수가 다 같으면 가장 큰 수의 카드를 출력해야 하기 때문에
            max = cnt_card[j]
            idx = j
    print(f"#{tc} {idx} {max}")

