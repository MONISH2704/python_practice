class father:
    def __init__(self,hair,skin):
        self.hair=hair
        self.skin=skin
    def display(self):
        print(f"father hair color: {self.hair}")
        print(f"father skin color: {self.skin}")
class son(father):
    def __init__(self,hair,skin,height):
        super().__init__(hair,skin)
        self.height=height
    def display_height(self):
        print(f"son height: {self.height}")
s=son("black","brown",5)
s.display()
s.display_height()