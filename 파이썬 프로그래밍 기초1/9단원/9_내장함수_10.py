def max_num(*num):
    max_n = -1
    for i in num :
        if i > max_n :
            max_n = i
    return max_n
result = max_num(3, 5, 4, 1, 8, 10, 2)
print(f"max(3, 5, 4, 1, 8, 10, 2) => {result}")