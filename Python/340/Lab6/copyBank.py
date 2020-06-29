import queue
import tree

FUND_TYPE = ["Money Market", "Prime Money Market", "Long-Term Bond", "Short-Term Bond", "500 Index Fund",
             "Capital Value Fund", "Growth Equity Fund", "Growth Index Fund", "Value Fund", "Value Stock Index"]


class Bank:
    def __init__(self, fileName):
        self.__transQueue = queue.Queue()
        self.__accounts = tree.BinarySearchTree()
        with open(fileName, 'r') as fh:
            for line in fh:
                line = line.rstrip("\n")
                self.__transQueue.put(line)
        for i in range(self.__transQueue.qsize()):
            temp = self.__transQueue.get()
            print(temp)

        fh.close()

    def processTransaction(self):
        while not self.__transQueue.empty():
            trans = self.__transQueue.get()
            line = trans.split()
            tranType = line[0]
            if tranType == 'O':
                fName = line[1]
                lName = line[2]
                fullID = line[3]
                accountID = fullID[0:-1]
                account = Account(fName, lName, accountID)
                if self.__accounts.find(accountID):
                    print("ERROR: Account: {} is already open. Transferal refused.".format(accountID))
            elif tranType == 'D':
                fullID = line[1]
                accountID = fullID[0:-1]
                fundID = fullID[-1]
                amount = line[2]
                account = self.__accounts.get(accountID)
                account.deposit(fundID, amount)
                line = Transaction(tranType, None, None, accountID, fundID, amount, None, None)
                account.addTransaction(line, fundID)
            elif tranType == 'W':
                fullID = line[1]
                accountID = fullID[0:-1]
                fundID = fullID[-1]
                amount = line[2]
                account = self.__accounts.get(accountID)
                line = Transaction(tranType, None, None, accountID, fundID, amount, None, None)
                if account.withdraw(fundID, amount):
                    line.setCheck(True)
                else:
                    line.setCheck(False)
                    print("ERROR: Not enough funds to withdraw {} from {} {} {}".format(line.getAmount(),
                                                                                        line.getFirstName(),
                                                                                        line.getLastName(),
                                                                                        line.getFundID()))
                if not account.getCheck():
                    account.addTransaction(line, fundID)
            elif tranType == 'T':
                fullID = line[1]
                accountID = fullID[0:-1]
                fundID = fullID[-1]
                amount = line[2]
                targetFullID = line[3]
                targetID = targetFullID[0:-1]
                targetFund = targetFullID[-1]
                account = self.__accounts.get(accountID)
                tarAccount = self.__accounts.get(targetID)
                line = Transaction(tranType, None, None, accountID, fundID, amount, targetID, targetFund)
                if self.__accounts.find(accountID):
                    if self.__accounts.find(targetID):
                        if account.withdraw(fundID, amount):
                            tarAccount.deposit(targetFund, amount)
                            account.addTransaction(line, accountID)
                            tarAccount.addTransaction(line, targetFund)
                        else:
                            print("ERROR: Unsufficent Funds to conduct transfer. From account number: {} fund: "
                                  "{} to account number: {} fund: {} from the amount of: {}".format(accountID,
                                                                                                    str(accountID.getFund(fundID)),
                                                                                                    targetID,
                                                                                                    str(tarAccount.getFund(targetFund)),
                                                                                                    amount))
                    else:
                        print("ERROR: Account: {} not found. Transferal refused".format(accountID))
                else:
                    print("ERROR: Account: {} not found. Transferal refused".format(accountID))
            elif tranType == 'H':
                fullID = line[1]
                if len(fullID) == 4:
                    account = self.__accounts.get(fullID)
                    print("Transaction History For: {} {}".format(account.getFirstName(),
                                                                  account.getLastName()))
                    account.displayFullHistory()
                elif len(fullID) == 5:
                    accountID = fullID[0:-1]
                    account = self.__acounts.get(accountID)
                    print("Transaction History For: {} {}".format(account.getFirstName(),
                                                                  account.getLastName()))
                    account.displayFundHistory()
                else:
                    print("ERROR: Account: {} not found.".format(accountID))
        self.__transQueue.get()

    def getTransQueue(self):
        return self.__transQueue

    def printResults(self):
        print("Process Done. Final Balances")
        self.__accounts.printInOrder()

class Fund:
    def __init__(self, fundType, amount):
        self.__fundType = fundType
        self.__balance = amount
        self.__history = []

    def getFundType(self):
        return self.__fundType

    def getBalance(self):
        return self.__balance

    def getHistory(self):
        return self.__history

    def setFundType(self, fundType):
        self.__fundType = fundType

    def setBalance(self, amount):
        self.__balance = amount

    def addMoney(self, amount):
        self.__balance += amount

    def subMoney(self, amount):
        self.__balance -= amount

    def addHistory(self, transaction):
        self.__history.append(transaction)

    def displayHistory(self):
        if len(self.__history) != 0:
            print("{}: ${}".format(self.getFundType(), self.getBalance()))
            for history in self.__history:
                print(history)

    def isEnough(self, amount):
        if self.__balance >= amount:
            return True
        else:
            return False

    def __str__(self):
        return "{}: ${}".format(self.getFundType(), self.getBalance())


