#!/usr/bin/python

from multiprocessing import  Process
import time

# TODO
# create multiple processes
# which read a file and calculate a hash of the file content
# then they write the result to an output file
# use python hash function:
# hash("123123")


def test(*args):
    print("running from process: {}".format(args))
    time.sleep(2)


def hash_file(*args):
    args = "".join(args)
    content = ""
    with open(args, 'r') as f:
        content = f.read()
        print(content)
    output_file = "hashed_"+str(args)
    with open(output_file, 'w') as o:
        o.write(str(hash(content)))


p1 = Process(target=test, args='1')
p2 = Process(target=test, args='2')
p1.run()
p2.run()

p3 = Process(target=hash_file, args='first.cs')
p4 = Process(target=hash_file, args='second.cs')
p3.run()
p4.run()
