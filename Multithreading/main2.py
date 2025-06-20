from concurrent.futures import ThreadPoolExecutor
import time
import threading

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

def poolingdemo():
    with ThreadPoolExecutor() as Executor:
        future= Executor.submit(sec,4)
        print(future.result(sec,2))
    with ThreadPoolExecutor() as Executor:
        future= Executor.submit(sec,2)
        print(future.result(sec,2))
    with ThreadPoolExecutor() as Executor:
        future= Executor.submit(sec,1)
        print(future.result(sec,1))

poolingdemo()