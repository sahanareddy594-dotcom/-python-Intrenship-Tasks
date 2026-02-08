def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

num1 = int(input("Enter first number: "))
print("Factorial of", num1, "is", factorial(num1))

num2 = int(input("Enter second number: "))
print("Factorial of", num2, "is", factorial(num2))
