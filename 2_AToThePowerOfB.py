
def multiply(x, y):
    result = 0
    for i in range(y):
        result += x

    return result


def power(x, y):
    result = x

    if y == 0:
        result = 0
    else:
        for i in range(y-1):
            result = multiply(result, x)

    return result


print("This program will output the answer to num1 ^ num2 \n")
number_1 = int(input("Please introduce the first number: "))
number_2 = int(input("Please introduce the second number: "))

print("The result of", number_1, "^", number_2,"is: ", power(number_1, number_2))
