# This class represent a time presenting program. The time span can be presented by
# a integer of seconds, minutes, and hours.
# The key math operations are addition, subtraction and unary negation.

import numpy

class TimeSpan:

    def __init__(self, sec=0, min=0, hrs=0):
        self.__sec = sec
        self.__min = min
        self.__hrs = hrs
        self.setTime(sec, min, hrs)

    def getHours(self):
        return self.__hrs

    def getMinutes(self):
        return self.__min

    def getSeconds(self):
        return self.__sec

    def setTime(self, sec, min, hrs):
        sign = self.getSign(sec, min, hrs)
        checkSec = -1 if numpy.signbit(sec) else 1
        checkMin = -1 if numpy.signbit(min) else 1

        min += checkSec * abs(sec // 60.0)
        sec %= 60

        hrs += checkMin * abs(min // 60.0)
        min %= 60

        if sec != 0 and sign != checkSec:
            sec += (sign * 60)
            min += -sign
        if min != 0 and sign != checkMin:
            min += (sign * 60)
            hrs += -sign

        self.__sec = sec
        self.__min = min
        self.__hrs = hrs

        return True

    # Helper Function
    def getSign(self, sec, min, hrs):
        sign = 0 if hrs == 0 else (hrs == 1 if hrs > 0 else -1)

        if sign == 0:
            sign = (min == 0 if min == 0 else (min == 1 if min > 0 else -1))
        if sign == 0:
            sign = (sec == 0 if sec == 0 else (sec == 1 if sec > 0 else -1))
        return sign


    # Overload operations and unary negation
    def __add__(self, rhs):
        return TimeSpan(self.__sec + rhs.__sec, self.__min + rhs.__min, self.__hrs + rhs.__hrs)

    def __sub__(self, rhs):
        return TimeSpan(self.__sec - rhs.__sec, self.__min - rhs.__min, self.__hrs - rhs.__hrs)

    def __iadd__(self, rhs):
        return TimeSpan(self.__sec + rhs.__sec, self.__min + rhs.__min, self.__hrs + rhs.__hrs)

    def __isub__(self, rhs):
        return TimeSpan(self.__sec - rhs.__sec, self.__min - rhs.__min, self.__hrs - rhs.__hrs)

    def __neg__(self):
        return TimeSpan(-self.__sec, -self.__min, -self.__sec)

    # Comparators
    def __eq__(self, rhs):
        if self.getSeconds() == rhs.getSeconds() and self.getMinutes() == rhs.getMinutes() and self.getHours() == rhs.getHours():
            return True
        else:
            return False

    def __ne__(self, rhs):
        if self == rhs:
            return False
        else:
            return True

    def __ge__(self, rhs):
        if self.getSeconds() >= rhs.getSeconds() and self.getMinutes() >= rhs.getMinutes() and self.getHours() >= rhs.getHours():
            return True
        else:
            return False

    def __gt__(self, rhs):
        if self.getSeconds() > rhs.getSeconds() and self.getMinutes() > rhs.getMinutes() and self.getHours() > rhs.getHours():
            return True
        else:
            return False

    def __le__(self, rhs):
        if self >= rhs:
            return False
        else:
            return True

    def __lt__(self, rhs):
        if self > rhs:
            return False
        else:
            return True

    def __str__(self):
        return "Hours: " + str(self.__hrs) + ", Minutes: " + str(self.__min) + ", Seconds: " + str(self.__sec)