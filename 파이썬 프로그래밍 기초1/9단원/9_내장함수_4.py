string = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"

# 점수를 매핑할 딕셔너리
scores = {'A': 4, 'B': 3, 'C': 2, 'D': 1}

# 문자열의 각 문자에 대해 점수를 매핑하고 총합을 계산
total_score = sum(map(lambda char: scores[char], string))

print(total_score)
