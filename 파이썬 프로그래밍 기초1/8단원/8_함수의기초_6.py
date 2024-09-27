# 정렬된 숫자를 가진 리스트에서 특정 숫자를 찾는 함수를 정의하고,
# 이 함수를 이용해 임의의 숫자의 포함 여부를 출력하는 프로그램을 작성하십시오.
def find_num(num_list,num) :
    for i in num_list :
        if num==i :
            return True
    return False

num_list = [2, 4, 6, 8, 10]
find5=find_num(num_list,5)
find10=find_num(num_list,10)
print(num_list)
print(f"5 => {find5}")
print(f"10 => {find10}")