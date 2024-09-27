scores = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]

sum_score = 0

while scores :
    score = scores.pop()
    if score >= 80 :
        sum_score += score

print(sum_score)