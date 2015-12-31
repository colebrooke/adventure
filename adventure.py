#!/usr/bin/env python3

debug = 0 

import sqlite3 as sqlitedb
import sys
import os
import time
import fnmatch # this is for pattern matching files
import re # for regex string matching
import random # for battles and npc moves



os.system('cls')
os.system('clear')


conection = sqlitedb.connect('game.db')

def p(debugstring):
	if (debug == 1):
		print ("%s" % debugstring)

#conection.text_factory = str

def db(sqlstring):
	conection = sqlitedb.connect('game.db')

#---------------------------------------------------------
	with conection:
		cursor = conection.cursor()
		cursor.execute("%s" % sqlstring)
		row = cursor.fetchone()
		return ("%s" % (row))
		cursor.close()
#---------------------------------------------------------


def db_print_rows(sqlstring, colour='none'):
#---------------------------------------------------------
	with conection:
		cursor = conection.cursor()
		cursor.execute("%s" % sqlstring)
		#rows = cursor.fetchall()
		#return ("%s" % (rows))
		for row in cursor:
			if colour == 'none': print ("%s" % (row))
			if colour == 'yellow': print ('\033[1;33m%s\033[1;m' % (row))
			if colour == 'magenta': print ('\033[1;35m%s\033[1;m' % (row))
			if colour == 'grey': print ('\033[1;30m%s\033[1;m' % (row))
			if colour == 'bold': print ('\033[1;37m%s\033[1;m' % (row))
		cursor.close()
#---------------------------------------------------------

def db_print_rows_numbered(sqlstring):
#---------------------------------------------------------
	with conection:
		cursor = conection.cursor()
		cursor.execute("%s" % sqlstring)
		#rows = cursor.fetchall()
		#return ("%s" % (rows))
		a = 1
		for row in cursor:
			#print ("%s:" % (a))
			#a = a + 1
			#print ("%s" % (=row))
			#output = row[0]
			print ( "   ", row[0], " ", row[1])
			#print (row[1])
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


def db_query(sqlstring):
#---------------------------------------------------------
	with conection:
		cursor = conection.cursor()
		cursor.execute("%s" % sqlstring)
		rows = cursor.fetchall()
		#return rows
		cursor.close()

	# First need to convert each tuple in the list to a list within a list:
	row_list = [list(row) for row in rows ] 
	
	#This gets the length of the list of items:
	#print ("number of items: %s" % len(item_list) )

	# Now need to convert each list within the list to a normal string...
	for i, row_text in enumerate(row_list):
		row_list[i] = row_text[0]

	return row_list

#---------------------------------------------------------


def scroll(lines):
#----------------------------------------------------------------------
	for x in range (0, lines):
		print ("")
		time.sleep(0.1)
#----------------------------------------------------------------------


def print_current_room(userid):
#---------------------------------------------------------
	current_room = db("select location from user where userid=%s" % ( userid ))
	#print ("current location for this user is %s" % (current_room))
	#current_room = get_current_room ( userid )
	print ("")
	print ("*********************************************************************")
	print ("")

	# print room name...
	db_print_rows("select roomname from rooms where roomid=%s" % current_room, 'bold')
	print ("")
	time.sleep(0.3)

	# print room description...
	db_print_rows("select roomdesc from rooms where roomid=%s" % current_room, 'grey' )
	print ("")
	time.sleep(0.3)

	# print available routes to other rooms...
	db_print_rows("select route_desc from route where from_id=%s" % current_room )
	time.sleep(0.3)
	print ("")

	# print any NPCs that may be in the room...
	db_print_rows("select npcshortdesc from npc where npcroom=%s" % current_room, 'yellow' )
	print ("")
	time.sleep(0.3)

	# print any objects in the room
	#db_print_rows("select objectdesc_short from object where roomid=%s" % current_room )
	#print ("")
	#time.sleep(0.3)

	# print any items in the room, if they are not in the users inventory...
	db_print_rows(	"select itemdesc_short from item where currentroom = %s \
			and itemid not in ( select distinct itemid from inventory \
			where userid = %s ) order by static desc" % ( current_room, userid ), 'magenta')
	time.sleep(0.3)
#---------------------------------------------------------

