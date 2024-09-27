def square(num) :
    for i in num:
        result = i**2
        print(f"square({i}) => {result}")

num = list(map(int, input().split(",")))
square(num)