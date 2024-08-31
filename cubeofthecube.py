def CalculateCube(number):
    result = number * number * number
    return result

x = int(input("Enter a number "))
result = CalculateCube(x)
print(result)