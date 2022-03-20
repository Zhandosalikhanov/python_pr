class MyClass:
    def getString(self):
        self.name = input("Enter your name: ")

    def printString(self):
        print("What is your name? Don't tell me, I know it! " + self.name + " :)")

if __name__ == "__main__":
    aFunc = MyClass()
    aFunc.getString()
    aFunc.printString()