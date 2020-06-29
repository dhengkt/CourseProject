import bank

test = bank.Transaction("BankTransIn.txt")
test.readFile()
test.processTransaction()