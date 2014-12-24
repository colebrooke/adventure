#!/bin/bash

if [ -a './game.db' ]; 
	then read -p "Existing game.db, do you want to remove? " -n 1 -r
	echo
	if [[ $REPLY =~ ^[Yy]$ ]];
	then
		rm ./game.db
	fi
fi
echo "Creating new database file with sqlite3...."
sqlite3 game.db < game.sql
echo "Done."


