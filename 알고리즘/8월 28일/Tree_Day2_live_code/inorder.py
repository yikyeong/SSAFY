import sys
sys.stdin = open("input (1).txt","r")

for tc in range(1, 11):
    N = int(input())
    nodes = [list(input().split()) for _ in range(N)]
    words = [""] * (N + 1)
    for i in range(N):
        words[i + 1] = nodes[i][1]
    cleft = [0] * (N + 1)
    cright = [0] * (N + 1)
    for j in range(N - 1):
        length = len(nodes[j])
        if length > 2:
            parent = int(nodes[j][0])
            child = nodes[j][2:]
            cleft[parent] = int(child[0])
            if length > 3:
                cright[parent] = int(child[1])


    def inorder(idx, str, words, cleft, cright):
        if idx:
            str = inorder(cleft[idx], str, words, cleft, cright)
            str.append(words[idx])
            str = inorder(cright[idx], str, words, cleft, cright)
            return str
        else:
            return str


    answer = "".join(inorder(1, [], words, cleft, cright))
    print(f"#{tc} {answer}")