colorFile = open("","w")
colorFile.write("Red\nBlue\nGreen")
colorFile.close()

coloFile = open("", "r")
line = colorFile.readline().strip()
while line != "":
    print(line)
    line = colorFile.readline()