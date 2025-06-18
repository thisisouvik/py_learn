import time
print(time.time())

def loopfor():
    for i in range(5):
        print(i)

loopfor()
init=time.time()
T1=time.time() - init
print(T1)

print(4)
time.sleep(3)
print("After 3 sec")

t=time.localtime()
formated_time=time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formated_time)