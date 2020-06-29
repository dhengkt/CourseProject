def find1(list, val):
    for i in range(len(list)):
        if list[i] == val:
            return True
    return False

def find2(list, val):
    temp = list
    temp.sort()
    return binarySearch(temp,val)

def find3(list, val):
    if val in list:
        return True
    else:
        return False

def find4(list, val):
    result = True
    i = 1
    while i < len(list):
        if list[i - 1] > list[i]:
            result = False
        i += 1
    if result:
        return binarySearch(list, val)
    else:
        return "This list is not pre-sorted."

# Helper function
def binarySearch(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] < item:
            low = mid + 1
        elif list[mid] > item:
            high = mid - 1
        else:
            return True
    return False
