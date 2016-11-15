#!/usr/bin/env python

myPaths2=["I:/Movies_AVI",
"I:/Movies_AVI/Handbraked",
"J:/Movie_AVIs"]

import os, sys, json, time


f1 = open("AVI-MPFiles.txt", "w")
f1.write("--=== AVI/MP3/MP4 Files" + " ")
f1.write(time.strftime("%d/%m/%Y"))
f1.write(" " + time.strftime("%H:%M:%S") + " ===--")
f1.write("\n" + "-----------------------------------------" + "\n")

for i in myPaths2:
    dirs = os.listdir( i )
    for file in dirs:
    	f1.write(i + " " + file + "\n");
    f1.write("\n" + "==*==*==*==*==*==*==*==*==*==" + "\n")	
f1.close()
