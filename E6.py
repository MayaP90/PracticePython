# String List

# Problem: Ask the user for a string and print out whether this string is
# a palindrome or not. (A palindrome is a string that reads the same forwards
# and backwards.)

# reversing a string
word = str(input("Enter a word:"))
reverse = word[::-1]
print(reverse)
if word == reverse:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")
