# 다음의 결과와 같이 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하십시오
num = int(input())

for i in range(1,num+1) :
    if num % i == 0 :
        print(f"{i}(은)는 {num}의 약수입니다.")