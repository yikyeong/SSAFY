# 다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.
# ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
# for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.
blood_type = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
blood_cnt = {'A':0, 'O':0, 'B':0, 'AB':0}

for i in blood_type:
    if i == 'A' :
        blood_cnt['A']+=1
    elif i == 'B' :
        blood_cnt['B']+=1
    elif i == 'O' :
        blood_cnt['O']+=1
    elif i == 'AB' :
        blood_cnt['AB']+=1

print(blood_cnt)