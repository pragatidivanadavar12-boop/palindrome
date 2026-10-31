word = input("Enter a word or number: ")
a = word.lower()
if a == a[::-1]:
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")
