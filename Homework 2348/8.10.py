if __name__ == '__main__':
    user_input = input()
    word = ""
    revword = ""
    for ch in user_input.lower():
        if ch != ' ':
            word += ch
            revword = ch + revword
    if word == revword:
        print(user_input + " is a palindrome")
    else:
        print(user_input + " is not a palindrome")