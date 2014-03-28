#!/usr/bin/python3

import re



userinput=input("Enter your text: ")


print ("You entered %s " % userinput)

examine = re.match ( r'^examine', userinput )

if examine: 
	print ("matched!")

else:
	print ("no")



