import time340

print("Version B of Test")
# 40 pts total. 5 pts toward documentation, and 35 pts toward tests
pts = 0

# Construct times
t1 = time340.TimeSpan(45) # 00:0:45
t2 = time340.TimeSpan(-59, 59) # 00:58:01
t3 = time340.TimeSpan(0, 30, -2) # -01:30:00

# Case 1:
# Test getter & normalization(increment)
# 2 pts
if t1.getSeconds() == 45 and t1.getMinutes() == 0 :
    pts += 2
else :
    print("ERROR:   Getter doesn't work. -2pts")
    print("         Getters are replaced with correct version")

# Case 2:
# Test getter & normalization(decrement)
# 1 pts
if t2.getSeconds() == 1 and t2.getMinutes() == 58:
    pts += 1
else :
    print("ERROR:   Cannot normalize(decrement) time. -1pt")

# Case 3:
# Test getter & normalization(increment and decrement at same time)
# 2 pts
if t3.getHours() == -1 and t3.getMinutes() == -30 :
    pts += 2
else :
    print("ERROR:   Cannot normalize time. -2pts")

# Case 4:
# Test setter and ==
# 2pts for setter, and 3pts for equal operation
t4 = time340.TimeSpan(0)
t4.setTime(45, 0, 0)
if t1 == t4 :
    pts += 5
else:
    print("ERROR:   Equal operator is not working. -5pts")

# Case 5:
# Test addition operation
# 5 for addition operation
t5 = time340.TimeSpan(46,58)
if t1 + t2 == t5 :
    pts += 5
else :
    print("ERROR:   Addition operation is not working. -5pts")

# Case 6:
# Test subtraction operation
# 5 for subtraction operation
t6 = time340.TimeSpan(-1, -28, -2)
if t6 == t3 - t2 :
    pts += 5
else :
    print("ERROR:   Subtraction operation is not working. -5pts")

# Case 7:
# Test negative TimeSpan and negative operator
# 1pt for constructor. 4pts for negative operator
t4 = time340.TimeSpan(-45, 0)
if -t1 == t4 :
    pts += 5
elif t4.getSeconds() == -45:
    pts += 1
    print("ERROR:   Negative operator is not working. -4pts")
elif (-t1).getSeconds() == -45 :
    pts += 4
    print("ERROR:   Negative constructor is not working. -1pts")
else :
    print("ERROR:   Negative constructor and negative operator are not working. -5pts")

# Case 8:
# Test not equal operator
# 2 pts
if t1 != t2 :
    pts += 2
else :
    print("ERROR:   not equal is not working. -2pts")

# Case 9:
# Test Greater than operator
# 2 pts
if t2 > t1 :
    pts += 2
else :
    print("ERROR:   Greater than operator is not working. -2pts")

# Case 10:
# Test Greater than or equal to operator
# 1 pt for each
if t1 >= t2 :
    print("ERROR:   Greater than or equal to operator is not working.(Greater then version)")
else :
    pts += 1

if t1 >= t1 :
    pts += 1
else :
    print("ERROR:   Greater than or equal to operator is not working.(Greater then version)")

# Case 11:
# Test less than operator
# 2 pts
if t1 < t2 :
    pts += 2
else :
    print("ERROR:   Less than operator is not working. -2pts")

# Case 10:
# Test less than or equal to operator
# 1 pt for each
if t2 <= t1 :
    print("ERROR:   Less than or equal to operator is not working.(Greater then version)")
else :
    pts += 1

if t1 <= t1 :
    pts += 1
else :
    print("ERROR:   Less than or equal to operator is not working.(Greater then version)")

# Print out the final test grade
print("You get " + pts.__str__())
