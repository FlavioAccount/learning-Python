#Multitasking concepts
#When we are running a program we already have one thread
import threading
import time

#First make a thread
def func(y):
    print("ran")
    time.sleep(1)
    print("Done!")

x = threading.Thread(target=func, args=(4,)) #target='name of the function' args='tuple'
x.start()

print(threading.active_count())