def multiply(*num) :
    result = 1
    for i in num:
        if type(i) != int :
            return "에러발생"
        else :
            result *= i
    return result
print(multiply(1, 2, '4', 3))