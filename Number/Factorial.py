def fact(x):
    if x < 0:
        return "Factorial is not defined for negative numbers"
    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

x = int(input("Enter a number: "))
print(fact(x))
