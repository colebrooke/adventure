PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "inventory" (
    "inventid" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "userid" INTEGER NOT NULL,
    "itemid" INTEGER NOT NULL
);
INSERT INTO "inventory" VALUES(7,2,2);
INSERT INTO "inventory" VALUES(9,4,3);
INSERT INTO "inventory" VALUES(12,2,1);
INSERT INTO "inventory" VALUES(13,2,3);
INSERT INTO "inventory" VALUES(16,1,3);
CREATE TABLE `q_and_a` (
	`q_and_a_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`q_and_a_npcid`	INTEGER,
	`q_and_a_text`	TEXT,
	`q_and_a_number`	INTEGER,
	`q_and_a_type`	INTEGER,
	`q_and_a_level`	INTEGER,
	`q_and_a_link`	INTEGER,
	`q_and_a_trigger`	INTEGER
);
INSERT INTO "q_and_a" VALUES(1,1,'Excuse me, could you tell me where to find the nearest shop?',1,0,1,2,NULL);
INSERT INTO "q_and_a" VALUES(2,1,'The old man looks blankly at you.  He says "I''m sure I saw
a shop around here somewhere."
',NULL,1,1,NULL,NULL);
INSERT INTO "q_and_a" VALUES(3,1,'Hi, I''ve recently arrived on this planet, can you tell me anything about this place?',2,0,1,4,NULL);
INSERT INTO "q_and_a" VALUES(4,1,'The old man says "This planet has many places to explore.  But be careful. 
There are gangs here you don''t want to mess with."',NULL,1,1,NULL,NULL);
INSERT INTO "q_and_a" VALUES(5,1,'What''s an old man like you doing in a place like this?',3,0,1,6,NULL);
INSERT INTO "q_and_a" VALUES(6,1,'The old man says "I''ve been here for many years! Now leave me alone!"',NULL,1,1,NULL,NULL);
INSERT INTO "q_and_a" VALUES(7,2,'What kind of droid are you?',1,0,1,8,NULL);
INSERT INTO "q_and_a" VALUES(8,2,'The droid buzzes and bleeps. A small display lights up displaying the words "I AM A REPAIR DROID".',NULL,1,1,NULL,NULL);
CREATE TABLE "rooms" (
	`roomid`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`roomdesc`	TEXT,
	`roomname`	TEXT
);
INSERT INTO "rooms" VALUES(1,'You are on the planet Terris.  You are in a well funished apartment.  
There are comfortable sofas, and a large vision screen.  There is a bed 
in the corner.
','Apartment');
INSERT INTO "rooms" VALUES(2,'You are in a large undercover courtyard... In reality, it''s a metal platform suspended above part of the city.
In the centre there is a ciruclar fountain, above which hovers a swirling sculpture.  
There are many plants around you.  
People mill aroud you going about their business.','Courtyard');
INSERT INTO "rooms" VALUES(3,'You are in a small work room.  There is a distressed work bench, and various tools.
Cobwebs hang from the ceiling, and it looks like nobody has used the room for some time.','Workroom');
INSERT INTO "rooms" VALUES(4,'You find yourself next to a crashed escape pod.  Debris litters the ground.
Salvage droids are creeping around, searching for anything useful.','Crashed Escape Pod');
INSERT INTO "rooms" VALUES(6,'You are in a small loft area above the appartment.
It''s very dusty and smells of old computers, which you can see several of lying around.
A tent is here, which brings back fond memories of days camping.  
You remember the tent was owned by your Great Great grandfather.
','Loft');
INSERT INTO "rooms" VALUES(7,'You find yourself in the upper city south.  There is a statue of two hands 
floating in the air shaking hands It has a cube underneath it says
-Statue of Respect.-','Upper City South');
INSERT INTO "rooms" VALUES(8,'You are on a bridge across part of the city.  People walk back and forth across.
The bridge spans a gap in the city, and you can see the lower city far below.

','City Bridge');
INSERT INTO "rooms" VALUES(9,'You are out side the cantina door, there are two drunk men to the left of you.
above the cantina door it says cantina albar.
','Outside Cantina');
INSERT INTO "rooms" VALUES(10,'You are under an archway made from junk.  It doesn''t look very stable.
In the shadows underneath you can see the remains of a dwelling.
Nobody lives here now, though.
','Archway');
INSERT INTO "rooms" VALUES(11,'You are in a driod shop.  There are various droids for sale here, but there is
no sign of the shop keeper.','Droid Shop');
INSERT INTO "rooms" VALUES(12,'You find yourself in the middle of the cantina.  There is a counter with a barman serving.  There are stools in front of the bar. 
There is a group of tables to the left, where people are playing some kind of card game.

To the right of you is a large vision screen, showing what appears to be a race in progress.

You notice the air is full of a light mist, which seams to be coming from the glasses in peoples hands!

A notice says "Try our new Delmarbeer for the ultimate high!"','Cantina Albar');
INSERT INTO "rooms" VALUES(14,'You are a dim cantina side room. To the left a couple of men are buzy playing a
mysterious card game. You can just about make out the wording on the
cards: -Ziplac-','Cantina Side Room');
INSERT INTO "rooms" VALUES(15,'You''re on a narrow path leading between piles of junk in the lower city.
It looks like this is the rubbish tip for the whole city.

','Narrow Path');
INSERT INTO "rooms" VALUES(20,'You are at the elevator to the upper city.  The lower city stretches out before you.... a hive of scum and villany.  
There are piles of scrap metal on the side of the paths.  There are wires hanging out of the ceiling.','Lower City');
INSERT INTO "rooms" VALUES(21,'You are in front of the lower city door.  It''s an elevator that goes down to the lower city.  
There are posters which say, "DO NOT PASS, by order of BRANGOOR".

There is a security keycard reader on the door of the elevator, with a sign saying "Enter keycard".
','Lower City Elevator');
INSERT INTO "rooms" VALUES(22,'You are in a small dwelling, which is fashioned out of discarded metal panels
and junk.  It doesn''t look like a very comfortable place to live.
The earth beneath foot is damp and partly hidden a towering cabinet over 
flowing with tools.','Small Dwelling');
INSERT INTO "rooms" VALUES(23,'A large medical center building stands in front of you.  There is a large
double door which opens onto a reception area.','Medical Center');
INSERT INTO "rooms" VALUES(24,'You are outside a small shop.  There is a dirty old sign over the door which reads SHOP MILBRAGED.
A window displays books, alien bric a brak, and various weapons.','Outside Shop Milbraged');
INSERT INTO "rooms" VALUES(25,'You walk through the blue automatic door, you see rows and rows of shelves with a selection of tin can foods; bags of rice; super refreshing water; 
cheap alcohol that could be used as a weapon, foreign galactic ice cream and local alien meat.
You also see a book which says S.A.F.A (which is the special alien fighting agency) all alien fighting secrets revealed.  
And at the very back is the til.','Shop Milbraged');
INSERT INTO "rooms" VALUES(26,'You are in a very dark path between piles of junk.  You can dimly see
the junk towering above you.','Dark Path');
INSERT INTO "rooms" VALUES(27,'You are in a small dwelling, which is fashioned out of discarded metal panels
and junk.  It doesn''t look like a very comfortable place to live.
The earth beneath foot is damp and partly hidden a towering cabinet over 
flowing with tools.','Small Dwelling');
INSERT INTO "rooms" VALUES(28,'You''re in a large open junk area, with a dusty clearing in the middle.
A layer of dust covers everything, suggesting nothing has been touched
for a long time.
A strange humming noise pervades the air, and you can''t decern it''s source.','Junk Area');
INSERT INTO "rooms" VALUES(29,'You''re on a path through the lower city.  There are piles of junk all
around you, and it''s hard to find your way.

Possible exits are to the west, where you can see a narrow path.
To the north, you can see a way between piles of junk.
To the south, there is an archway made of junk.','Wide Path');
CREATE TABLE "npc" (
	`npcid`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`npcname`	TEXT NOT NULL,
	`npcshortdesc`	TEXT,
	`npclongdesc`	TEXT,
	`npcroom`	INTEGER NOT NULL,
	`npcstartroom`	INTEGER NOT NULL,
	`npcsrength`	INTEGER,
	`npchealth`	INTEGER,
	`npcstatus`	INTEGER
);
INSERT INTO "npc" VALUES(1,'Old Man','There is an old man here.','The old man is wearing rags, and has his head covered by a black hood.  
He doesn''t look like he''s in the mood for a chat, but you can''t help thinking with the right motivation he
would have a few interesting stories to tell.
',4,4,50,100,1);
INSERT INTO "npc" VALUES(2,'Repair Droid','You can see a repair droid here.','The repair droid is a ugly look utalitarian device, with various
arms sticking out.  It looks pretty dangerous in the wrong hands,
or with the wrong programming....',7,7,50,100,1);
CREATE TABLE "item" (
	`itemid`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`itemname`	TEXT NOT NULL,
	`itemdesc`	TEXT,
	`itemlevel`	INTEGER DEFAULT (1),
	`defaultroom`	INTEGER,
	`currentroom`	INTEGER,
	`itemdesc_short`	TEXT,
	`static`	INTEGER DEFAULT (0)
);
INSERT INTO "item" VALUES(1,'hammer','The hammer looks like a relic from a bygone era. It''s of a heavy steel contruction and looks 
like it could be used as a weapon in a pinch.',1,1,3,'There is a hammer here.',0);
INSERT INTO "item" VALUES(2,'diamond','The diamond is the size of a pea and gleams brightly. It has many facets, and looks 
like it would be worth a small fortune.',1,2,2,'You notice a diamond had been dropped here!',0);
INSERT INTO "item" VALUES(3,'keycard','You look closly at the keycard, it is small and grey. You can just make out the words LOWER CITY.',1,3,3,'A keycard has been discarded here.',0);
INSERT INTO "item" VALUES(4,'hard drive','The hard drive is black and has a title spintel.  On the other side is a laser proof glass, 
with wires behind it and a big circle in the middle, you notice on the side of the circle 
is small writing saying B213T.',1,6,6,'A hard drive lies here gathering dust.',0);
INSERT INTO "item" VALUES(5,'trophy cabinet','The cabiniet is unremarkable. It looks like it used to contain quite a few trophies.',1,1,1,'There is a trophy cabinet here.',1);
INSERT INTO "item" VALUES(6,'workbench','There isn''t much remarkable about the workbench.',1,3,3,'A workbench is along one wall.',1);
CREATE TABLE "object" (
	`objectid`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`objectdesc`	TEXT,
	`objectdesc_short`	TEXT,
	`roomid`	INTEGER,
	`objectname`	TEXT
);
INSERT INTO "object" VALUES(1,'There isn''t much remarkable about the workbench.','A long workbench is along one wall.',1,'workbench');
INSERT INTO "object" VALUES(2,'There is a single notice on the board. 
It says ''Come to the droid shop for the best deals
on R100 droids!''.','There is a notice board attached to one wall.',14,'notice board');
INSERT INTO "object" VALUES(3,'The bed is plain and unremarkable.  It doesn''t look very comfortable.','A bed is in the corner.',3,'bed');
INSERT INTO "object" VALUES(4,'The rock tower is contructed from large, flat,
square blocks of stone.  It''s quite high and you
can''t reach the top.
There is some writing scrwaled around the base,
which says ''All is red, all is white''.','A rock tower has been constructed here.',20,'rock tower');
CREATE TABLE "route" (
	`route_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`from_id`	INTEGER,
	`to_id`	INTEGER,
	`direction`	TEXT,
	`route_desc`	TEXT
);
INSERT INTO "route" VALUES(1,1,2,'s','To the south, you see a courtyard.');
INSERT INTO "route" VALUES(2,2,1,'n','To the north you can see your apartment.');
INSERT INTO "route" VALUES(3,1,3,'n','There is a small door leading north.');
INSERT INTO "route" VALUES(4,2,4,'w','To the west is a damaged escape pod.');
INSERT INTO "route" VALUES(5,2,7,'s','To the south is a walkway that leads to the upper city south.');
INSERT INTO "route" VALUES(6,1,6,'u','There is a ladder going up through a hatch in the ceiling.');
INSERT INTO "route" VALUES(7,6,1,'d','There is a ladder leading down to your apartment');
INSERT INTO "route" VALUES(8,7,9,'w','In the west you can see a Cantina.');
INSERT INTO "route" VALUES(9,8,21,'e','To the east is the door to the lower city.');
INSERT INTO "route" VALUES(10,3,1,'s','A small door is south of you.');
INSERT INTO "route" VALUES(11,10,11,'n','To the north you can see a wide path.');
INSERT INTO "route" VALUES(12,8,7,'w','In the west is a path to the Upper City South.');
INSERT INTO "route" VALUES(13,9,7,'e','In the east you can see the Upper City South.');
INSERT INTO "route" VALUES(14,9,12,'w','To the west of you there is the main entance to the cantina.');
INSERT INTO "route" VALUES(15,12,9,'e','The exit of the cantina is to the east.');
INSERT INTO "route" VALUES(16,12,14,'n','A door leads to a side room north of you.');
INSERT INTO "route" VALUES(17,14,12,'s','A door to the south leads back to the cantina.');
INSERT INTO "route" VALUES(18,7,2,'n','There is a courtyard area to the north.');
INSERT INTO "route" VALUES(19,15,20,'w','To the west you can see the elevator which leads to the upper city.');
INSERT INTO "route" VALUES(20,15,16,'e','There is a wide path to the east.');
INSERT INTO "route" VALUES(21,15,26,'n','A dark path appears to head northward between the piles of junk.');
INSERT INTO "route" VALUES(22,20,21,'w','The door to the upper city elevator is to the west.');
INSERT INTO "route" VALUES(23,20,15,'e','To the east you can see a narrow path, though the piles of scrap metal.');
INSERT INTO "route" VALUES(24,20,22,'n','A lower city dwelling is to the north of you.');
INSERT INTO "route" VALUES(25,21,23,'n','You can see what looks to be a medical center to the north.');
INSERT INTO "route" VALUES(26,22,20,'s','Possible exits are to the south, where you can see the lower city.');
INSERT INTO "route" VALUES(27,21,20,'e','The door of the elevator is to the east of you.');
INSERT INTO "route" VALUES(28,4,2,'e','In the east there is a courtyard.');
INSERT INTO "route" VALUES(29,2,4,'w','To the west, you can see the remains of a crashed escape pod.');
INSERT INTO "route" VALUES(30,7,8,'e','In the east you can see a bridge.');
INSERT INTO "route" VALUES(31,23,21,'s','To the south, there is the elevator back to the upper city.');
INSERT INTO "route" VALUES(32,9,24,'n','To the north, you can see what looks to be a shop of some kind.');
INSERT INTO "route" VALUES(33,24,9,'s','A cantina is located to the south of you.');
INSERT INTO "route" VALUES(34,24,25,'n','The door of the shop is north of you.');
INSERT INTO "route" VALUES(35,25,24,'s','The exit of the shop is south of you.');
INSERT INTO "route" VALUES(36,21,8,'w','In the west there is a bridge across the city.');
INSERT INTO "route" VALUES(37,26,15,'s','To the south there is a narrow path.');
INSERT INTO "route" VALUES(38,15,26,'n','Looking to the north there is a dark path.');
INSERT INTO "route" VALUES(39,10,27,'n','To the north, you can see a small dwelling.');
INSERT INTO "route" VALUES(40,27,10,'s','In the south, you can see the lower city.');
INSERT INTO "route" VALUES(41,13,29,'e','In the east there is a wider path.');
INSERT INTO "route" VALUES(42,29,13,'w','To the west you can see a narrow path.');
INSERT INTO "route" VALUES(43,29,28,'n','In a northerly direction there is what looks like a junk area.');
INSERT INTO "route" VALUES(44,29,2,'s','There is an archway to the south.');
INSERT INTO "route" VALUES(45,28,29,'s','To the south there is a wide path.');
CREATE TABLE "user" (
	`userid`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT,
	`score`	INT,
	`location`	INT,
	`health`	INT,
	`userdesc`	TEXT,
	`moves`	INTEGER NOT NULL DEFAULT (1)
);
INSERT INTO "user" VALUES(1,'Justin',0,3,100,'',122);
INSERT INTO "user" VALUES(2,'Jensen',1,1,100,'',125);
INSERT INTO "user" VALUES(3,'Ellie',0,1,100,'',11);
INSERT INTO "user" VALUES(4,'Amy',0,2,100,'A tall teenager',8);
INSERT INTO "user" VALUES(5,'Testing',0,7,100,'',2);
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('inventory',18);
INSERT INTO "sqlite_sequence" VALUES('q_and_a',8);
INSERT INTO "sqlite_sequence" VALUES('rooms',29);
INSERT INTO "sqlite_sequence" VALUES('npc',2);
INSERT INTO "sqlite_sequence" VALUES('item',6);
INSERT INTO "sqlite_sequence" VALUES('object',4);
INSERT INTO "sqlite_sequence" VALUES('route',45);
INSERT INTO "sqlite_sequence" VALUES('user',6);
COMMIT;
