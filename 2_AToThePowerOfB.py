
def multiply(x, y):
    result1 = 0
    for i in range(y):
        result1 += x

    return result1


def power(x, y):
    result1 = x

    if y == 0:
        result1 = 0
    else:
        for i in range(y-1):
            result1 = multiply(result1, x)

    return result1


print("This program will output the answer to num1 ^ num2 \n")
try:
    number_1 = int(input("Please introduce the first number: "))
    number_2 = int(input("Please introduce the second number: "))
except:
    print("Please input a number")

print("The result of", number_1, "^", number_2,"is: ", power(number_1, number_2))


# Without using any functions
result = number_1
for i in range(number_2-1):
    temp_result = 0
    for c in range(number_1):
        temp_result += result

    result = temp_result

print(result)

# print(list(range(10,1,-1)))

a = 5
b = 4

power = 1

for i in range(b):
    result = 0
    for j in range(a):
        result += power
    power = result

print(power)
