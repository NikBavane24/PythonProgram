

#string1="radar"
def palindrome(string1):
    string1=string1.lower()
    string2=string1[::-1]
    if string1==string2:
        print("Both the strings are Palindrome")
    else:
        print("Both the strings are not Palindrome")

palindrome("radaR")

