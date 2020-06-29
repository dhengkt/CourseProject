# MotifTesting
# HsinYu Chi(Katie)

# This program is designed to open
# and look at the data in
# motifFinding.txt.

def main():

    infile = open("motifFinding.txt", "r")

    dataList = infile.readlines()
    print(dataList)

main()
