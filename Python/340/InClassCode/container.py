INITIAL_HASHMAP_SIZE = 23


class HashMap:
    def __init__(self):
        self.__size = INITIAL_HASHMAP_SIZE
        self.__keys = [None] * self.__size
        self.__values = [None] * self.__size
        self.__count = 0

    def getCounts(self):
        return self.__count

    def put(self, key, data):
        if self.__count == self.__size:
            raise OverflowError
        nextSlot = self.hashFunction(key)
        while self.__keys[nextSlot] is not None and self.__keys[nextSlot] != key:
            nextSlot = self.rehash(nextSlot)
        if self.__keys[nextSlot] == key:
            self.__values[nextSlot] = data
        else:
            self.__keys[nextSlot] = key
            self.__values[nextSlot] = data
            self.__count += 1

    def get(self, key):
        position = self.hashFunction(key)
        startSlot = position
        while self.__keys[position] is not None and self.__keys[position] != key:
            position = self.rehash(position)
            if position == startSlot:
                return None
        return self.__values[position]

    def __setitem__(self, key, data):
        return self.put(key, data)

    def __getitem__(self, key):
        return self.get(key)

    def __str__(self):
        repString = ""
        for i in range(self.__size):
            if self.__keys[i] is not None:
                repString = repString + str(self.__keys[i]) + " " + str(self.__values[i]) + "\n"
        return repString

    def hashFunction(self, key):
        return (key * key * key) % self.__size

    def rehash(self, oldHash):
        return (oldHash + 1) % self.__size
