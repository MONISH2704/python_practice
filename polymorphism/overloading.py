class addition:
    def add(self,a,b=0,c=0):
        if b==0 and c==0:
            print("there is only one number ",a)
        elif(b!=0 and c==0):
            print("the sum of two numbers is ",a+b)
        else:
            print("the sum of three numbers is ",a+b+c)
a=addition()
a.add(5,10,15)
