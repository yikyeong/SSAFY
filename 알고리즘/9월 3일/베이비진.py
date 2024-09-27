import sys
sys.stdin = open("베이비진_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    babygin = list(map(int,input().split()))
    
    p1_card = [0]*10    # babygin에 담긴 카드를 p1_card 인덱스 번호에 담아주기 위해 리스트 초기화 해준다. 
    p2_card = [0]*10    # babygin에 담긴 카드를 p2_card 인덱스 번호에 담아주기 위해 리스트 초기화 해준다. 
    winner = 0
    
    for i in range(len(babygin)):
        if i%2 == 0:                    # 홀수 번째는 p1_card에 담는다. 
            p1_card[babygin[i]] += 1    # babygin i번째 수를 p1_card 인덱스에 담아준다.
        else :                          # 짝수 번째는 p2_card에 담는다. 
            p2_card[babygin[i]] += 1    # babygin i번째 수를 p2_card 인덱스에 담아준다.
            
        if 3 in p1_card :               # p1_card가 3이면 triplet
            winner = 1
            break
        if 3 in p2_card :
            winner = 2
            break
        
        for t in range(0, 8):           # 연속된 3장의 카드가 1보다 크면 run
            if p1_card[t] >=1 and p1_card[t+1] >= 1 and p1_card[t+2] >= 1:      # 따단
                winner = 1
                break
            if p2_card[t] >=1 and p2_card[t+1] >= 1 and p2_card[t+2] >= 1:
                winner = 2
                break
        
        if winner:                      # 여기서 브레이크를 걸어주지 않으면 따단 줄에서 winner가 1이라고 되고  
            break                       # break 때문에 빠져나가서 그 다음 if문으로 들어간다. 그리고 다시 for문을 돌다가
    print(f"#{tc} {winner}")            # winner가 2인 조건을 성립하면 winner는 2로 바뀌기 때문에 이 곳에서 winner가 있다면
                                        # break를 만나서 전체 for문을 빠져나간다. 