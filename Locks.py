#!/usr/bin/python
from threading import Lock, Thread
import copy
import time

lock = Lock()

global g_stocks
g_stocks = []


def add_stock():
    global g_stocks
    # get a lock
    lock.acquire()
    time.sleep(0.25)
    g_stocks.append('1')
    # release a lock
    lock.release()


def read_stocks():
    global g_stocks
    lock.acquire()
    current_stocks = copy.copy(g_stocks)
    lock.release()
    print(current_stocks)
    return current_stocks


for i in range(1, 10):
    th1 = Thread(target=add_stock)
    th1.start()

    th2 = Thread(target=read_stocks)
    th2.start()


def read_file():
    file_name = "first.cs"
    lock.acquire()
    with open(file_name, 'r') as f:
        print(f.read())
    lock.release()


for i in range(1, 100):
    th1 = Thread(target=read_file)
    th1.start()