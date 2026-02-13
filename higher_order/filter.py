num=[1,2,3,4,5,6]
def even_num(num):
    if num %2==0:
        return num
def square (even):
    return even**2
even=list(filter(even_num,num))
res=list(map(square,even))
print("even no: ",even)
print("result:c",res)