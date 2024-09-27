'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

# 전위 순회 구현( 나 -> 왼쪽 -> 오른쪽 ) -> 이건 이진 트리만 가능한 코드
def preorder(node):
    if node == 0:
        return
    # 전위 순회
    print(node, end=" ")    # 본인을 먼저 확인
    preorder(left[node])
    preorder(right[node])

    # 중위 순회
    preorder(left[node])
    print(node, end=" ")  # 왼쪽을 보고나서, 본인을 확인
    preorder(right[node])

    # 후위 순회
    preorder(left[node])
    preorder(right[node])
    print(node, end=" ")  # 왼쪽, 오른쪽 자식들을 모두 보고나서, 본인을 확인


# left, right를 쓰는 버전
# 단, 입력이 반드시 각 노드당 "최대 2번"씩만 들어온다고 가정한 코드
N = int(input())                            # 정점의 개수(정점: 1~N번)
arr = list(map(int, input().split()))

left = [0] * (N+1)                          # 왼쪽 자식 번호를 저장할 리스트 # 1부터 시작하기 때문에 +1 해준것임
# ex) left[3] = 2 ==> 3번 부모의 왼쪽 자식은 2다.
right = [0] * (N+1)                         # 오른른쪽자식 번호를 저장할 리스트

for i in range(0,len(arr),2):
    parent, child = arr[i], arr[i+1]

    if left[parent] == 0:                   # 만약 left[parent]에 자식이 없다면
        left[parent] = child                # 왼쪽에 삽입
    # 왼쪽 자식은 있는데, 오른쪽 자식이 없다면 오른쪽에 삽입
    else:
        right[parent] = child

# print(left)
# print(right)

root = 1        # 시작점은 1이라고 가정
preorder(root)


# def pre_order(T):
#     if T:
#         print(T, end = ' ')
#         pre_order(left[T])
#         pre_order(right[T])
#
# N = int(input())        # 1번부터 N번까지인 정점
# E = N-1
# arr = list(map(int, input().split()))
# left = [0]*(N+1)        # 부모를 인덱스로 왼쪽자식번호 저장
# right = [0]*(N+1)       #
# par = [0]*(N+1)         # 자식을 인덱스로 부모 저장
#
# for i in range(E):
#     p, c = arr[i*2], arr[i*2+1]
# # for i in range(0,E*2, 2):
# #         p, c = arr[i], arr[i + 1]
#     if left[p]==0:          # 왼쪽자식이 없으면
#         left[p] = c
#     else:
#         right[p] = c
#     par[c] = p
#
# c = N
# while par[c]!=0:        # 부모가 있으면
#     c = par[c]          # 부모를 새로운 자식으로 두고
# root = c                # 더이상 부모가 없으면 root
# print(root)
# pre_order(root)