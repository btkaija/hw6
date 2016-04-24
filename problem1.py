#! /usr/bin/python
# ECE 2524 Homework 6 Problem 1 Ben Kaija

import sys

try:
	name = sys.argv[1]
except:
	sys.exit("insufficent file name argument")


try:
	f = open(name)
except:
	sys.exit("unable to open file: "+name)

lines = f.readlines()
f.close()

for l in lines:

	if "element vertex" in l:
		vert_line = l
		vert = int(vert_line[-2])
	if "element face" in l:
		face_line = l
		face = int(face_line[-2])

vert_count = 0
face_count = 0
end_header_pos = 0
for i in range(len(lines)):
	
	if "end_header" in lines[i]:
		end_header_pos = i

	split_line = lines[i].split(' ')

	if(len(split_line) == 3 and 0 != end_header_pos):
		vert_count = vert_count+1
	if(len(split_line) == 4 and 0 != end_header_pos):
		face_count = face_count+1



if vert_count != vert:
	print "PLY format error: "+str(vert)+" vertices are specified, but file contains "+str(vert_count)
elif face_count != face:
	print "PLY format error: "+str(face)+" vertices are specified, but file contains "+str(face_count)
else:
	print "Number of verticies = "+str(vert)
	print "Number of faces = "+str(face)