# In class practice on 04/08/2019

SUITS = ("spade", "club", "heart", "diamond")
NUM_CARDS_IN_SUIT = 13

class Card:
    def __init__(self, value = 1, suit = None):
        if value < 1 or value > NUM_CARDS_IN_SUIT:
            self.__value = 1
        else:
            self.__value = value

        if suit not in SUITS:
            self.__suit = SUITS[0]
        else:
            self.__suit = suit

    def getSuit(self):
        return self.__suit

    def getValue(self):
        return self.__value

    def printDetails(self):
        if self.__value == 1:
            print("Ace of " + self.__suit)
        elif self.__value == 11:
            print("Jack of " + self.__suit)
        elif self.__value == 12:
            print("Queen of " + self.__suit)
        elif self.__value == 13:
            print("King of " + self.__suit)
        else:
            print(str(self.__value) + " of " + self.__suit)


class Deck:
    def __init__(self):
        self.__deck = []
        for value in range(1, NUM_CARDS_IN_SUIT+1):
            for suit in SUITS:
                card = Card(value, suit)
                self.__deck.append(card)

    def printDetails(self):
        for card in self.__deck:
            card.printDetails()