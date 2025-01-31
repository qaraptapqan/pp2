class Scanner:
    def getString(self):
        self.txt = input()
    def printString(self):
        print(self.txt.upper())

scanner = Scanner()

scanner.getString()
scanner.printString()
