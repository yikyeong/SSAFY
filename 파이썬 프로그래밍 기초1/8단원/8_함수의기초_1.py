
def reverse_word(word) :
    in_reverse = ""
    for i in word :
        in_reverse = i+in_reverse
    return in_reverse

def palindrome(word, already_reverse) :
    print(already_reverse)
    if word == already_reverse :
        print("입력하신 단어는 회문(Palindrome)입니다.")
    else :
        print("입력하신 단어는 회문(Palindrome)이 아닙니다.")

word = input()
already_reverse = reverse_word(word)
palindrome(word, already_reverse)
