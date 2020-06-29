import sys

avengers = open(sys.argv[1], "r")
avengersDict = {}
line = avengers.readline().strip()  # stripping out the white space
print(line)

while line != "":
    alist = line.split()
    avengersDict[alist[0]] = alist[1]
    line = avengers.readline().strip()
avengers.close()

m = input("Who is your favorite avenger?")
print("Actor: ", avengersDict[m])
