import numbers

num = eval(input("Enter a numerator: "))
den = eval(input("Enter a denominator: "))
r1 = numbers.Rational(num, den)

num = eval(input("Enter a numerator: "))
den = eval(input("Enter a denominator: "))
r2 = numbers.Rational(num, den)

if r1 != r2:
    print(r1, r2, " They are not equal.")
else:
    print(r1, r2, " They are equal.")

r3 = r1 * r2
print("Addition: ", r3)