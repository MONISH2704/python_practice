def maths(func):
    def calculate(a,b):
        print("before calculation")
        func(a,b)
        print("after calculation")
    return calculate

#decorator
@maths
def add(a,b):
    print(a+b)
add(2,3)
