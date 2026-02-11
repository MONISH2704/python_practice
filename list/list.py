num = [10,11,12,13]
print(num)

#append
num.append(14)
print("append:",num)
#insert
num.insert(0,9)
print("insert:",num)
#remove
num.remove(12)
print("after removinf 12:",num)
#pop
num.pop()
print("after pap:",num)
#sort
num.sort()
print("sorted num:",num)
#reverse
num.reverse()
print("reversed:",num)
#length
print("length of num:",len(num))
#place
print("index of 10:",num.index(10))
#for loop
print ("for loop:")
for i in range(len(num)):
    print(num[i])
#list repetation
print("repeatation:",num*2)