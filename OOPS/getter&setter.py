class MyClass:
    def __init__(self,value):
        self._value=value

    def show(self):
        print(f"Return my {self._value} value")
    
    @property
    def ten_value(self):
        return self._value
    
    @ten_value.setter
    def ten_value(self,new_value):
        self._value= new_value/10
    
    
obj = MyClass(10)
obj.ten_value= 67
print(obj.ten_value)
obj.show()

    