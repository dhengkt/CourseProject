# Mariners
# HsinYu Chi(Katie)

# This program will open a data file of
# Mariner's batting averages and generate
# three seperate lists for names, positions and
# batting averages, then output results.

def main():

    nameList = []
    positionList = []
    batavgList = []
    infile = open("MarinersBattingAvg.txt","r")

    dataList = infile.readlines()
    
    for i in range(1,len(dataList)):
        tempList = dataList[i].split()
        
        # Create the name list.
        name = tempList[1] + " " + tempList[0]
        nameList.append(name)
        
        # Create the position list.
        position = tempList[2]
        position = position.replace("DH","designated hitter")
        positionList.append(position)

        # Create the batting averages list.
        batavg = tempList[3]
        batavgList.append(batavg)
                    
        # Output the result.
        print("{0}, {1}, is batting {2}."
              .format(name,position.lower(),batavg))
        
    # Print the lists.    
    #print(nameList)
    #print(positionList)
    #print(batavgList)
              
main()
