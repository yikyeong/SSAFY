N = 5
lst = [55, 7, 78, 12, 42]

def bubble_sort(numbers, n):
    # numbers : 정렬하고 싶은 대상
    # n : 배열(리스트)의 길이

    # i번 자리의 주인 정하기 (n-1 ~ 1)
    for i in range(n - 1, 0, -1):       # i는 n-1부터 1까지 반복합니다. 0은 포함되지 않습니다.
        # 맨 앞에서 두개씩 비교 하면서 큰게 뒤로 오도록 자리 바꿔
        for j in range(i):              # j는 0부터 i-1까지 반복합니다. (i가 1일 때 j는 0까지만 돕니다.)
            # 자리를 바꾸는 조건
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                # 다른 언어에서 자리 바꾸기
                # 임시 변수를 하나 만들어서 기억
                # temp = numbers[j]
                # numbers[j] = numbers[j+1]
                # numbers[j+1] = temp

bubble_sort(lst, N)
print(lst)

