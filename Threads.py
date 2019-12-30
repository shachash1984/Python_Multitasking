#! /usr/bin/python
from threading import Thread
import time


# TODO
# create two threads which are reading a file
# given in the 'args' argument
# each thread should read another file synchronously


def thread_example(*args):
    print("started sleeping for args={}...".format(args))
    time.sleep(4)
    print("ended sleeping for args={}...".format(args))


th1 = Thread(target=thread_example, args="1")
th2 = Thread(target=thread_example, args="2")

th1.start()
# th1.run()
th2.start()
# th2.run()

print("currently here")
th1.join()
print("thread 1 is done")

th2.join()
print("thread 2 is done")