# 20% 농도의 소금물 100g과 물 200g을 혼합한 소금물의 농도(%)를 소수점 두 번째 자리까지 구하는 프로그램을 작성하십시오.

salt_per = 20       # 소금물 농도
salt_water = 100    # 소금물의 양
water = 200         # 물의 양

# 소금물에 포함된 소금의 양
salt = (salt_per/100)*salt_water

# 기존 소금물에 물을 더한 소금물의 농도
plus_salt_per = (salt_per/(salt_water+water))*100

print(f"혼합된 소금물의 농도: {plus_salt_per:.2f}%")