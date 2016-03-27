#!/usr/bin/env python

Myfile = open("testfile.txt", "w")
Myfile.write("Hello World\n")
Myfile.write("another line \n")
Myfile.close()

Myfile = open('testfile.txt', 'r')
print (Myfile.readline())
