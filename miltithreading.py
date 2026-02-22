# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from APIs
#                  threading. Thread(target=my_function)

import threading
import time

def walk_dog():
    time.sleep(8)
    print("You finished walking the dog")

def take_out_thresh():
    time.sleep(2)
    print("You take out the trash")

def get_email():
    time.sleep(4)
    print("You get the mail")
print("Whithout multitasking: ---------------------------")
walk_dog()
take_out_thresh()
get_email()

#We can accomplishe all the tasks on the same time
print("With multitasking: ----------------------------")
chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))# Accessing the threading module, .Thread to access the constructor
chore1.start() #Use the start() method

chore2 = threading.Thread(target=take_out_thresh)
chore2.start()

chore3 = threading.Thread(target=get_email)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

