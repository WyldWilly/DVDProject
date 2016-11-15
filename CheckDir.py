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

import os, sys, json, time, errno

for i in myPaths:
	if os.path.exists( i )
		print "%s exists!" % ( i )
	else:
		print "%s Not Found!" % ( i)