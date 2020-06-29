# This class represents a rational number. That is one that can be represented by an integer
# numerator and integer denominator.
# The key math

class Rational:
    def __init__(self, numerator = 0, denominator = 1):
        if denominator == 0:
            self.__numerator = 0
            self.__denominator = 1
        else:
            self.__numerator = numerator
            self.__denominator = denominator
        self.simplify()

    # Reduces fraction to simplest form
    def simplify(self):
        gcd = 1
        for i in range(1, min(abs(self.__numerator), abs(self.__denominator)) + 1):
            if not self.__numerator % i and not self.__denominator % i:
                gcd = i
        self.__numerator = self.__numerator // gcd
        self.__denominator = self.__denominator // gcd

    # Getters/Setters
    def getNumerator(self):
        return self.__numerator

    def getDenominator(self):
        return self.__denominator

    def setNumerator(self, numerator):
        self.__numerator = numerator
        self.simplify()
        return True

    def setDenominator(self, denominator):
        if denominator != 0:
            self.__denominator = denominator
            self.simplify()
            return True
        else:
            return False

    # Overload arithmetic operations
    def __mul__(self, rhs):
        tempRat = Rational()
        tempRat.setNumerator(self.getNumerator() * rhs.getNumerator())
        tempRat.setDenominator(self.getDenominator() * rhs.getDenominator())
        return tempRat

    def __add__(self, rhs):
        tempRat = Rational()
        tempRat.setNumerator((self.getNumerator() * rhs.getDenominator()) + (rhs.getNumerator() * self.getDenominator()))
        tempRat.setDenominator(self.getDenominator() * rhs.getDenominator())
        return tempRat

    def __sub__(self, rhs):
        tempRat = Rational()
        tempRat.setNumerator((self.getNumerator() * rhs.getDenominator()) - (rhs.getNumerator() * self.getDenominator()))
        tempRat.setDenominator(self.getDenominator() * rhs.getDenominator())
        return tempRat

    def __truediv__(self, rhs):
        tempRat = Rational()
        tempRat.setNumerator(self.getNumerator() * rhs.getDenominator())
        tempRat.setDenominator(self.getDenominator() * rhs.getNumerator())
        return tempRat

    #Comparators
    def __eq__(self, rhs):
        if self.getDenominator() == rhs.getDenominator() and self.getNumerator() == rhs.getNumerator():
            return True
        else:
            return False

    def __ne__(self, rhs):
        if self == rhs:
            return False
        else:
            return True

    def __str__(self):
        return str(self.__numerator) + "/" + str(self.__denominator)
