try:

    num=int(input("enter num: "))
    a=100/num
    

except ZeroDivisionError:
    print("cannot divide by zero")
else:
    print(a)
finally:
    print("program exit")