import numpy as np

f=open('breast-cancer-wisconsin.data', 'r')
f1=open('breast-cancer-wisconsin_.data', 'w')

for line in f.readlines():
	if('?' in line):
		continue
	else:
		f1.write(line)

f.close()
f1.close()
