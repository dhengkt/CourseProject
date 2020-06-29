import queue
import tree

class Bank:

    def __init__(self, transactionFile):
        self.__transactionQueue = queue.Queue()
        self.__accounts = tree.BSTree()

        openFile = open(transactionFile, "r")
        for line in openFile:
            arr = line.split()
            if arr[0] != 'O' and len(arr[1]) == 5:
                if len(arr) == 2:
                    accountAndFundSpecifier = arr[1]
                    fund = accountAndFundSpecifier[4]
                    accountID = accountAndFundSpecifier[:4]
                    transaction = Transaction(arr[0], None, None, accountID, fund, None, None, None)
                    self.__transactionQueue.put(transaction)
                elif len(arr) == 3:
                    accountAndFundSpecifier = arr[1]
                    fund = accountAndFundSpecifier[4]
                    accountID = accountAndFundSpecifier[:4]
                    transaction = Transaction(arr[0], None, None, accountID, fund, arr[2], None, None)
                    self.__transactionQueue.put(transaction)
                else:
                    accountAndFundSpecifier = arr[1]
                    accountAndFundSpecifier2 = arr[3]
                    fund = accountAndFundSpecifier[4]
                    fund2 = accountAndFundSpecifier2[4]
                    accountID = accountAndFundSpecifier[:4]
                    accountID2 = accountAndFundSpecifier2[:4]
                    transaction = Transaction(arr[0], None, None, accountID, fund, arr[2], accountID2, fund2)
                    self.__transactionQueue.put(transaction)
            elif len(arr) == 2 and len(arr[1]) == 4:
                accountAndFundSpecifier = arr[1]
                accountID = accountAndFundSpecifier[:4]
                transaction = Transaction(arr[0], None, None, accountID, None, None, None, None)
                self.__transactionQueue.put(transaction)

            elif arr[0] == 'O':
                newAccount = Transaction(arr[0], arr[1], arr[2], int(arr[3]), None, None, None, None)
                self.__transactionQueue.put(newAccount)
            else:
                if len(arr) == 2:
                    transaction = Transaction(arr[0], None, None, None, arr[1], None, None, None)
                    self.__transactionQueue.put(transaction)
                elif len(arr) == 3:
                    transaction = Transaction(arr[0], None, None, arr[1], None, arr[2], None, None)
                    self.__transactionQueue.put(transaction)

    def getTransactionQueue(self):
        return self.__transactionQueue

    def execute(self):
        size = self.getTransactionQueue().qsize()
        for index in range(size):
            transaction = self.getTransactionQueue().get()
            if transaction.getTransactionType() == "O":
                newAccount = Account(transaction.getLastName(), transaction.getFirstName(), transaction.getAccountID())
                self.__accounts.put(transaction.getAccountID(), newAccount)

            elif transaction.getTransactionType() == "D":
                account = self.__accounts.searchTree(transaction.getAccountID())
                account.deposit(int(transaction.getAmount()))
                account.getFunds().addTransaction(transaction)

            elif transaction.getTransactionType() == "W":
                account = self.__accounts.searchTree(transaction.getAccountID())
                account.withdraw(int(transaction.getAmount()))
                account.getFunds().addTransaction(transaction)

            elif transaction.getTransactionType() == "T":
                account1 = self.__accounts.searchTree(transaction.getAccountID())
                account2 = self.__accounts.searchTree(transaction.getAccountID2())
                fund1 = transaction.getFundNumber()
                fund2 = transaction.getFundNumber2()
                self.transfer(account1, fund1, account2, fund2)
                account1.getFunds().addTransaction(transaction)
                account2.getFunds().addTransaction(transaction)
            else:
                if transaction.getFundNumber() is None:
                    account = self.__accounts.searchTree(transaction.getAccountID())
                    account.getFunds().printTransactions()
                else:
                    account = self.__accounts.searchTree(transaction.getAccountID())
                    account.getFunds().printTransactionsOnFund(account.getFundNumber())

    def transfer(self, account1, fund1, amount, account2, fund2):
        account1.withdraw(fund1, amount)
        account2.deposit(fund2, amount)

    def printResults(self):
        print("Process Done. Final Balances")
        self.__accounts.printInOrder()

