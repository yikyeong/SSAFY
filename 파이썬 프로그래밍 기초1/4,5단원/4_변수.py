# 1~9 사이의 정수 a를 입력받아 
# a + aa + aaa + aaaa 의 값을 계산하는 프로그램을 작성하십시오.

a = int(input())

if 1 <= a <= 9 :
    aa = int(str(a) * 2)
    aaa = int(str(a) * 3)
    aaaa = int(str(a) * 4)

print(a + aa + aaa + aaaa)
