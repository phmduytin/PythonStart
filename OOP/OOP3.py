class BankAccount:
    rate = 0.0 #class variqble

    @staticmethod
    def setInterestRate(newRate):
        BankAccount.rate = newRate


bankAccount1 = BankAccount()
bankAccount2 = BankAccount()

BankAccount.setInterestRate(0.01)
print(BankAccount.rate)

BankAccount.setInterestRate(0.02)

print(bankAccount1.rate)
print(bankAccount2.rate)



