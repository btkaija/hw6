#! /usr/bin/python
# ECE 2524 Homework 6 Problem 2 Ben Kaija

import sys

try:
	name = sys.argv[1]
	scale = float(sys.argv[2])
except:
	sys.exit("insufficent or unsupported arguments")

try:
	infile = open(name)
except:
	sys.exit("unable to open file: "+name)

lines = infile.readlines()
infile.close()

begin_scale = False

for l in lines:
	nums = l.split(' ')
	if len(nums) == 4:
		begin_scale = False

	if begin_scale:
		
		for x in nums:
			print scale*float(x),
		print
		
	else:
		print l,
	

	if ("end_header" in l):
		begin_scale = True




