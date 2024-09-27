person1 = input()
person2 = input()
rsp1 = input()
rsp2 = input()

if rsp1 == rsp2 :
    print("비겼습니다.")
elif (rsp1 == "가위" and rsp2 == "보") or \
    (rsp1 == "바위" and rsp2 == "가위") or \
    (rsp1 == "보" and rsp2 == "바위"):
    print(f"{rsp1}가 이겼습니다!")
else :
    print(f"{rsp2}가 이겼습니다!")