num = int(input())

list = []
for i in range(1,num+1) :
    if num%i == 0 :
        list.append(i)
        print(f"{i}(은)는 {num}의 약수입니다.")

if len(list) == 2 :
    print(f"{num}(은)는 {list[0]}과 {list[1]}로만 나눌 수 있는 소수입니다.")