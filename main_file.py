#!/usr/bin/env python

myPaths=["E:/DVDTemp/",
"G:/DVDTemp/",
"G:/DVD_Storage/",
"H:/DVDTemp/",
"I:/DVD_Archives/",
"J:/DVD_Archives/",
"Z:/DVD_Hold/",
"Z:/DVD_Hold2",
"Z:/DVD_Hold3"]

import os, sys, json, time

fo = open("DVDs.txt", "w")
fo.write("--=== DVD Files" + " ")
fo.write(time.strftime("%d/%m/%Y"))
fo.write(" " + time.strftime("%H:%M:%S") + " ===--")
fo.write("\n" + "-----------------------------------------" + "\n")


for i in myPaths:
    dirs = os.listdir( i )
    for file in dirs:
    	fo.write(i + " " + file + "\n");
    fo.write("\n" + "==*==*==*==*==*==*==*==*==*==" + "\n")	
fo.close()

