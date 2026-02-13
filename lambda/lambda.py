def add(a,b):
       num=lambda a,b : a+b 
       num(a,b)
       return num(a,b)
       
print(add(2,3))
print((lambda x: x**2)(5))

divide=lambda a,b : a/b
print(divide(10,2))

guess = lambda a,b : a if a>=10 else b
print(guess(1,20))