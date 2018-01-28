#import random
#n = 0

#a = ['this is definitely a string,', 'not an integer.']

# Flip Flop Test:

x = 1

for i in range(6):
	if (x == 1):
		x = 2
	else:
		x = 1
	#print (x)

#argv test
import sys

y = sys.argv

for i in range(1,len(y)):
	print y[i]