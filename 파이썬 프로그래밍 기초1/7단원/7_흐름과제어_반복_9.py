# while문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.
"""
*******
 *****
  ***
   *
"""
stars = 7
space = 0

while stars > 0 :
    print(" " * space + "*" * stars)
    stars -= 2
    space += 1

lines = 4
for i in range(lines) :
    print(" "*i + "*"*(7-2*i))

