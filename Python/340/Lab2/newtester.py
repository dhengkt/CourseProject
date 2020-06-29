import time340

pts = 0

t1 = time340.TimeSpan(-60,1) # 00:00:00
t2 = time340.TimeSpan(0) # 00:00:00
t3 = time340.TimeSpan(0,120,1) # 03:00:00
t4 = time340.TimeSpan(30.2) # float points seconds, 00:00:30
t5 = time340.TimeSpan(-30, 1.5) # float point minutes, 00:01:00
t6 = time340.TimeSpan(-10,4,1.5) # float point hours, 01:33:50

# Case 1:
if t1.getSeconds() == 0 and t1.getMinutes() == 0 and t1.getHours() == 0 and t1==t2 :
    pts += 5
elif t1.getSeconds() == 0 and t1.getMinutes() == 0 and t1.getHours() == 0 :
    pts += 3
    print("Case 1: Zero time comparison error. -2pts")
elif t1==t2 :
    pts += 2
    print("Case 1: Zero time not set properly. -3pts")
else :
    print("Case 1: Zero time not set properly and comparison error. -5 pts")

# Case 2:
t10 = time340.TimeSpan(0)
t10.setTime(0, 1, 0)
t11 = time340.TimeSpan(0)
t11.setTime(0,0,1)
if t5 == t10 and t3 == t11 + t11 + t11 :
    pts += 5
elif t11.getHours() == 1 and t10.getMinutes() == 1 :
    pts += 3
    print("Case 2: Issue with one of the comparisons. -2pts")
else :
    print("Case 2: Setter is not working. -5pts")

# Case 3:
if t6.getSeconds() == 50 and t6.getMinutes() == 33 and t6.getHours() == 1 :
    pts += 3
else :
    print("Case 3: Float point hour not set properly. -3pts")

# Case 4:
if t5.getSeconds() == 0 and t5.getMinutes() == 1 and t5.getHours() == 0 :
    pts += 3
else :
    print("Case 4: Float point minute not set properly. -3pts")

# Case 5:
if t4.getSeconds() == 30 and t4.getMinutes() == 0 and t4.getHours() == 0 :
    pts += 3
else :
    print("Case 5: Float point seconds not set properly. -3pts")

# Case 6:
t7 = time340.TimeSpan(0)
t7.setTime(59, 0, 0)
if t4 <= t7 :
    pts += 2
else :
    print("Case 6: Less than or equal to comparison error. -2pts")

# Case 7:
if t4 < t7 :
    pts += 2
else :
    print("Case 7: Less than comparison error. -2pts")

# Case 8:
if t5 > t7 :
    pts += 2
else :
    print("Case 8: Greater than comparison error. -2pts")

# Case 9:
if t5 >= t7 :
    pts += 2
else :
    print("Case 9: Greater than or equal to comparison error. -2pts")

# Case 10:
t12 = time340.TimeSpan(0,1,0)
t13 = time340.TimeSpan(30,0,0)
if t12 == t13 + t13 :
    pts += 3
else :
    print("Case 10: Addition operation is not working. -3pts")

# Case 11:
if t13 == t12 - t13 :
    pts += 3
else :
    print("Case 11: Subtraction operation is not working. -3pts")

# Case 12:
t8 = time340.TimeSpan(-30, 0)
if -t4 == t8 :
    pts += 2
else :
    print("Case 12: Negative operation is not working. -2pts")

print (pts)
