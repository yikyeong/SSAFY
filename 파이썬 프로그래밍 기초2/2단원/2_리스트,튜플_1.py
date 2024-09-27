score = [(90, 80), (85, 75), (90, 100)]

# enumerate 함수는 첫 번째 인수로 순회할 객체를 받으며, 
# 두 번째 인수로 시작 인덱스 값을 받는다. 
for i, (korean,math) in enumerate(score, start=1) :
    total = korean + math
    average = total / 2
    print(f"{i}번 학생의 총점은 {total}점이고, 평균은 {average}입니다.")