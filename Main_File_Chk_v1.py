#!/usr/bin/env python


import os, sys, json, time, errno

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
		# print(i + ' : Available' + '\n')
		i = i + '\\'
		dirs = os.listdir( i )
		for file in dirs:
			# fo.write(i + " " + file + "\n");
			#print(i + ' : Available' + '\n')
			#fileFIXED = file.lstrip('DVD_')
			file = file.replace('DVD_' , '' , 1);
			fo.write(i);
			fo.write(',');
			fo.write(file);
			fo.write("\n");
	else:
			fo.write(i);
			fo.write(',');
			fo.write("unavailable");
			fo.write("\n");
			print(i + ' : Not Available' + '\n')

fo.close()
