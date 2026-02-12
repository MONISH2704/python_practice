class parent:
    def display(self):
        print("this is parent")
class child(parent):
    def display(self):
        print("this is child")
a=child()
a.display()