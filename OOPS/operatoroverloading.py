class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __str__ (self):
        return (f" {self.x}i + {self.y}j + {self.z}z")
    
    def __add__(self, i):
        return (f"{self.x+i.x}i {self.y+i.y}j {self.z + i.z}k")
    
vect = Vector(1,2,3)

vect2=Vector(4,5,6)

print(vect + vect2)