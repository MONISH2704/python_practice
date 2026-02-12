class student:
    def __init__(self):
        self.name=input("enter name: ")
        self.rollno=int(input("enter roll no: "))
    def display(self):
        print(f"student name: {self.name}")
        print(f"student roll no: {self.rollno}")
s=student()
s.display()
