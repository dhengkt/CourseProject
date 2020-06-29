import queue
import tree

FUND_TYPE = ["Money Market", "Prime Money Market", "Long-Term Bond", "Short-Term Bond", "500 Index Fund",
             "Capital Value Fund", "Growth Equity Fund", "Growth Index Fund", "Value Fund", "Value Stock Index"]


class Funds:
    def __init__(self, fundType):
        self.__fundType = FUND_TYPE[fundType]
        self.__balance = 0
        self.__fundHistory = []

    def getFundType(self):
        return self.__fundType

    def getBalance(self):
        return self.__balance

    def getFundHistory(self):
        return self.__fundHistory

    def setFundType(self, fundType):
        self.__fundType = fundType

    def setBalance(self, amount):
        self.__balance = amount

    def setFundHistory(self, history):
        self.__fundHistory = history

    def addFundHistory(self, history):
        self.__fundHistory.append(history)

    def printFundHistory(self):
        size = len(self.__fundHistory)
        if size != 0:
            for i in range(size):
                print(self.__fundHistory[i])

    def isEnough(self, amount):
        if self.__balance >= amount:
            return True
        else:
            return False

    def addMoney(self, amount):
        self.__balance += amount
        return True

    def subMoney(self, amount):
        if self.isEnough(amount):
            self.__balance -= amount
            return True
        else:
            return False

    def __str__(self):
        return "{}: ${}".format(self.getFundType(), self.getBalance())


class Transaction:
    def __init__(self, fileName):
        self.__fileName = fileName
        self.__tempAccounts = tree.BinarySearchTree()
        self.transacQueue = queue.Queue()

    def readFile(self):
        with open(self.__fileName, 'r') as fh:
            for line in fh:
                line = line.rstrip("\n")
                self.transacQueue.put(line)

        #for i in range(transaction.qsize()):
        #    string = transaction.get()
        #    print(string)

        fh.close()
        return True

    def Open(self, firstName, lastName, accountID):
        if self.__tempAccounts:
            return "ERROR Account " + accountID + " is already open. Transaction refused"
        else:
            newAccount = Account()
            self.__tempAccounts
            self.__tempAccounts.put(accountID, firstName + lastName)
            self.__tempAccounts[accountID].setFirstName(firstName)

    def displayAllHistory(self, accountID):
        temp = Account()
        self.__tempAccounts.Retrieve(accountID, temp)
        name = temp.getFirstName() + " " + temp.getLastName()
        print("Transaction History for " + name + " " + temp.getAccountID())

    def processTransaction(self):
        while not self.transacQueue.empty():
            tran = self.transacQueue.get()
            line = tran.split()
            tranType = line[0]
            if tranType == 'O':
                lastName = line[1]
                firstName = line[2]
                accountID = line[3][0:-1]
                self.Open(firstName, lastName, accountID)

            if tranType == 'D':
                accountID = line[1][0:-1]
                amount = line[2]
                fundID = line[1][-1]
                self.Deposit(accountID, fundID, amount, False)

            if tranType == 'W':
                neg = 0
                accountID = line[1][0:-1]
                amount = line[2]
                fundID = line[1][-1]
                self.Withdraw(accountID, amount, False, neg)
                if fundID == 2 and neg > 0:
                    amount = neg
                    neg = -1
                    self.Withdraw(amount, 3, amount, False, neg)
                elif fundID == 0 and neg > 0:
                    amount = neg
                    neg = -1
                    self.Withdraw(accountID, 1, amount, False, neg)
                elif fundID == 1 and neg > 0:
                    amount = neg
                    neg = -1
                    self.Withdraw(accountID, 0, amount, False, neg)
                elif fundID == 3 and neg > 0:
                    amount = neg
                    neg = -1
                    self.Withdraw(accountID, 2, amount, False, neg)

            if tranType == 'T':
                accountID = line[1][0:-1]
                fundID = line[1][-1]
                amount = line[2]
                targetID = line[3][0:-1]
                targetFund = line[3][-1]
                self.Transfer(accountID, fundID, amount, targetID, targetFund)

            if tranType == 'H':
                idNumber = line[1]
                if len(idNumber) > 4:
                    fundID = idNumber[-1]
                    accountID = idNumber[0:-1]
                    self.displayHistory(accountID, fundID)
                else:
                    accountID = line[1]
                    self.displayHistory(accountID)
    def Display(self):
        self.__tempAccounts.Display()



