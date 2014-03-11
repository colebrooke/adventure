#!/usr/bin/python3

import sqlite3 as sqlitedb
import sys
import os
import time
import fnmatch # this is for pattern matching files
import re # for regex string matching


os.system('cls')
os.system('clear')




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

def db_rows(sqlstring):
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


def print_current_room(userid):
#---------------------------------------------------------
	current_room = get_current_room ( userid )
	print ("")
	print ( db("select roomname from rooms where roomid=%s" % current_room ))
	print ("")
	print ( db("select roomdesc from rooms where roomid=%s" % current_room ))
	print ("")
	db_rows("select route_desc from route where from_id=%s" % current_room )
	#for row in result:
	#	print ("%s" % row )
	print (" >>> ", end="")
	db_rows("select itemdesc2 from item where currentroom=%s" % current_room )
	print ("")
#---------------------------------------------------------

def move( room, direction, userid ):
	illegal = 0
	next_room = db("select to_id from route where from_id=%s and direction='%s'" % ( room, direction ))
	print ("next room : %s " % next_room )
	time.sleep(3)	
	current_room = next_room

	if (current_room == "None"):
		current_room = room
		illegal = 1
		print("You can't move in that direction!")
	else:
		# add one to the user moves 
		db("update user set moves = moves + 1 where userid = %s" % ( userid ))
		# set the users current location in the db
		db("update user set location = %s where userid = %s" % ( current_room, userid ))
	return (current_room,illegal)


def get_current_room( userid ):
	current_room = db("select location from user where userid=%s" % ( userid ))
	return current_room

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

loop = 1
while loop == 1 :
	print ("")
	print ("illegal move = %s" % (illegal_move))
	if (illegal_move == 0):	
		print ("----current_room=%s" % (get_current_room (userid)))
	if (illegal_move == 1):
		print ("-----You can't move in that direction!")
	
	#print (db("select roomdesc from rooms where roomid=%s" % current_room ))
	if (illegal_move == 0):	
		print_current_room( current_room )
		moves = db("select moves from user where userid=%s" % userid )
		print ("DEBUG: your userid %s and your total moves are %s" % (userid, moves))


	
	userinput=input('Which direction do you want to go? ').lower()


	# Version1 direction interpretation	
	if (userinput == "n") or (userinput == "north"): direction = "n"; move ( current_room, direction, userid )
	elif (userinput == "e") or (userinput == "east"): direction = "e"; current_room, illegal_move=move ( current_room, direction, userid )
	elif (userinput == "s") or (userinput == "south"): direction = "s"; move ( current_room, direction, userid )
	elif (userinput == "w") or (userinput == "west"): direction = "w"; current_room, illegal_move=move ( current_room, direction, userid )
	elif (userinput == "u") or (userinput == "up"): direction = "u"; current_room, illegal_move=move ( current_room, direction, userid )
	elif (userinput == "d") or (userinput == "down"): direction = "d"; current_room, illegal_move=move ( current_room, direction, userid )
	elif (userinput == "se") or (userinput == "south east"): direction = "se"; current_room, illegal_move=move ( current_room, direction, userid )

	# Inventory
	elif (userinput == "i") or (userinput == "inventory"): 
		db_rows("select itemname from user as U join inventory as I on U.userid=I.userid join item as D on I.itemid=D.itemid where I.userid=%s" % (userid))
	else :
		print ("I don't understand that input. Try again!")
	
		


	time.sleep(0.5)


	
	
	
	# inventory query:
	# select itemname from user as U join inventory as I on U.userid=I.userid join item as D on I.itemid=D.itemid
	
print ("THE END")	
