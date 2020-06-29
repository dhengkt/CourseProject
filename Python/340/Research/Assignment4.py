#import catalan
import robot
import point

#for i in range (10):
#    print (catalan.catalanNum(i))

robo = robot
coord = point

xr, yr, xt, yt = input("Please enter the robot and treasure coordinates in the format xr, yr, xt, yt: ").split()
print("Robot coordinates: ", xr, ", ", yr)
print("Treasure coordinates: ", xt, ", ", yt)

robotPoint = coord.Point(xr, yr)
treasurePoint = coord.Point(xt, yt)
robotTest = robo.Robot(robotPoint, treasurePoint)

robotTest.findTreasure()
robotTest.pathsToTreasure()


