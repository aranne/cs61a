import threading
from time import sleep

counter = [0]

def increment():
    count = counter[0]
    sleep(0) # try to force a switch to the other thread
    counter[0] = count + 1

other = threading.Thread(target=increment, args=())
other.start()
increment()
print('count is now: ', counter[0])  # sometimes the counter[0] is 1, sometimes is 2.

"""This problem arises only in the presence of shared data that may be mutated by one thread while another thread accesses it."""
