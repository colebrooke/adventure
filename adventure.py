#!/usr/bin/python3

debug = 0 

import sqlite3 as sqlitedb
import sys
import os
import time
import fnmatch # this is for pattern matching files
import re # for regex string matching


os.system('cls')
os.system('clear')

def p(debugstring):
	if (debug == 1):
		print ("%s" % debugstring)



conection = sqlitedb.connect('game.db')
#conection.text_factory = str
# this function sets up the datebase connection.
def db(sqlstring):
#---------------------------------------------------------
	with conection:
		cursor = conection.cursor()
		cursor.execute("%s" % sqlstring)
		row = cursor.fetchone()
		return ("%s" % (row))
		cursor.close()
#---------------------------------------------------------

def db_print_rows(sqlstring):
#---------------------------------------------------------
	with conection:
		cursor = conection.cursor()
		cursor.execute("%s" % sqlstring)
		#rows = cursor.fetchall()
		#return ("%s" % (rows))
		for row in cursor:
			print ("%s" % (row))
		cursor.close()
#---------------------------------------------------------

def db_return_rows(sqlstring):
#---------------------------------------------------------
	with conection:
		cursor = conection.cursor()
		cursor.execute("%s" % sqlstring)
		row = cursor.fetchall()
		return row
		cursor.close()
#---------------------------------------------------------



def print_current_room(userid):
#---------------------------------------------------------
	print ("userid in print_current_room is %s" % (userid))
	current_room = db("select location from user where userid=%s" % ( userid ))
	print ("current location for this user is %s" % (current_room))
	#current_room = get_current_room ( userid )
	print ("")
	print ("*********************************************************************")
	print ("")
	print ( db("select roomname from rooms where roomid=%s" % current_room ))
	print ("")
	print ( db("select roomdesc from rooms where roomid=%s" % current_room ))
	print ("")
	db_print_rows("select route_desc from route where from_id=%s" % current_room )
	#for row in result:
	#	print ("%s" % row )
	#print (" >> ", end="")
	db_print_rows("select objectdesc_short from object where roomid=%s" % current_room )
	print ("")
	#print (" >>> ", end="")
	db_print_rows("select itemdesc_short from item where currentroom=%s" % current_room )

#---------------------------------------------------------

def move( direction, userid ):
#---------------------------------------------------------
	room = get_current_room ( userid )
	p("current room %s " % room)
	p("chosen direciton %s " % direction)
	p("userid %s " % userid)
	#illegal = 0
	next_room = db("select to_id from route where from_id=%s and direction='%s'" % ( room, direction ))
	p ("next room query result: %s " % next_room )
	#time.sleep(3)	
#	current_room = next_room

	if (next_room == "None") or (not next_room):
		#current_room = room
		#illegal = 1
		print("You can't go in that direction!")
	else:
		# add one to the user moves 
		db("update user set moves = moves + 1 where userid = %s" % ( userid ))
		# set the users current location in the db
		db("update user set location = %s where userid = %s" % ( next_room, userid ))
		# print the room description for the user
		print_current_room( userid )

#	return (current_room,illegal)
#--------------------------------------------------------



def get_current_room( userid ):
	current_room = db("select location from user where userid=%s" % ( userid ))
	return current_room




def examine ():
#---------------------------------------------------------
	current_room = db("select location from user where userid=%s" % ( userid ))
	available_items = db_return_rows("select itemname from item where currentroom=%s" % current_room )
	available_objects = db_return_rows("select objectdesc_short from object where roomid=%s" % current_room )

	# strip the action term from the user input to leave the item your examining.
	thing_to_examine = userinput.replace('examine ', '')

	# First need to convert each tuple in the list to a list within a list:
	item_list = [list(i) for i in available_items ] 
	
	#This gets the length of the list of items:
	#print ("number of items: %s" % len(item_list) )

	# Now need to convert each list within the list to a normal string...
	for i, item_name in enumerate(item_list):
		item_list[i] = item_name[0]

	# So that the list can be searched with the 'in' command...
	if thing_to_examine in item_list:
		print ("")
		print ("You examine the %s..." % thing_to_examine ) 
		time.sleep(1.3)
		print ("")
		db_print_rows("select itemdesc from item where itemname='%s'" % thing_to_examine)
		print ("")
		time.sleep(0.8)
	else:
		print ("You can't do that.")
#---------------------------------------------------------


def look ():
	print_current_room( userid )













print ("-------------------------------------------------")
print ("  Welcome to Justin & Jensens NEW Adventure game ")
print ("-------------------------------------------------")
print ("")

userid=input("Enter your user ID: ")

username = db("select name from user where userid=%s" % userid)

print ("Your username is -- %s" % db("select name from user where userid=%s" % userid))


time.sleep(0.5)


# Set up various game variables not in db???
current_room = get_current_room ( userid )
illegal_move = 0

# This is the main loop of the game...
print_current_room( userid )

loop = 1
while loop == 1 :
	print ("")
	#print ("illegal move = %s" % (illegal_move))
	#if (illegal_move == 0):	
	#print ("----current_room=%s" % (get_current_room (userid)))
	#if (illegal_move == 1):
	#print ("-----You can't move in that direction!")
	
	#print (db("select roomdesc from rooms where roomid=%s" % current_room ))
	#if (illegal_move == 0):	
	moves = db("select moves from user where userid=%s" % userid )
	p ("DEBUG: your userid %s and your total moves are %s" % (userid, moves))


	
	userinput=input('Which direction do you want to go? ').lower()


	# Version1 direction interpretation	
	if (userinput == "n") or (userinput == "north"): move ( "n", userid )
	elif (userinput == "e") or (userinput == "east"): direction = "e"; move ( direction, userid )
	elif (userinput == "s") or (userinput == "south"): direction = "s"; move ( direction, userid )
	elif (userinput == "w") or (userinput == "west"): direction = "w"; move ( direction, userid )
	elif (userinput == "u") or (userinput == "up"): direction = "u"; move ( direction, userid )
	elif (userinput == "d") or (userinput == "down"): direction = "d"; move ( direction, userid )
	elif (userinput == "se") or (userinput == "south east"): direction = "se"; move ( direction, userid )

	# Inventory
	elif (userinput == "i") or (userinput == "inventory"): 
		db_print_rows("select itemname from user as U join inventory as I on U.userid=I.userid join item as D on I.itemid=D.itemid where I.userid=%s" % (userid))
	
	# Examine
	elif re.match ( r'^examine', userinput ):
		#print ("You examine that but don't notice anything special.")
		examine ()

	# Look
	elif (userinput == "look"): look ()	

	else :
		print ("I don't understand that input. Try again!")
	
		


	time.sleep(0.5)


	
	
	
	# inventory query:
	# select itemname from user as U join inventory as I on U.userid=I.userid join item as D on I.itemid=D.itemid
	
print ("THE END")	
