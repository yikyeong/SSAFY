# 다음의 결과와 같이 어떤 한 양의 정수를 입력하여
# 그 숫자에 0~9가 몇 번 사용되었는지 표시하십시오.
"""
입력
11

출력
0 1 2 3 4 5 6 7 8 9
0 2 0 0 0 0 0 0 0 0
"""
# # 사용자로부터 양의 정수를 입력받기
# number = input("입력: ")
#
# # 0부터 9까지의 숫자 빈도를 저장할 리스트 초기화
# digit_count = [0] * 10
#
# # 입력된 숫자의 각 자리 숫자에 대해 빈도수를 계산
# for digit in number:
#     digit_count[int(digit)] += 1
#
# # 0부터 9까지의 숫자를 출력
# print(" ".join(str(i) for i in range(10)))
#
# # 각 숫자의 빈도수를 출력
# print(" ".join(str(count) for count in digit_count))

num = input()

arr = [0] * 10

for i in num :
    arr[int(i)] += 1

for N in range(10) :
    print(N, end=" ")

print()
for N in arr:
    print(N, end=" ")
