def get_current_room( userid ):
#----------------------------------------------------------------------
	current_room = db("select location from user where userid=%s" % ( userid ))
	return current_room
#----------------------------------------------------------------------

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
		scroll (5)
		print_current_room( userid )

#	return (current_room,illegal)
#--------------------------------------------------------




def examine ():
#---------------------------------------------------------
	current_room = db("select location from user where userid=%s" % ( userid ))
	available_items = db_query("select lower(itemname) from item where currentroom=%s" % current_room )
#	available_objects = db_query("select lower(objectname) from object where roomid=%s" % current_room )
	available_npcs = db_query("select lower(npcname) from npc where npcroom =%s" % current_room )

	# strip the action term from the user input to leave the item your examining.
	if re.match (r'look at', userinput ):
		thing_to_examine = userinput.replace('look at ', '')
	else:
		thing_to_examine = userinput.replace('examine ', '')

	if thing_to_examine in available_items:
		print ("")
		print ("You examine the %s..." % thing_to_examine ) 
		time.sleep(1.3)
		print ("")
		db_print_rows("select itemdesc from item where lower(itemname)='%s'" % thing_to_examine)
		print ("")
		time.sleep(0.8)
#	elif thing_to_examine in available_objects:
#		print ("")
#		print ("You examine the %s..." % thing_to_examine )
#		time.sleep(1.3)
#		print ("")
#		db_print_rows("select objectdesc from object where lower(objectname)='%s'" % thing_to_examine)
	elif thing_to_examine in available_npcs:
		print ("")
		print ("You examine the %s..." % thing_to_examine )
		time.sleep(1.3)
		print ("")
		db_print_rows("select npclongdesc from npc where lower(npcname)='%s'" % thing_to_examine)
	
	else:
		print ("You can't do that.")

	


#---------------------------------------------------------

def inventory ():
#---------------------------------------------------------
	print ("You have the following items in your inventory:-")
	db_print_rows(	"select itemname from user as U join \
			inventory as I on U.userid=I.userid join \
			item as D on I.itemid=D.itemid \
			where I.userid=%s" % (userid))

#---------------------------------------------------------



def take ():
#---------------------------------------------------------
	current_room = db("select location from user where userid=%s" % ( userid ))
	available_items = db_return_rows("select itemname from item where currentroom=%s" % current_room )

	inventory = db_return_rows("select itemname from user as U join \
				inventory as I on U.userid=I.userid join \
				item as D on I.itemid=D.itemid \
				where I.userid=%s" % (userid))
	# For the inventory...
	# First need to convert each tuple in the list to a list within a list:
	inventory_list = [list(i) for i in inventory ] 
	
	# Now need to convert each list within the list to a normal string...
	for i, item_name in enumerate(inventory_list):
		inventory_list[i] = item_name[0]

	# For the items in the room...
	# First need to convert each tuple in the list to a list within a list:
	item_list = [list(i) for i in available_items ] 
	
	# Now need to convert each list within the list to a normal string...
	for i, item_name in enumerate(item_list):
		item_list[i] = item_name[0]

	# So that the list can be searched with the 'in' command...

	# strip the action term from the user input to leave the item you want to take.
	if re.match (r'take', userinput ):
		thing_to_take = userinput.replace('take ', '')
	elif re.match (r'pick up', userinput ):
		thing_to_take = userinput.replace('pick up ', '')
	elif re.match (r'get', userinput ):
		thing_to_take = userinput.replace('get ', '')
	if re.match (r'the', thing_to_take ):
		thing_to_take = thing_to_take.replace('the ', '')

	if thing_to_take in item_list:
		if thing_to_take in inventory_list:
			print ("The %s looks similar to one you already have." % thing_to_take )
			print ("You decide to leave it for another adventurer to find.")
		else:
			thing_to_take_id = db("select itemid from item where itemname = '%s'" % thing_to_take )
			item_is_static = db("select static from item where itemid = %s" % thing_to_take_id )
			if item_is_static == '1':
				print ("The %s is too heavy for you to take with you!" % thing_to_take )
			else:
				print ("You take the %s." % thing_to_take )
				db("insert into inventory (userid, itemid) values ( '%s', '%s' )" % (userid, thing_to_take_id) )	
	else:
		print ("You can't do that!")

