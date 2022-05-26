import threading
import concurrent.futures
import time

start=time.perf_counter()
def do_something(seconds):
    print(f'Sleeping {seconds} second')
    time.sleep(seconds)
    print('Done Sleeping')
    return ('Done')
with concurrent.futures.ThreadPoolExecutor() as executor:
    results=[executor.submit(do_something,3) for _ in range(13)]
finish=time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s)")