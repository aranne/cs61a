import threading

def thread_hello():
    other = threading.Thread(target=thread_say_hello, args=())    # create a new thread.
    other.start()                                                                               # run the new thread.
    thread_say_hello()

def thread_say_hello():
    print('hello from', threading.current_thread().name)

thread_hello()
