# 킬로그램(kg)를 파운드(lb)으로 변환하는 프로그램을 작성하십시오.
# 이 때 1 킬로그램은 2.2046 파운드입니다.

kg_num = int(input())
pd_num = kg_num * 2.2046
print(f"{kg_num:.2f} kg =>  {pd_num:.2f} lb")