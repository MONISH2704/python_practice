#reading
f=open('abc.txt')
print(f.read())
f.close()

print("using readline")
f=open('abc.txt')
print(f.readline())
f.close()


print("using readlines")
f=open('abc.txt')
print(f.readlines())
f.close()