from functools import lru_cache
import time

@lru_cache(maxsize=None)       #memoisation
def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(4))
print("done for 4")


print(fx(12))
print("Done for 12")
print(fx(2))
print("done for 2")
print(fx(4))
print("done for 4")

