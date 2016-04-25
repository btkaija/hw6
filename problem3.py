#! /usr/bin/python
# ECE 2524 Homework 6 Problem 3 Ben Kaija

import sys
from collections import namedtuple
from operator import attrgetter
Item = namedtuple("Item", "item_id descrip qty_1 qty_10 floor whse")

#error checking crap...
try:
	d_f = sys.argv[1]
	c_f = sys.argv[2]
except:
	sys.exit("insufficent or unsupported arguments")
try:
	cmd_file = open(c_f)
except:
	sys.exit("unable to open file: "+c_f)
try:
	data_file = open(d_f)
except:
	sys.exit("unable to open file: "+d_f)

#parsing data file
data_lines = data_file.readlines()
inventory_data = []
for l in data_lines:
	i = l.split('\t')
	#remove spaces
	i = [x.strip() for x in i if x]
	#separate into new Item objects
	if len(i) == 6 and i[0] != "ItemID":
		new_item = Item(i[0], i[1], float(i[2]), float(i[3]), int(i[4]), int(i[5]))
		inventory_data.append(new_item)

def _sort(data, field):
	sort_field = ''
	
	if field == "ItemID":
		data = sorted(data, key=attrgetter('item_id'))
	elif field == "Description":
		data = sorted(data, key=attrgetter('descrip'))
	elif field == "Quantity1":
		data = sorted(data, key=attrgetter('qty_1'))
	elif field == "Quantity10":
		data = sorted(data, key=attrgetter('qty_10'))
	elif field == "Floor":
		data = sorted(data, key=attrgetter('floor'))
	elif field == "Warehouse":
		data = sorted(data, key=attrgetter('whse'))
	else:
		sys.exit("the field: "+field+" is not a valid sort key")

	return data



def _dump(data):
	inventory_data = data

	print "ItemID  Description                        Qty 1   Qty 10   Floor    Whse"
	print "-------------------------------------------Price----Price---Stock---Stock"
	for d in inventory_data:
		print "{0:6}".format(d.item_id) + ' ',
		print "{0:30}".format(d.descrip) + ' ',
		print "{0:8}".format(d.qty_1) + ' ',
		print "{0:7}".format(d.qty_10) + ' ',
		print "{0:6}".format(d.floor) + ' ',
		print "{0:6}".format(d.whse)

def _add(data, line):
	print line
	new_item = Item(line[0], line[1], line[2], line[3], line[4], line[5])
	data.append(new_item)
	return data

def _del(data, item_id):
	for d in data:
		if d.item_id == item_id:
			pos = data.index(d)
			del data[pos]
			return data



#parsing cmd file
cmd_lines = cmd_file.readlines()

has_not_sorted = True

for l in cmd_lines:
	args = l.split('\t')
	args = [x.strip() for x in args if x]
	print args
	if "dump" == args[0]:
		#print "do dump command"
		if has_not_sorted:
			inventory_data = _sort(inventory_data, "ItemID")
		_dump(inventory_data)

	elif "sort" == args[0]:
		has_not_sorted = False
		#print "do sort command"
		inventory_data = _sort(inventory_data, args[1])

	elif "add" == args[0]:
		#print "do add command"
		inventory_data = _add(inventory_data, args[1:])

	elif "del" == args[0]:
		#print "do del command"
		inventory_data = _del(inventory_data, args[1])

	else:
		sys.exit(l+" is not a valid command")


