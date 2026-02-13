from functools import reduce

marks=[60,50,40,90,80]
def divide(a):
    return a/10


def distinction(b):
    if b>7:
        return b
    


def sum(a,b):
    return a*b

mapped=list(map(divide,marks))
filtered=list(filter(distinction,mapped))
print("the final answer is : ",reduce(sum,filtered))
print(marks)

