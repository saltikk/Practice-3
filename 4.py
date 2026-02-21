class StringHandler :
    def getString(self):
        self.txt = input()

    def printString(self):
        print(self.txt.upper())


handler = StringHandler()

handler.getString()
handler.printString()