#--------------------------------------------------------

def drop ():
#--------------------------------------------------------
	inventory = db_query("select itemname from user as U join \
				inventory as I on U.userid=I.userid join \
				item as D on I.itemid=D.itemid \
				where I.userid=%s" % (userid))
	if re.match (r'drop', userinput ):
		thing_to_drop = userinput.replace('drop ', '')
	elif re.match (r'put down', userinput ):
		thing_to_drop = userinput.replace('put down ', '')

	

	if thing_to_drop in inventory:
		print ("You drop the %s." % thing_to_drop )
		# find the id of the item...
		thing_to_drop_id = db("select itemid from item where itemname = '%s'" % thing_to_drop )
		# delete the item from our inventory...
		db("delete from inventory where userid = %s and itemid = %s" % (userid, thing_to_drop_id) )
		current_room = db("select location from user where userid=%s" % ( userid ))
		db("update item set currentroom = %s where itemid = %s" % (current_room, thing_to_drop_id) )	

	else:
		print ("You can't do that!")



def help ():
#--------------------------------------------------------
	print ( """

	You can enter a directiom in the form of:-
		
	N for North
	E for East 
	S for South
	W for West
	U for Up
	D for Down
		
	Other commands include:-
		
	Look around, look at, examine, where am I, take, drop, activate, use, 
	get, restart, score, quit, sleep, talk to, speak to, hit, kill,
	attack, save, load.

	""")

#-------------------------------------------------------

def talk ():
#-------------------------------------------------------
	current_room = db("select location from user where userid=%s" % ( userid ))
	available_npcs = db_query("select lower(npcname) from npc where npcroom =%s" % current_room )

	# strip the action term from the user input to leave the npc you're talking to...
	if re.match (r'talk to', userinput ):
		npc_to_talk_to = userinput.replace('talk to ', '')
	else:
		npc_to_talk_to = userinput.replace('speak to ', '')

	if npc_to_talk_to in available_npcs:
		print ("")
		print ("What do you want to say to the %s?" % npc_to_talk_to )
		time.sleep(1.3)
		print ("")
		# set the npcid we are talking to...
		npcid_to_talk_to = db("select npcid from npc where npcname = '%s' collate nocase" % ( npc_to_talk_to ))
		# print the possible questions...
		db_print_rows_numbered("select q_and_a_number, q_and_a_text from q_and_a \
					where q_and_a_npcid='%s' and q_and_a_type = 0" % npcid_to_talk_to)
		print ("")
		while True: 
			selection=input("Please Select an option: ")
			try:
				selected_question = int(selection)
			except ValueError:
				print("You must choose a number corrisponding to the choice above.")
			break
		answer = db(	"select q_and_a_link from q_and_a where q_and_a_npcid='%s' \
				and q_and_a_type = 0 and q_and_a_number='%s'" % (npcid_to_talk_to, selected_question))
		print ("")
		db_print_rows("select q_and_a_text from q_and_a where q_and_a_id='%s'" % answer )
		print ("")

	else:
		print ("You can't do that.")
#----------------------------------------------------------------------

def sleep ():
#---------------------------------------------------------------------
	current_room = db("select location from user where userid=%s" % ( userid ) )

	if current_room == 1:
		print ("You go to sleep for a while on the bed.")
	else:
		print ("You manage to sleep for a few minutes on the hard floor.")
	


def attack ():
#----------------------------------------------------------------------
	current_room = db("select location from user where userid=%s" % ( userid ) )
	available_npcs = db_query("select lower(npcname) from npc where npcroom =%s" % current_room )
	strength = db("select strength from user where userid=%s" % ( userid ) )
	# attack force will be a random int between 1 and 10,
	# multiplied by the player strength.
	# TODO: add in weapon strength.
	attack_force = (random.randint(1,10) * int(strength) )

	# strip the action term from the user input to leave The npc you're attacking...
	if re.match (r'^attack ', userinput ):
		npc_to_attack = userinput.replace('attack ', '')
	elif re.match (r'^kill ', userinput ):
		npc_to_attack = userinput.replace('kill ', '')
	elif re.match (r'^hit ', userinput ):
		npc_to_attack = userinput.replace('hit ', '')
	elif re.match (r'^shoot ', userinput ):
		npc_to_attack = userinput.replace('shoot ', '')
	
	# always strip out 'the' from the input string...
	if re.match (r'^the ', npc_to_attack ):
		npc_to_attack = npc_to_attack.replace('the ', '')

	print ("You move to attack the %s" % npc_to_attack )
	if npc_to_attack in available_npcs:
		# attack only viable if NPC is in the room...
		#print ("The %s is here, you try and attack!" % npc_to_attack )
		#print ("Your initial attack_force is ", attack_force )
		battle ( npc_to_attack )

	else:
		print ("The %s is nowhere to be seen, you can't attack!" % npc_to_attack )

	# see if we are trying to use a weapon...
	if re.match (r'with ', userinput ):
		# then try and strip out the npc to leave the weapon...
		weapon = re.match ( npc_to_attack , '')
		print ("Chosen weapon: %s" % weapon )


