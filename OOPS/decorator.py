#Decorator
def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks")
    return mfx

@greet
def hello():
    print("Hello World")

hello() 