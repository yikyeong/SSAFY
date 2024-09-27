import sys
sys.stdin = open("txt_folder/전기버스_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    # K: 한 번 충전으로 최대 이동할 수 있는 정류장 수, N: N번째 정류장까지 존재, M: 충전기 가 설치된 정류장 수
    K, N, M = map(int,input().split())
    charge_stop_list = list(map(int,input().split()))
    bus_stop = [0] * (N + 1)
    now = K
    last_stop =0                                    # 이전 충전 위치
    cnt = 0
    for i in range(M):
        bus_stop[charge_stop_list[i]] = 1           # 충전소가 있는 위치를 체크

    while now < N:                                  # N값에 도착하기 위해선 최소 N-1에만 도달하면 되니까
        if bus_stop[now] == 1:                      # 정류소가 있다면
            last_stop = now                         # 이전 위치를 현재 위치로 저장
            now += K                                # 현재 위치에서 최대로 갈 수 있는 위치 누적 합해서 저장
            cnt+=1                                  # 충전 횟수 추가
        elif bus_stop[now] == 0:                    # 현재 위치에 충전소가 없으면
            now -= 1                                # 현재 위치에서 앞으로 1칸씩
            if now == last_stop:                    # 그 전 도착 지점까지 되돌아간다면
                cnt = 0                             # 완주 할 수 없으므로 cnt를 0으로 초기화하고
                break                               # 빠져나간다.
    print(f"#{tc} {cnt}")