#---------------------------------------------------------------------




def battle ( npc ):
#---------------------------------------------------------------------
	strength = db("select strength from user where userid=%s" % ( userid ) )
	npc_strength = db("select npcstrength from npc where npcname like '%s'" % (npc) )

	# some temp variables whilst developing this feature
	my_weapon = 'fist'
	target_weapon = 'fist'
	
	while True:
		# get npc current health
		npc_health = db('select npchealth from npc where npcname like "%s"' % npc )

		# get player health
		user_health = db('select health from user where userid = %s' % userid )

		# calculate attack force, random int from 1 to 10, multipled by player strength, / 10
		attack_force = int(random.randint(1,10) * int(strength) / 10 )

		# same for npc attack force
		npc_attack_force = int(random.randint(1,10) * int(npc_strength) / 10 )

		print ("npc attack force", npc_attack_force)
		
		time.sleep(3)

		# display first attack description, from the user (type=0)
		db_print_rows('select action1 from battle where type=0 and level=%s' % attack_force )
		time.sleep(3)
		# display attack result...
		db_print_rows('select action2 from battle where type=0 and level=%s' % attack_force )
		time.sleep(3)
		# inflict damage on oponent...
		new_npc_health = ( int( npc_health ) - int ( attack_force ) )
		db('update npc set npchealth = %s where npcname like "%s"' % ( new_npc_health, npc ))
		# for debugging, print npc health...
		#print ('npc health:', npc_health )
		# if npc health is less than 0, the npc is killed...
		if int(new_npc_health) <= 0: 
			npc_dies (npc)		
			break
		# display first attack description, from npc (type=10)	
		db_print_rows('select action1 from battle where type=10 and level=%s' % int(npc_attack_force) )
		time.sleep(3)
		# display attack result...
		db_print_rows('select action2 from battle where type=10 and level=%s' % int(npc_attack_force) )
		time.sleep(3)
		# take damage given by npc...
		new_user_health = ( int( user_health ) - int ( npc_attack_force ) )
		db('update user set health = %s where userid = %s' % ( new_user_health, userid ))
		print("")
		# for debugging, display user health...
		#print ('user health:', new_user_health )
		if int(new_user_health) <= 0: 
			user_dies()		
			break

		print ('Do you want to continue the battle?')
		print ("""1.  Continue the battle! 2.  Admit defeat and run away!""")

		run = 0
		while True: 
			selection=input("Enter your choice: ") 
			if selection =='1':
				print ('You brace yourself to continue the battle!') 
				break
			elif selection == '2':
				print ('You decide to run away.  Oh dear. You find you are routed to the spot!')
				run = 1
				break

		if run == 1: break


	
def user_dies ():
#----------------------------------------------------------------------
	print ('You have been killed! Your stats will be reset, and you will be returned to the start of the game.')
	db('update user set health = 100, location = 1 where userid = %s' % userid )
	#db('update user set location = 1 where userid = %s' % userid )
	time.sleep(3)
	# TODO clear inventory
	print_current_room ( userid )
	

def npc_dies ( npc ):
#----------------------------------------------------------------------
	print ('You have killed the %s!' % npc )
	time.sleep(3)
	print_current_room ( userid )



def look ():
#----------------------------------------------------------------------
	print_current_room( userid )
#----------------------------------------------------------------------

#======================================================================


