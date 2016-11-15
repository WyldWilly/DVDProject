#!/usr/bin/env python


import os, sys, json, time, errno

var1 = 100
if var1:
   print ("1 - Got a true expression value")
   print (var1)
else:
   print ("1 - Got a false expression value")
   print (var1)

var2 = 0
if var2:
   print ("2 - Got a true expression value")
   print (var2)
else:
   print ("2 - Got a false expression value")
   print (var2)

print ("Good bye!" + "\n --------------\n")

cwd = os.getcwd()
print(cwd + "\n --------------\n")


# AD="E:\\"
# BD="MySQL"

# path = os.path.join("E:\\","MySQL")
# path = os.path.join(AD, BD)
# if os.path.exists(path):
#	print(path + ' : exists')
#	if os.path.isdir(path):
#		print(path + ' : is a directory')


myPaths=["E:\\DVDTemp",
"G:\\DVDTemp",
"G:\\DVD_Storage",
"H:\\DVDTemp",
"Z:\\DVD_Hold",
"Z:\\DVD_Hold2",
"Z:\\DVD_Hold3",
"I:\\DVD_Archives",
"J:\\DVD_Archives"]

fo = open("DVDs.txt", "w")
fo.write("--=== DVD Files" + " ")
fo.write(time.strftime("%d/%m/%Y"))
fo.write(" " + time.strftime("%H:%M:%S") + " ===--")
fo.write("\n" + "-----------------------------------------" + "\n")

for i in myPaths:
	if os.path.exists(i):
		print(i + ' : Available' + '\n')
		i = i + '\\'
	    dirs = os.listdir( i )
	    for file in dirs:
	    	fo.write(i + " " + file + "\n");
	    fo.write("\n" + "==*==*==*==*==*==*==*==*==*==" + "\n")	
	else:
		print(i + ' : Not Available' + '\n')
		fo.write("\n" + "==*==*==*==*==*==*==*==*==*==" + "\n")
		fo.write("==*==*==*==*" + i + " Not Available ==*==*==*==*==*==" + "\n")		

fo.close()