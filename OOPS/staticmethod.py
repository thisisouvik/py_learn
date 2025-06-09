class Math:
    def __init__(self,num):
        self.num= num
    def addtonum(self,addnum):
        self.num= self.num + addnum
    
    @staticmethod
    def add(a,b):
        return a+b
    
a= Math(5)
print(a.num)
a.addtonum(6)
print(a.num)
print(Math.add(1,7))
