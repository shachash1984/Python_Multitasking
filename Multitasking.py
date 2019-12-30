#! /usr/bin/python
import os
import subprocess


def get_time():
    res = os.popen("time/t")
    for line in res:
        print(line)


def write_to_shell():
    # writes shell command
    # os.system("cd")
    path = "E:\\Coding Projects\PythonProjects\Multitasking"
    output_file = path + "\\dir_output.txt"
    temp = open(output_file, "w")
    temp.close()

    exit_code = os.system("E:\\Coding Projects\PythonProjects\Multitasking\dir > {}".format(output_file))

    if exit_code == 0:
        f = open(output_file, "r")
        print(f.read())


def std_out_example():
    try:
        proc = os.popen("dir 2>1")
        for line in proc:
            print(line, "1111")
    except Exception as e:
        print("Failed running popen")
    #proc = subprocess.run("<<shell command>>")

std_out_example()
#write_to_shell()

get_time()
