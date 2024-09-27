# num = []
# for i in range(100, 301):
#     check = str(i)
#     if all( int(digit) % 2 == 0 for digit in check) :
#         num.append(check)
# print(",".join(num))

# 다시 풀어본 코드!!
arr = []
for i in range(100,301):
    check = str(i)
    if all(int(digit) % 2 == 0 for digit in check) :
        arr.append(check)
print(",".join(arr))










