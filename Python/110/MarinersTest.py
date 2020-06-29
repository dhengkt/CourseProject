# MsrinersTest
# Katie

# Sample module to practice
# using data files, and read statements
# and lists.

def main():

    infile = open("MarinersBattingAvg.txt","r")

    #for line in infile.readlines():
    #    line = line.replace("\n","")
    #    line = line.replace("\t",", ")
    #    print(line)

    # Find the number of each type of player.

    data = infile.read()
    
    c = data.count("Catcher")
    i = data.count("Infielder")
    o = data.count("Outfielder")
    dh = data.count("DH")

    p = 25 - (c + i + o +dh)
    
    print("The current Mariner's roster had "
          "{0} catchers, {1} infielder, "
          "{2} outfielder, {3} designated hitter "
          "and {4} pitchers."
          "".format(c,i,o,dh,p))
    
    infile.close()

    

main()
