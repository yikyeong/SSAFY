import sys
sys.stdin = open("회문_input.txt","r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    str_list = [[input()] for _ in range(N)]
    
        