class Account:
    def __init__(self, fName, lName, accountID):
        if accountID < 1000 or accountID > 9999:
            print("ERROR: Account ID must ba a four digit number between 1000 and 9999")
        self.__lastName = lName
        self.__firstName = fName
        self.__accountID = accountID
        self.__funds = []
        self.__check = False

        # Create 10 funds automatically
        for i in range(10):
            temp = Fund(FUND_TYPE[i], 0)
            self.__funds.append(temp)

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getAccountID(self):
        return self.__accountID

    def getAllFunds(self):
        return self.__funds

    def getFund(self, index):
        return self.__funds[index]

    def getCheck(self):
        return self.__check

    def setFirstName(self, fName):
        self.__firstName = fName

    def setLastName(self, lName):
        self.__lastName = lName

    def setAccountID(self, accountID):
        if accountID < 1000 or accountID > 9999:
            print("ERROR: Account ID must ba a four digit number between 1000 and 9999")
        else:
            self.__accountID = accountID

    def deposit(self, fund, amount):
        self.__funds[fund].addMoney(amount)

    def withdraw(self, fund, amount):
        if self.__funds[fund].isEnough(amount):
            self.__funds[fund].subMoney(amount)
            return True
        if 0 <= fund <= 3:
            if fund == 0:
                if self.__funds[fund].getBalance() + self.__funds[1].getBalance() >= amount:
                    left = amount - self.__funds[fund].getBalance()
                    self.__funds[fund].subMoney(amount - left)
                    self.__funds[1].subMoney(left)
                    first = Transaction('W', None, None, self.getAccountID(), fund, amount - left, None, None)
                    second = Transaction('W', None, None, self.getAccountID(), 1, left, None, None)
                    self.__funds[fund].addHistory(first)
                    self.__funds[1].addHistory(second)
                    self.__check = True
                    return True
                elif fund == 1:
                    if self.__funds[fund].getBalance() + self.__funds[0].getBalance() >= amount:
                        left = amount - self.__funds[fund].getBalance()
                        self.__funds[fund].subMoney(amount - left)
                        self.__funds[1].subMoney(left)
                        first = Transaction('W', None, None, self.getAccountID(), fund, amount - left, None, None)
                        second = Transaction('W', None, None, self.getAccountID(),  0, left, None, None)
                        self.__funds[fund].addHistory(first)
                        self.__funds[0].addHistory(second)
                        self.__check = True
                        return True
                elif fund == 2:
                    if self.__funds[fund].getBalance() + self.__funds[fund + 1].getBalance() >= amount:
                        left = amount - self.__funds[fund].getBalance()
                        self.__funds[fund].subMoney(amount - left)
                        self.__funds[3].subMoney(left)
                        first = Transaction('W', None, None, self.getAccountID(), fund, amount - left, None, None)
                        second = Transaction('W', None, None, self.getAccountID(),  3, left, None, None)
                        self.__funds[fund].addHistory(first)
                        self.__funds[3].addHistory(second)
                        self.__check = True
                        return True
                elif fund == 3:
                    if self.__funds[fund].getBalance() + self.__funds[fund - 1].getBalance() >= amount:
                        left = amount - self.__funds[fund].getBalance()
                        self.__funds[fund].subMoney(amount - left)
                        self.__funds[2].subMoney(left)
                        first = Transaction('W', None, None, self.getAccountID(), fund, amount - left, None, None)
                        second = Transaction('W', None, None, self.getAccountID(),  2, left, None, None)
                        self.__funds[fund].addHistory(first)
                        self.__funds[2].addHistory(second)
                        self.__check = True
                        return True
        else:
            return False

    def displayFundsBalance(self):
        for i in range(10):
            print(f"{self.__funds[i]}: ${self.__funds[i].getBalance()}")

    def displayFundHistory(self, fundID):
        self.__funds[fundID].displayHistory()

    def addTransaction(self, trans, fundID):
        self.__funds[fundID].addHistory(trans)

    def __str__(self):
        return "{} {}, Account ID: {}".format(self.getFirstName(),
                                              self.getLastName(),
                                              self.getAccountID())

class Transaction:
    def __init__(self, transType, fName, lName, accountID, fundID, amount, targetID, targetFundID):
        self.__transType = transType
        self.__lastName = lName
        self.__firstName = fName
        self.__accountID = accountID
        self.__fundID = fundID
        self.__amount = amount
        self.__targetID = targetID
        self.__targetFundID = targetFundID
        self.__check = True

    def getTransType(self):
        return self.__transType

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getAccountID(self):
        return self.__accountID

    def getFundID(self):
        return self.__fundID

    def getAmount(self):
        return self.__amount

    def getTargetID(self):
        return self.__targetID

    def getTargetFundID(self):
        return self.__targetFundID

    def getCheck(self):
        return self.__check

    def setTransType(self, transType):
        self.__transType = transType

    def setFirstName(self, fName):
        self.__firstName = fName

    def setLastName(self, lName):
        self.__lastName = lName

    def setFundID(self, fundID):
        self.__fundID = fundID

    def setAmount(self, amount):
        self.__amount = amount

    def setTargetID(self, targetID):
        self.__targetID = targetID

    def setTargetFundID(self, targetFundID):
        self.__targetFundID = targetFundID

    def setCheck(self, statement):
        self.__check = statement
        return True

    def __str__(self):
        if self.getTransType() == 'D' or self.getTransType() == 'W':
            return "{} {} {}".format(self.getTransType(),
                                     str(self.getAccountID()) + str(self.getFundID()),
                                     self.getAmount())
        elif self.getTransType() == 'T':
            return "{} {} {} {}".format(self.getTransType(),
                                        str(self.getAccountID()) + str(self.getFundID()),
                                        self.getAmount(),
                                        str(self.getTargetID()) + str(self.getTargetFundID()))