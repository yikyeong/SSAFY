T = int(input())
code = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N : 세로, M : 가로
    arr = [input() for _ in range(N)]
    store = ""
    store_code = []

    for i in range(N):
        if "1" in arr[i]:
            store = arr[i]
            break
    for j in range(M - 1, -1, -1):
        if store[j] == "1":
            store = store[j - 55:j + 1]
            break
    for t in range(0, 56, 7):
        temp = store[t:t + 7]
        store_code.append(code[temp])

    odd = sum(store_code[0:8:2])
    even = sum(store_code[1:8:2])
    sum_code = (odd * 3) + even
    result = odd + even
    if sum_code % 10:
        result = 0

    print(f"#{tc} {result}")