student = {"name":"monish","age":21}

print("name of student :",student.get("name"))
#adding key-value
student["city"]="bengaluru"
print(student)
#updating
student["age"]=20
print(student)#deleting
print(student.pop("city"))
#obtain keys
print(student.keys())
#obtain values
print(student.values())
#otaining key & value
print(student.items())
#using for loop
for k in student:
    (print(k))
for v in student:
    print(v)

