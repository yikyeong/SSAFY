# 피보나치 수열의 결과를 생성하는 프로그램을 작성하십시오.
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
num = int(input())

list = [1] * (num)

for i in range(2,num):
    list[i] = list[i-1]+list[i-2]
print(list)