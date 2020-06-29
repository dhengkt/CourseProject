if abs(sec // 60) >= 1:
    tempSec = sec // 60
    sec %= 60
    min += tempSec
    self.__sec = int(sec)
else:
    self.__sec = int(sec)

if abs(min // 60) >= 1:
    tempMin = min // 60
    min %= 60
    hrs += tempMin
    self.__min = int(min)
    self.__hrs = int(hrs)
else:
    self.__min = int(min)
    self.__hrs = int(hrs)