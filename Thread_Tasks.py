import time
import threading

def display_nums ():
    for i in range (1,6):
        print ("Number :", i)
        time.sleep(2)

def display_sq():
    for i in range (1,6):
        print ("Squares :", i*i)
        time.sleep(2)

def display_mess ():
    for i in range(1,6):
        print("Python Thread :", i)
        time.sleep(2)

t1 = threading.Thread(target = display_nums)
t2 = threading.Thread(target = display_sq)
t3 = threading.Thread(target = display_mess)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print ("all tasks done")