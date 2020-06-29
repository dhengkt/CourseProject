# This class represent a time presenting program. The time span can be presented by
# a integer of seconds, minutes, and hours.
# The key math operations are addition, subtraction and unary negation.

class TimeSpan:

    def __init__(self, seconds=0, minutes=0, hours=0):
        self.__seconds = seconds
        self.__minutes = minutes
        self.__hours = hours
        self.setTime(seconds, minutes, hours)

    def getHours(self):
        return self.__hours

    def getMinutes(self):
        return self.__minutes

    def getSeconds(self):
        return self.__seconds

    def setTime(self, seconds, minutes, hours):
        if abs(seconds // 60) >= 1:
            tempSec = seconds // 60
            seconds %= 60
            minutes += tempSec
            self.__seconds = int(seconds)
        else:
            self.__seconds = int(seconds)

        if abs(minutes // 60) >= 1:
            tempMin = minutes // 60
            minutes %= 60
            hours += tempMin
            self.__minutes = int(minutes)
            self.__hours = int(hours)
        else:
            self.__minutes = int(minutes)
            self.__hours = int(hours)

    # Helper Function
    # Not really using. (Just an idea)
    def getSign(self, seconds, minutes, hours):
        sign = 0 if hours == 0 else (hours == 1 if hours > 0 else -1)

        if sign == 0:
            sign = (minutes == 0 if minutes == 0 else (minutes == 1 if minutes > 0 else -1))
        if sign == 0:
            sign = (seconds == 0 if seconds == 0 else (seconds == 1 if seconds > 0 else -1))
        return sign

    # Overload operations and unary negation
    def __add__(self, rhs):
        return TimeSpan(self.__seconds + rhs.__seconds, self.__minutes + rhs.__minutes, self.__hours + rhs.__hours)

    def __sub__(self, rhs):
        return TimeSpan(self.__seconds - rhs.__seconds, self.__minutes - rhs.__minutes, self.__hours - rhs.__hours)

    def __iadd__(self, rhs):
        return TimeSpan(self.__seconds + rhs.__seconds, self.__minutes + rhs.__minutes, self.__hours + rhs.__hours)

    def __isub__(self, rhs):
        return TimeSpan(self.__seconds - rhs.__seconds, self.__minutes - rhs.__minutes, self.__hours - rhs.__hours)

    def __neg__(self):
        return TimeSpan(-self.__seconds, -self.__minutes, -self.__seconds)

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

    def __gt__(self, rhs):
        if self.getHours() > rhs.getHours():
            return True
        elif self.getHours() == rhs.getHours() and self.getMinutes() > rhs.getMinutes():
            return True
        elif self.getHours() == rhs.getHours() and self.getMinutes() >= rhs.getMinutes() and self.getSeconds() > rhs.getSeconds():
            return True
        else:
            return False

    def __ge__(self, rhs):
        if self.getHours() >= rhs.getHours() and self.getMinutes() >= rhs.getMinutes() and self.getSeconds() >= rhs.getSeconds():
            return True
        else:
            return False

    def __lt__(self, rhs):
        if self.getHours() < rhs.getHours():
            return True
        elif self.getHours() == rhs.getHours() and self.getMinutes() < rhs.getMinutes():
            return True
        elif self.getHours() == rhs.getHours() and self.getMinutes() <= rhs.getMinutes() and self.getSeconds() < rhs.getSeconds():
            return True
        else:
            return False

    def __le__(self, rhs):
        if self.getHours() <= rhs.getHours() and self.getMinutes() <= rhs.getMinutes() and self.getSeconds() <= rhs.getSeconds():
            return True
        else:
            return False

    def __str__(self):
        return "Hours: {}, Minutes: {}, Seconds: {}".format(self.getHours(), self.getMinutes(), self.getSeconds())