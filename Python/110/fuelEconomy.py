# fuelEconomy
# HsinYu Chi(Katie)

# This program calls four functions to analysis
# from two data files, and output the results.

# Open the data file and create a float list.
def convertData(carModelData):

    infile = open(carModelData,"r")
    List = []
    
    for tempList in infile.readlines():
        tempList.replace("\n" , " " )
        List.append(float(tempList))
        
    return(List)

# Calculates the average mpg value for
# all mpg values in the list.
def averageMPG(List):

    avg = round(sum(List) / len(List),4)
    return(avg)

# Calculates the among of gas guzzler.
def countGasGuzzlers(List1,List2):

    dataList = []
    for i in range(len(List1)):
        if List1[i]< 22 or List2[i] < 27:
            num = "GasGuzzler"
            dataList.append(num)
        n = len(dataList)
    
    return(n)

# Output the results.
def OutputResult(CityList, AvgCity, Avghwy, Gasguzzlers):

    Listnum = len(CityList)
    print("The total number of vehicles tested is", Listnum, end=".\n")
    print("The average for the city mpg for all the vehicles tested is", AvgCity, end=".\n")
    print("The average for the highway mpg for all the vehicles tested is", Avghwy, end=".\n")
    print("The number of gas guzzlers among the vehicle models tested is", Gasguzzlers, end=".\n")

# The main function.
def main():

   carModelData_city = "carModelData_city.txt"
   cityList = convertData(carModelData_city)
   carModelData_hwy = "carModelData_hwy.txt"
   hwyList = convertData(carModelData_hwy)
   avgCity = averageMPG(cityList)
   avghwy = averageMPG(hwyList)
   gasguzzlers = countGasGuzzlers(cityList, hwyList)
   OutputResult(cityList, avgCity, avghwy, gasguzzlers)
   
main()
