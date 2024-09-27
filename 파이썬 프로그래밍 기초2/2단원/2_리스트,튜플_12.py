arr = list(i**2 for i in range(1,21))
result=(i for i in arr if i%3!=0 or i%5!=0)
print(list(result))

# arr = list(i*i for i in range(1,21))
# final_arr=[]
# for i in arr :
#     if i % 3 != 0 or i % 5 != 0:
#         final_arr.append(i)
# print(final_arr)