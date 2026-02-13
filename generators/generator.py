def generate():
    i=1
    while i>=1:
        yield i
        i+=1
a=generate()
print(next(a))
print((a))
print((a))