class Account:
    def __init__(self, owner, balance):
        self.o = owner
        self.b = balance

    def deposit(self, amount):
        self.b += amount
        print("Your new balance is: {}".format(self.b))

    def withdraw(self, w_amount):
        if w_amount > self.b:
            print("You don't have such money on your bank account")
        else:
            self.b -= w_amount
        print("Your balance: {}".format(self.b))


bank_account = Account("Daniyal", 7000)
bank_account.withdraw(400)
bank_account.deposit(7000000)
# bank_account.withdraw(7000000)
# bank_account.withdraw(6600)
# bank_account.withdraw(6600)
