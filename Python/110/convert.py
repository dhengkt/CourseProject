#convert.py
#Katie Chi

#This program convert inputed miles to kilometers.

def main():
    
    mile = eval(input("Enter the miles:"))
    km = 1.60934 * mile
    print(mile, "miles is", km, "kilometers.")

main()
