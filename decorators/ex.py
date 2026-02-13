def decor(func):
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")
    return wrapper

def original():
    print("you are monish")

a=decor(original)
a()