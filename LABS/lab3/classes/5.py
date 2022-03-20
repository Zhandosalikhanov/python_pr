class Kaspi_kz:
    def __init__(create, name, initial_bal):
        create.name = name
        create.balance = initial_bal

    def Owner(self):
        print("This is", self.name + "'s account")

    def Moy_bank(self):
        print("You have", self.balance, "tenge left")

    def Depozit(self, income):
        self.balance += income
        print("+" + str(income), "tenge.", "Current balance is:", self.balance)

    def Withdraw(self, take):
        if self.balance - take > 0:
            self.balance -= take
            print("You withdrawed", take, "tenge")
            print("Money left:", self.balance)
        else:
            print("Not enough money for", '-' + str(take), "operation.", take - self.balance, "tenge required to do the operation")

if __name__ == "__main__":
    zhakes_acc = Kaspi_kz("Zhandos", 10000)
    zhakes_acc.Owner()
    print()
    zhakes_acc.Moy_bank()
    print()
    zhakes_acc.Depozit(5000)
    print()
    zhakes_acc.Withdraw(16000)