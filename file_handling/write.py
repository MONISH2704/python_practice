f=open('new.txt','w')
modified=f.write("this is monish gowda")
print(modified)
f.close()

f=open('new.txt','r')
print(f.read())