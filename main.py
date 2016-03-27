#!/usr/bin/env python

myPaths=["E:/DVDTemp/",
"G:/DVDTemp/",
"G:/DVD_Storage/",
"H:/DVDTemp/",
"I:/DVD_Archives/",
"J:/DVD_Archives/",
"Z:/DVD_Hold/"]

import os, sys

for i in myPaths:
    dirs = os.listdir( i )
    for file in dirs:
        print (i,file)