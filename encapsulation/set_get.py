class encaps:
    def __init__(self):
        self.__balance=100
    def get_balance(self):
        print("the balance is :",self.__balance)
    def set_balance(self,amt):
        self.__balance+=amt
a=encaps()
a.get_balance()
a.set_balance(100)
a.get_balance()