#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import re
import json

import MySQLdb

config_file = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__))), 'config.jso')

load = {}
try:
	with open(config_file, 'rb') as data:
		load.update(json.load(data))
except ValueError:
	print 'Error with configuration file'
	sys.exit(-1)

db = MySQLdb.connect(host=load.get('db_host'),    # your host, usually localhost
                     user=load.get('db_user'),         # your username
                     passwd=load.get('db_pass'),  # your password
                     db=load.get('db_name'))        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

bot_id = sys.argv[1]
bot_login = ""
bot_pass = ""

line = ['test1', '#test2', '@test3']
new_line = []
for key in line:
	new_line.append(re.sub('[@#]', '', key))

print new_line

# Get data from database
try:
    numrows = cur.execute("SELECT * FROM bots WHERE bot_id = %s", bot_id)
    rows = cur.fetchall()
except MySQLdb.Error, e:
    try:
        print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
    except IndexError:
        print "MySQL Error: %s" % str(e)

# print all the first cell of all the rows
if numrows > 0:
    for row in rows:
	tags = row[18]
	if tags is not None:
	#	tags = dict((key, '') for key in tags.split(','))
		tags = dict((key, '') for key in tags.split(','))
	else:
		tags = 'test'
        print tags

else:
    print "Bot ID '%s' NOT found." % bot_id

cur.close()
db.close()
