class encaps:
    def __init__(self,bal):
        self.__balance=bal
    def get_balance(self):
        print("the balance is :",self.__balance)
    def set_balance(self,amt):
        self.__balance+=amt
a=encaps(500)
a.get_balance()
a.set_balance(100)
a.get_balance()