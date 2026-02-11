a={1,2,3,3,4}
b={3,4,5,6}
print(type(a))

#can be accesed only by loop
for i in range(len(a)):
    print(i)
#add element
a.add(7)
print(a)
#remove
a.remove(7)
print(a)
#set operations
#unioun
print("union:",a | b)
#intersection
print("intersection:",a & b)
#dufference
print("difference:",a-b)