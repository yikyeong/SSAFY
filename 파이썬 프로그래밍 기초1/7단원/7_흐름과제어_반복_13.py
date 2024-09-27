# 10진수를 2진수로 변환하는 프로그램을 작성하십시오.

number = int(input())

result = ""
if number == 0 :
    print(0)
while number :
    remain = number % 2
    result = str(remain) + result
    number = number // 2

print(result)