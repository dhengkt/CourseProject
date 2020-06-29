# extraeredit
# HsinYu Chi(Katie)

# This program will open a text file,
# exchange the order of data to a list,
# and output the results.

def convertData(filename):

    infile = open(filename,"r")
    List = infile.readline()
    temp = List.split(",")
    return(temp)

def convertList(List1):

    NameList2 = []
    for i in range(len(List1)):
        s = List1[i]
        namestr = s.split()
        name = namestr[1] + "," + namestr[0]
        NameList2.append(name)
    return(NameList2)

def OutputResult(List2):

    for ch in List2:
        print(ch)

def main():

    name = "Names.txt"
    nameList1 = convertData(name)
    nameList2 = convertList(nameList1) 
    OutputResult(nameList2)

main()
