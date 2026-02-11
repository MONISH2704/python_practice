#variables and datatype
a=10
b=1.2
c="123"
d=True
print(type(a),type(b),type(c),type(d))

#control flow
performance=str(input("enter performance bad/good/excellent:"))
if performance=="bad":
    print("needs to improve more")
elif performance=="good":
    print("go through concepts")
elif performance=="excellent":
    print("perfect")
else:
    print("asses performance within bad/good/excellent")