import sys
sys.stdin = open("txt_folder/이진수_input.txt","r")

T = int(input())

dic_16 = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}
for tc in range(1, T + 1):
    N, str_list = input().split()  # N : 자리수, str_list : 16진수
    arr = list(str_list)
    ans = ""
    for i in range(int(N)):
        ans += dic_16[arr[i]]

    print(f"#{tc} {ans}")