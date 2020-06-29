# project3A
# HsinYu Chi(Katie)

# This program is designed to open
# and look at the data in motifFinding.txt.

def OutputResult(index):

    position = ""
    print("The sub-string t occurs within the string s at starting"
          " positions indexed at ", ", ".join(str(x) for x in index),end=".")
    
def main():

    # Open the file
    infile = open("motifFinding.txt", "r")

    # Create the strings s and t.
    strings = infile.readline()
    s = strings.split()

    stringt = infile.readline()
    t = stringt.rstrip()

    # Find the string t in string s.
    index = []
    
    for i in range(len(strings)):
        a = strings[i:i+len(t)].count(t)
        if a == 1:
            index.append(i)

    OutputResult(index)

main()
