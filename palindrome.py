
try:
    palindrome = input("Please introduce a number: ")
    palindrome_int = int(palindrome)
except:
    print("That is not a number")

palindrome_reverse = ""
for char in palindrome:
    palindrome_reverse = char + palindrome_reverse

if palindrome == palindrome_reverse:
    print("It's a palindrome!!")
else:
    print("It's NOT a palindrome")

## other:

a = 1234321
a_test = a
b = 0
while a_test > 0:
    b = 10 * b + (a_test % 10)
    a_test = a_test//10

if a == b:
    ## print("its a palindrome")
    print("fifne")

