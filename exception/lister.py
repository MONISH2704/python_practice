try:
    a=[1,2,3]
    print(a[1])
except IndexError:
    print("there are only ",len(a)," elements")
finally:
    print("program exit")