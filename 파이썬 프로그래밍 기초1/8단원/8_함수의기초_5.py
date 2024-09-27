# 리스트의 항목 중 유일한 값으로만 구성된 리스트를 반환하는 함수를 정의하고
# 이 함수를 이용해 리스트의 중복 항목을 제거하는 프로그램을 작성하십시오.


def one_value(first_list):
    check_list = []
    for i in first_list:
        if i not in check_list:
            check_list.append(i)
    return check_list

first_list = [1, 2, 3, 4, 3, 2, 1]
result=one_value(first_list)
print(first_list)
print(result)