print ("----------------------------------------")
print ("  Welcome to the -Adventure- game ")
print ("----------------------------------------")
print ("""
   1  Log in an exsiting adventurer
   2  Create a new adventurer
   3  See who is online
   4  Exit
""")
while True: 
	selection=input("Please Select an option: ") 
	if selection =='1': 
		#userid=input("Enter your user ID: ")
		username=input("Enter your username: ")
		userid = db("select userid from user where name='%s' collate nocase" % username)
		if userid != 'None':
			break
		elif userid == 'None':
			print("Not a valid username.  Returning to menu.")
	elif selection == '2': 
		username=input("Enter your firstname / login name: ")
		checkuser = db("select name from user where name='%s' collate nocase" % username)
		if checkuser == username:
			print("There is already a user with that name!")
		if username == '':
			print("Not a valid username.  Returning to menu.")
			break
		else :
			db("insert into user (name, score, location, health, strength, userdesc, moves) \
				values ( '%s', '0', '1', '100', '10', '', '0' )" % username )
			print("Created a new user.  You can now log in.")
	
	elif selection == '3':
		print ("Feature not available yet!")
	elif selection == '4': 
		print ("Thanks for playing!")
		print ("")
		sys.exit()
	else: 
		print ("Unknown Option Selected!")




#username = db("select name from user where userid=%s" % userid)

#print ("Your username is -- %s" % db("select name from user where userid=%s" % userid))
#print (" Your userid is -- %s" % userid)



time.sleep(0.5)


# Set up various game variables not in db???
current_room = get_current_room ( userid )
illegal_move = 0

# This is the main loop of the game...
print_current_room( userid )

loop = 1
while loop == 1 :
	print ("")
	moves = db("select moves from user where userid=%s" % userid )
	p ("DEBUG: your userid %s and your total moves are %s" % (userid, moves))


	#print ('\033[1;37m%s\033[1;m'	
	userinput=input('\033[0;37mWhat do you want to do? \033[0;m').lower()


	# Version1 direction interpretation	
	if   (userinput == "n") or (userinput == "north"): move ( "n", userid )
	elif (userinput == "e") or (userinput == "east"): direction = "e"; move ( direction, userid )
	elif (userinput == "s") or (userinput == "south"): direction = "s"; move ( direction, userid )
	elif (userinput == "w") or (userinput == "west"): direction = "w"; move ( direction, userid )
	elif (userinput == "u") or (userinput == "up"): direction = "u"; move ( direction, userid )
	elif (userinput == "d") or (userinput == "down"): direction = "d"; move ( direction, userid )
	elif (userinput == "se") or (userinput == "south east"): direction = "se"; move ( direction, userid )

	# Inventory
	elif (userinput == "i") or (userinput == "inventory"): inventory ()

	# Take / Pick up
	elif 	re.match ( r'^take', userinput ) or \
		re.match ( r'^pick up', userinput ) or \
		re.match ( r'^get', userinput ): take ()		

	# Drop / Put down
	elif 	re.match ( r'^drop', userinput ) or \
		re.match ( r'^put down', userinput ): drop ()

	# Examine
	elif re.match ( r'^examine', userinput ) or re.match ( r'^look at', userinput ): examine ()

	# Look
	elif (userinput == "look"): look ()	

	# Talk
	elif 	re.match ( r'^talk to', userinput ) or \
		re.match ( r'speak to', userinput ): talk ()

	# Sleep
	elif re.match ( r'^sleep', userinput ):
		sleep ()

	# Help
	elif (userinput == "help"): help ()

	# Attack
	elif	re.match (r'^attack', userinput ) or \
		re.match (r'^kill', userinput ) or \
		re.match (r'^hit', userinput ) or \
		re.match (r'^shoot', userinput ):	attack ()

	# Exit
	elif (userinput == "exit") or (userinput == "quit"):
		print ("Thanks for playing!")
		sys.exit()


	# end of user input interpretation
	#-----------------------------------------------------------------------------------------
	# Fall through
	else :
		print ("I don't understand that input. Try again!")
	
		


	time.sleep(0.5)


	
	
	
	# inventory query:
	# select itemname from user as U join inventory as I on U.userid=I.userid join item as D on I.itemid=D.itemid
	
print ("THE END")	
