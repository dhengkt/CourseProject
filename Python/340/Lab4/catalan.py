import sys

def catalan(n):
    result = 0
    if n < 0:
        return "Error: Please enter a positive number."
    if n == 0 or n == 1:
        return 1
    for i in range(n):
        result += catalan(i) * catalan(n - i - 1)
    return result

number = input(sys.argv)
# Change number into integer since the passing value is string
print(catalan(int(number)))
