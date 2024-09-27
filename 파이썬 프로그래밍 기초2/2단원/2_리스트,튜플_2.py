string = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
vowels = 'aeiou'
result = ''.join([char for char in string if char.lower() not in vowels])
print(result)

