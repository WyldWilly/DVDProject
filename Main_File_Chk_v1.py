#!/usr/bin/env python


import os, sys, json, time, errno, datetime

myPaths=["E:\\DVDTemp",
"G:\\DVDTemp",
"G:\\DVD_Storage",
"H:\\DVDTemp",
"I:\\DVD_Archives",
"J:\\DVD_Archives",
"Z:\\DVD_Hold",
"Z:\\DVD_Hold2",
"Z:\\DVD_Hold3"]

fo = open("DVD_Parsed.txt", "w")
# fo.write("--=== DVD Files" + " ")
# fo.write(time.strftime("%d/%m/%Y"))
# fo.write(" " + time.strftime("%H:%M:%S") + " ===--")
# fo.write("\n" + "-----------------------------------------" + "\n")

for i in myPaths:
	if os.path.exists(i):
		i = i + '\\'
		CAT = ''
		dirs = os.listdir( i )
		for file in dirs:
			#crtime = os.path.getmtime(i);
			created = str(os.path.getmtime(i));
			if 'DVD_' in file:
				TPF = 'DVD';
			else:
				TPF = 'NA';
			file = file.replace('DVD_' , '' , 1);
			fo.write(i);
			fo.write(',');
			fo.write(file);
			fo.write(',');
			fo.write(TPF)
			fo.write(',');
			fo.write(created);
			fo.write("\n");
	else:
			fo.write(i);
			fo.write(',');
			fo.write("unavailable");
			fo.write("\n");
			print(i + ' : Not Available' + '\n')

fo.close()