class Transaction:

    def __init__(self, transactionType, lastName, firstName, accountId, fundNumber, \
                 amount, accountId2, fundNumber2):
        self.__transactionType = transactionType
        self.__lastName = lastName
        self.__firstName = firstName
        self.__accountId = accountId
        self.__fundNumber = fundNumber
        self.__amount = amount
        self.__accountId2 = accountId2
        self.__fundNumber2 = fundNumber2

    def getTransactionType(self):
        return self.__transactionType

    def getLastName(self):
        return self.__lastName

    def getFirstName(self):
        return self.__firstName

    def getAccountID(self):
        return self.__accountId

    def getFundNumber(self):
        return self.__fundNumber

    def getAmount(self):
        return self.__amount

    def getAccountID2(self):
        return self.__accountId2

    def getFundNumber2(self):
        return self.__fundNumber2

    def setTransactionType(self, transactionType):
        self.__transactionType = transactionType

    def setLastName(self, lastName):
        self.__lastName = lastName

    def setFirstName(self, firstName):
        self.__firstName = firstName

    def setID(self, accountId):
        self.__accountId = accountId

    def setFundNumber(self, fundNumber):
        self.__fundNumber = fundNumber

    def setAmount(self, amount):
        self.__amount = amount

    def setAccountID2(self, accountId2):
        self.__accountId2 = accountId2

    def __str__(self):
        if self.getTransactionType() == 'O':
            return "Transaction Type: Open Account, Last Name: " + str(self.getLastName()) \
                  + ", First Name: " + self.getFirstName() + ", Account ID: " + str(self.getAccountID())

        elif self.getTransactionType() == 'W':
            return "Transaction Type: Withdraw, Account ID " + str(self.getAccountID()) \
                   + ", Fund: " + str(self.getFundNumber()) + ", Amount Withdrawn: " + str(self.getAmount())

        elif self.getTransactionType() == 'D':
            return "Transaction Type: Deposit, Account ID " + str(self.getAccountID()) \
                   + ", Fund: " + str(self.getFundNumber()) + ", Amount Deposited: " + str(self.getAmount())

        elif self.getTransactionType() == 'H':
            return "Transaction Type: History, Account ID: " + str(self.getAccountID()) + ", Fund: " + str(self.getFundNumber())

        else:
            return "Transaction Type: Transfer, From Account ID: " + str(self.getAccountID()) \
                   + ", Fund: " + str(self.getFundNumber()) + ", Amount Transferred: " + str(self.getAmount()) \
                   + ", To Account Number: " + str(self.getAccountID2()) + ", Fund: " + str(self.getFundNumber2())


