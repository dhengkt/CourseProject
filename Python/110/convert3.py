# convert3.py
# HsinYu Chi(Katie)

# This program converts Fahrenheit to Celsius.

def main():

    print("This program converts Fahrenheit to Celsius.")
    
    Fahrenheit = eval(input("Enter the temperature of Fahrenheit: "))
    Celsius = (Fahrenheit - 32) * (5/9)

    print(Fahrenheit, "Fahrenheit is", Celsius, "Celsius.")

main()
