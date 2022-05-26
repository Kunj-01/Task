import os
import threading
import time

# def fun(m):
#     # print(threading.current_thread(),os.getpid())
#     for i in range(10):
#         print("Cube",m*m*m)

# t1 = threading.Thread(target=fun,args=(5,))
# t2 = threading.Thread(target=fun,args=(2,))

# t1.start()
# t2.start()

# t1.join()
# t1.join()

def thread(n):
    # time.sleep(5)
    # print(threading.active_count())
    # print(threading.enumerate())
    thread_lock.acquire()
    thread1(n)
    thread_lock.release()
    # print(threading.current_thread(),os.getpid())


def thread1(n):
    for i in range(n):
        print(threading.current_thread())
    # time.sleep(7)
    # print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.current_thread(),os.getpid())

thread_lock = threading.Lock()

t1 = threading.Thread(target=thread, args=[10])
t2 = threading.Thread(target=thread, args=[10])
start = time.perf_counter()
t1.start()
t2.start()

print(time.perf_counter()-start)
t1.join()
print(time.perf_counter()-start)
t2.join()
print(time.perf_counter()-start)
