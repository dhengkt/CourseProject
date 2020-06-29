# testingfile
# Katie

# This program is for testing the file.

def main():

    List = []
    infile = open("carModelData_city.txt","r")
    data = infile.readlines()
    List.append(data)
    print(List)

main()
