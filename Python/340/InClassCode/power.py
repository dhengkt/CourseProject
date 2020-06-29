def pow(x, n):
    if n < 0:
        return "Error: should be positive number"
    elif n == 0:
        return 1
    else:
        return x * pow(x, n - 1)


x = eval(input("Enter X: "))
n = eval(input("Enter n: "))
print(pow(x, n))