class Account:

    def __init__(self, lastName, firstName, accountId):
        if accountId < 1000 or accountId > 9999:
            print("Error: Account ID must be a four digit number between 1000 and 9999")
        self.__lastName = lastName
        self.__firstName = firstName
        self.__accountId = accountId
        monMark = Fund("Money Market", 0)
        primeMonMark = Fund("Prime Money Market", 0)
        longBond = Fund("Long-Term Bond", 0)
        shortBond = Fund("Short-Term Bond", 0)
        index = Fund("Index Fund", 0)
        capVal = Fund("Capital Value", 0)
        growthEq = Fund("Growth Equity", 0)
        growthInd = Fund("Growth Index Fund", 0)
        value = Fund("Value Fund", 0)
        valStockInd = Fund("Value Stock Fund", 0)
        self.__funds = [monMark, primeMonMark, longBond, shortBond, index, capVal, growthEq, growthInd, value, valStockInd]

    def getLastName(self):
        return self.__lastName

    def getFirstName(self):
        return self.__firstName

    def getID(self):
        return self.__accountId

    def getFunds(self):
        return self.__funds

    def getFund(self, index):
        return self.getFunds()[index]

    def setLastName(self, lastName):
        self.__lastName = lastName

    def setFirstName(self, firstName):
        self.__firstName = firstName

    def setID(self, accountId):
        if accountId < 1000 or accountId > 9999:
            print("ERROR: Account ID must be a four digit number between 1000 and 9999")
        self.__accountId = accountId

    def deposit(self, fund, amount):
        self.getFunds()[fund].addAmount(amount)

    def withdraw(self, fund, amount):
        if amount > self.getFunds()[fund].getAmount():
            if fund == 0:
                if self.getFunds()[1].getAmount() >= amount:
                    newAmount = amount - self.getFunds()[0].getAmount()
                    self.getFunds()[1].subtractAmount(newAmount)
                    self.getFunds()[0].addAmount(newAmount)
                    self.getFunds()[0].subtractAmount(amount)
                else:
                    print("ERROR: Cannot withdraw an amount greater than the fund balance")
            elif fund == 1:
                if self.getFunds()[0].getAmount() >= amount:
                    newAmount = amount - self.getFunds()[0].getAmount()
                    self.getFunds()[0].subtractAmount(newAmount)
                    self.getFunds()[1].addAmount(newAmount)
                    self.getFunds()[1].subtractAmount(amount)
                else:
                    print("ERROR: Cannot withdraw an amount greater than the fund balance")
            elif fund == 2:
                if self.getFunds()[3].getAmount() >= amount:
                    newAmount = amount - self.getFunds()[0].getAmount()
                    self.getFunds()[3].subtractAmount(newAmount)
                    self.getFunds()[2].addAmount(newAmount)
                    self.getFunds()[2].subtractAmount(amount)
                else:
                    print("ERROR: Cannot withdraw an amount greater than the fund balance")
            elif fund == 3:
                if self.getFunds()[2].getAmount() >= amount:
                    newAmount = amount - self.getFunds()[0].getAmount()
                    self.getFunds()[2].subtractAmount(newAmount)
                    self.getFunds()[3].addAmount(newAmount)
                    self.getFunds()[3].subtractAmount(amount)
                else:
                    print("ERROR: Cannot withdraw an amount greater than the fund balance")
            else:
                print("ERROR: Cannot withdraw an amount greater than the fund balance")

        else:
            self.getFunds()[fund].subtractAmount(amount)

    def __str__(self):
        result = str(self.__firstName) + " " + str(self.__lastName) + ", Account ID: " \
               + str(self.__accountId) + "\n"
        for i in range(len(self.getFunds())):
            result += str(self.getFunds()[i]) + "\n"
        return result

class Fund:

    def __init__(self, fundName, amount):
        self.__fundName = fundName
        self.__amount = amount
        self.__listOfTransactions = []

    def getFundName(self):
        return self.__fundName

    def getAmount(self):
        return self.__amount

    def getTransactions(self):
        return self.__listOfTransactions

    def setFundName(self, fundName):
        self.__fundName = fundName

    def setAmount(self, amount):
        self.__amount = amount

    def addAmount(self, amount):
        self.__amount += amount

    def subtractAmount(self, amount):
        self.__amount -= amount

    def addTransaction(self, transaction):
        self.__listOfTransactions.append(transaction)

    def printTransactions(self):
        for transaction in range(len(self.__listOfTransactions)):
            print(transaction)

    def printTransactionsOnFund(self, fund):
        for transactionIndex in range(len(self.getTransactions())):
            if fund == transactionIndex:
                print(transactionIndex)

    def __str__(self):
        return str(self.__fundName) + ": $" + str(self.__amount)


jollyBanker = Bank("BankTransIn.txt")
iters = jollyBanker.getTransactionQueue().qsize()
print(iters)
for i in range(iters):
    print(jollyBanker.getTransactionQueue().get())
jollyBanker.execute()
jollyBanker.printResults()
