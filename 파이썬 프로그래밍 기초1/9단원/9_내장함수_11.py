s = 'abcdef'
value = range(len(s))

dictionary = dict(zip(s,value))

for key,value in dictionary.items():    
    print(f"{key}: {value}")