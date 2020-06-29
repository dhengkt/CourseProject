# fact.py
# HsinYu Chi(Katie)

# This program will use a loop
# to find n! (n-factorial).

def main():

    n = eval(input("Enter n: "))
    x = 1
    for i in range(n):
        x = x * (i+1)
    print(x)

main()
