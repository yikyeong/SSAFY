num_list = list(range(1,11))
result = list(map(lambda x:x**2,(filter(lambda x:x%2 == 0, num_list))))
print(result)