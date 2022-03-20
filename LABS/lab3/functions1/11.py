def isPal(string):
    string = list(string)
    temp = string
    temp = temp.reverse()

    if temp == string:
        return True
    return False

if __name__ == "__main__":
    s = input("Enter the word: ")
    if isPal(s):
        print("It is a palindrome!")
    else:
        print("It is not a palindrome!")