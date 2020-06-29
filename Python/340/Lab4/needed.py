import greedyRobot

print("Enter coordinates point for robotX, robotY, treasureX, treasureY:")
robotX, robotY, treasureX, treasureY = map(int, input().split())
robot1 = greedyRobot.Robot(robotX, robotY, treasureX, treasureY)