#parallel processing

import threading
import time

def sec(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

time1=time.perf_counter()
sec(4)
sec(2)
sec(1)

Th1=threading.Thread(target=sec, args=[4])
Th2=threading.Thread(target=sec, args=[2])
Th3=threading.Thread(target=sec, args=[1])
time2=time.perf_counter()
Th1.start()
Th2.start()
Th3.start()

print(time2 - time1)