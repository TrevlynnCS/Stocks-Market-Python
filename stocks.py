#!/usr/bin/env python3
#Trevlynn Galvis 

import requests
import sys
import re 

url = 'http://tophat.sunywcc.edu/~smiller/stock.py'
trevi = open("trevistocks.txt", "w")
trevi.write("Symbol\tPrice\tHigh\tLow\tRatio\tRec\t\n")
s = sys.argv[1:]

if len(sys.argv) < 2:
	print("You need to have atleast one argument", file=sys.stderr)
	exit(2)
else:
	for symbol in s:
		r = requests.get(url, {'ticker':symbol})
		sym =re.split("\n|\t",r.text)
		if sym[2]=='Unknown symbol':
			print("Error Processing:",symbol,file=sys.stderr)
			error=1
			pass
		else:
			curPrice= float(sym[9])
			avgRec= (float(sym[13])+ float(sym[15]))/2
			if curPrice < avgRec:
				rec="S"
			else:
				rec="B"
			print("Processing: \t", sym[5])
			trevi.write(sym[3]+"\t" + sym[9]+"\t" + sym[13]+"\t" + sym[15]+"\t" + sym[17]+"\t" + rec +"\n" )
			error=0
	trevi.close()
	trevi2= open("trevistocks.txt", "r")
	message = trevi2.read()
	print(message)
	trevi2.close()	
if error==1:
	exit(3)	
