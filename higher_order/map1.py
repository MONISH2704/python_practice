x=[]
x.append(int(input("enter a number: ")))
def square(x):
    return x**2
result=list(map(square,x))
print(result)