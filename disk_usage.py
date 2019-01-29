#!/usr/local/bin/python3.7
#Python script to check disk utilization on linux

import os
#import system

directory = input("please enter the directory...")
files = os.listdir(directory)

for m in files:
    fullpath = directory + "/" + m
    if os.path.isfile(fullpath):
        hrfilesize = os.path.getsize(fullpath) / 1024
        print(m),(hrfilesize)