class Account:
    def __init__(self, firstName=None, lastName=None, accountID=None):
        self.__fName = firstName
        self.__lName = lastName
        self.__accountID = accountID
        self.__totalBalance = 0
        self.__error = False
        self.__funds = {}

        for i in range(10):
            self.__funds[i] = Funds(i)
            self.__funds[i].setBalance(0)

    def getFirstName(self):
        return self.__fName

    def getLastName(self):
        return self.__lName

    def getAccountID(self):
        return self.__accountID

    def getFunID(self):
        return

    def getTotalBalance(self):
        return self.__totalBalance

    def getError(self):
        return self.__error

    def getFundName(self, index):
        return self.__funds[index]

    def setFirstName(self, firstName):
        self.__fName = firstName

    def setLastName(self, lastName):
        self.__lName = lastName

    def setAccountID(self, accountID):
        self.__accountID = accountID

    def setTotalBalance(self):
        total = 0
        for i in range(10):
            total += self.__funds[i].getBalance()
        self.__totalBalance = total

    def setError(self, text):
        self.__error = text

    def displayFunds(self):
        for i in range(len(self.__funds)):
            print(self.getFundName(i))

    def addFundHistory(self, fundNumber, history):
        self.__funds[fundNumber].addFundHistory(history)

    def displayFundHistory(self, fundNumber):
        self.__funds[fundNumber].printFundHistory()

    def addTotalBalance(self, amount):
        self.__totalBalance += amount

    def addToFund(self, fundNumber, amount):
        self.__funds[fundNumber].addMoney(amount)

    def withdrawFromFund(self, fundNumber, amount):
        if self.__funds[fundNumber].getBalance() < amount:
            if self.__funds[0].getBalance() < amount and ((self.__funds[0].getBalance() + self.__funds[1].getBalance())
                                                          >= amount) and fundNumber == 0:
                temp = self.__funds[0].getBalance()
                self.__funds[0].setBalance(0)
                amount -= temp
                self.__funds[1].setBalance(self.__funds[1].getBalance() - amount)
            elif self.__funds[1].getBalance() < amount and (self.__funds[0].getBalance() + self.__funds[1].getBalance()
                                                            >= amount) and fundNumber == 1:
                temp = self.__funds[1].getBalance()
                self.__funds[1].setBalance(0)
                amount -= temp
                self.__funds[0].setBalance(self.__funds[0].getBalance() - amount)
            elif self.__funds[2].getBalance() < amount and (self.__funds[2].getBalance() + self.__funds[3].getBalance()
                                                            >= amount) and fundNumber == 2:
                temp = self.__funds[2].getBalance()
                self.__funds[2].setBalance(0)
                amount -= temp
                self.__funds[3].setBalance(self.__funds[3].getBalance() - amount)
            elif self.__funds[3].getBalance() < amount and (self.__funds[2].getBalance() + self.__funds[3].getBalance()
                                                            >= amount) and fundNumber == 3:
                temp = self.__funds[3].getBalance()
                self.__funds[3].setBalance(0)
                amount -= temp
                self.__funds[3].setBalance(self.__funds[2].getBalance() - amount)
            else:
                self.__error = True
                print("ERROR: Not enough funds to withdraw " + amount + " from ")
        else:
            self.__funds[fundNumber].subMoney(amount)

    def readFile(self, fileName):
        transaction = queue.Queue()
        with open(fileName, 'r') as fh:
            for line in fh:
                line = line.rstrip("\n")
                print(line)
                transaction.put(line)

        for i in range(transaction.qsize()):
            string = transaction.get()
            print(string)

        fh.close()

    def __str__(self):
        return "{} {} Account ID: {}".format(self.getFirstName(), self.getLastName(), self.getAccountID())

class Bank:
    def __init__(self, accTree=None):
        self.__accounts = []

    def getAccounts(self):
        return self.__accounts

    def setAccounts(self, accounts):
        self.__accounts = accounts

    def __contains__(self, item):
        if item in self.__accounts:
            return True
        else:
            return False
