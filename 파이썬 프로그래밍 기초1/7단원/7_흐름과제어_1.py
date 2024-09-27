score = [88, 30, 61, 55, 95]

for sc in range(len(score)) :
    if score[sc] >= 60 :
        print(f"{sc+1}번 학생은 {score[sc]}점으로 합격입니다.")
    else :
        print(f"{sc+1}번 학생은 {score[sc]}점으로 불합격입니다.")