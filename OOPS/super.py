class Parentclass:
    def parent_method(self):
        print("This is parent class")
class childclass(Parentclass):
    def parent_method(self):
        print("Hello")
        super().parent_method()
    def child_method(self):
        print("This is child class")
        super().parent_method()

e=childclass()
e.child_method()
e.parent_method()